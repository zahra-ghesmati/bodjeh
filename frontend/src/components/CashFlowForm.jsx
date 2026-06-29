import { useEffect, useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { apiFetch } from "../services/api";
import "./GenericForm.css";
import NumericCell from "./NumericCell";

const COMPANIES = [
  "سيمان مازندران",
  "گروه صنايع سيمان کرمان",
  "بين المللي ساروج بوشهر",
  "سيمان شمال",
  "توليدي سيمان فيروزکوه",
];

const SAROJ = "بين المللي ساروج بوشهر";

// ردیف‌هایی که جمع کل دریافتی/پرداختی هستند (برای چک 5%)
const JAMC_DARYAFTI = "جمع وجوه دریافتی";
const JAMC_PARDAKHTI = "جمع وجوه پرداختی";
const SAYR_DARYAFTI_KEYS = ["سایر دریافت‌ها*", "سایر دریافتی‌ها*"];
const SAYR_PARDAKHTI_KEYS = ["سایر پرداخت‌ها*", "سایر پرداختی‌ها*"];

function toNum(v) {
  const n = parseFloat(String(v ?? "").replace(/,/g, ""));
  return isNaN(n) ? 0 : n;
}

function calcSum(values, monthFields) {
  return monthFields.reduce((s, f) => s + toNum(values[f]), 0);
}

export default function CashFlowForm() {
  const [meta, setMeta] = useState(null);
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);
  const [approval, setApproval] = useState(null);
  const [years, setYears] = useState([]);
  const [company, setCompany] = useState(COMPANIES[0]);
  const [year, setYear] = useState("");

  // ---- load base ----
  useEffect(() => {
    (async () => {
      try {
        const userRes = await apiFetch("/me");
        const user = await userRes.json();
        setCurrentUser(user);
        if (user.role === "COMPANY_USER" && user.companies?.length) {
          setCompany(user.companies[0]);
        }

        const yearRes = await apiFetch("/api/months/years");
        const ys = await yearRes.json();
        const list = Array.isArray(ys) ? ys : [];
        setYears(list);
        if (list.length) setYear(list[0]);
      } catch (e) {
        console.error(e);
      }
    })();

    (async () => {
      try {
        const res = await apiFetch("/forms/cash_flow/meta");
        setMeta(await res.json());
      } catch (e) {
        console.error(e);
      }
    })();
  }, []);

  // ---- load rows + approval when filters change ----
  useEffect(() => {
    if (company && year) {
      loadRows();
      loadApproval();
    }
  }, [company, year]);

  async function loadRows() {
    setLoading(true);
    try {
      const res = await apiFetch(
        `/forms/cash_flow/rows?company=${encodeURIComponent(company)}&year=${encodeURIComponent(year)}`
      );
      const data = await res.json();
      setRows(Array.isArray(data) ? data : []);
    } catch (e) {
      alert("خطای شبکه در دریافت داده‌ها");
    } finally {
      setLoading(false);
    }
  }

  async function loadApproval() {
    try {
      const res = await apiFetch(
        `/approvals/status?form_key=cash_flow&company=${encodeURIComponent(company)}&year=${encodeURIComponent(year)}&month=annual`
      );
      setApproval(await res.json());
    } catch (e) {
      console.error(e);
    }
  }

  // ---- edit ----
  function updateCell(index, field, value) {
    setRows((prev) => {
      const next = [...prev];
      next[index] = {
        ...next[index],
        values: { ...next[index].values, [field]: value },
      };
      return next;
    });
  }

  function addRow() {
    const monthFields = meta?.month_fields ?? [];
    const empty = { nvan: "", shrh: "", mjmv: "" };
    monthFields.forEach((f) => (empty[f] = ""));
    setRows((prev) => [...prev, { id: null, tempId: Date.now(), values: empty }]);
  }

  function deleteRow(index) {
    setRows((prev) => prev.filter((_, i) => i !== index));
  }

  const [visibleSums, setVisibleSums] = useState({});
  function toggleSum(field) {
    setVisibleSums(prev => ({ ...prev, [field]: !prev[field] }));
  }
  function calcColSum(field) {
    return rows.reduce((sum, row) => {
      const v = parseFloat(row.values?.[field]);
      return sum + (isNaN(v) ? 0 : v);
    }, 0);
  }

  // ---- validation ----
  function validate() {
    const monthFields = meta?.month_fields ?? [];
    const warnings = [];

    rows.forEach((row, i) => {
      const nvan = row.values?.nvan ?? "";
      const mjmv = toNum(row.values?.mjmv);
      const calcMjmv = calcSum(row.values ?? {}, monthFields);

      // چک جمع مجموع
      if (mjmv !== 0 && calcMjmv !== 0 && Math.abs(mjmv - calcMjmv) > 1) {
        warnings.push(
          `ردیف ${i + 1} (${nvan}): مجموع وارد شده (${mjmv.toLocaleString()}) با جمع ماه‌ها (${calcMjmv.toLocaleString()}) مطابقت ندارد.`
        );
      }
    });

    // چک 5% سایر دریافتی
    const jamdRow = rows.find((r) => r.values?.nvan === JAMC_DARYAFTI);
    if (jamdRow) {
      const jamdTotal = toNum(jamdRow.values?.mjmv) || calcSum(jamdRow.values ?? {}, monthFields);
      SAYR_DARYAFTI_KEYS.forEach((key) => {
        const sayrRow = rows.find((r) => r.values?.nvan === key);
        if (sayrRow && jamdTotal > 0) {
          const sayrTotal = toNum(sayrRow.values?.mjmv) || calcSum(sayrRow.values ?? {}, monthFields);
          if (sayrTotal > jamdTotal * 0.05) {
            warnings.push(
              `«سایر دریافت‌ها» (${sayrTotal.toLocaleString()}) بیشتر از ۵٪ جمع وجوه دریافتی (${(jamdTotal * 0.05).toLocaleString()}) است.`
            );
          }
        }
      });
    }

    // چک 5% سایر پرداختی
    const jampRow = rows.find((r) => r.values?.nvan === JAMC_PARDAKHTI);
    if (jampRow) {
      const jampTotal = toNum(jampRow.values?.mjmv) || calcSum(jampRow.values ?? {}, monthFields);
      SAYR_PARDAKHTI_KEYS.forEach((key) => {
        const sayrRow = rows.find((r) => r.values?.nvan === key);
        if (sayrRow && jampTotal > 0) {
          const sayrTotal = toNum(sayrRow.values?.mjmv) || calcSum(sayrRow.values ?? {}, monthFields);
          if (sayrTotal > jampTotal * 0.05) {
            warnings.push(
              `«سایر پرداخت‌ها» (${sayrTotal.toLocaleString()}) بیشتر از ۵٪ جمع وجوه پرداختی (${(jampTotal * 0.05).toLocaleString()}) است.`
            );
          }
        }
      });
    }

    return warnings;
  }

  // ---- save ----
  async function saveRows() {
    if (!company || !year) {
      alert("شرکت و سال را انتخاب کنید");
      return;
    }

    const warnings = validate();
    if (warnings.length > 0) {
      const msg =
        "⚠️ هشدارهای زیر شناسایی شد:\n\n" +
        warnings.join("\n") +
        "\n\nآیا با وجود این هشدارها ذخیره شود؟";
      if (!window.confirm(msg)) return;
    }

    setSaving(true);
    try {
      const payload = {
        company,
        year,
        rows: rows.map((row) => ({
          id: row.id ?? null,
          values: row.values,
        })),
      };

      const res = await apiFetch("/forms/cash_flow/save", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await res.json();
      if (!res.ok) {
        alert(data.detail || "خطا در ذخیره");
        return;
      }
      alert("اطلاعات با موفقیت ذخیره شد");
      await loadRows();
    } catch (e) {
      alert("خطای شبکه");
    } finally {
      setSaving(false);
    }
  }

  // ---- approval ----
  async function doApproval(url, method) {
    try {
      const res = await apiFetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ form_key: "cash_flow", company, year, month: "annual" }),
      });
      const data = await res.json();
      if (!res.ok) {
        alert(data.detail || "خطا");
        return;
      }
      await loadApproval();
      await loadRows();
    } catch (e) {
      alert("خطای شبکه");
    }
  }

  const isAdmin =
    currentUser?.role === "ADMIN" || currentUser?.role === "ADMINISTRATOR";
  const isSuperAdmin = currentUser?.role === "ADMINISTRATOR";
  const isLocked = approval?.budget_approved ?? false;

  const visibleCompanies =
    currentUser?.role === "COMPANY_USER" ? currentUser.companies : COMPANIES;

  const monthFields = meta?.month_fields ?? [];
  const monthLabels = meta?.month_labels ?? {};

  // ---- render ----
  return (
    <MainLayout>
      <div className="page">
        <h2 className="text-center mb-4">جریان وجوه نقد</h2>

        {/* فیلترها */}
        <div className="controls">
          <div className="controls-grid">
            <div className="field">
              <label>شرکت:</label>
              <select
                className="form-select"
                value={company}
                onChange={(e) => setCompany(e.target.value)}
              >
                {visibleCompanies.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </div>
            <div className="field">
              <label>سال مالی:</label>
              <select
                className="form-select"
                value={year}
                onChange={(e) => setYear(e.target.value)}
              >
                {years.map((y) => (
                  <option key={y} value={y}>
                    {y}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </div>

        {/* approval panel */}
        {approval && (
          <div className="approval-panel">
            <div className="approval-header">
              <h6>وضعیت تایید گزارش</h6>
            </div>
            <div className="approval-content">
              <div className="approval-statuses">
                <div className={`approval-card ${isLocked ? "approved" : "pending"}`}>
                  <div className="approval-icon">{isLocked ? "✓" : "⏳"}</div>
                  <div>
                    <div className="approval-title">وضعیت گزارش</div>
                    <div className="approval-value">
                      {isLocked ? "تایید شده" : "در انتظار تایید"}
                    </div>
                  </div>
                </div>
              </div>
              <div className="approval-actions">
                {isAdmin && !isLocked && (
                  <button
                    className="btn btn-success approval-btn"
                    onClick={() => doApproval("/approvals/budget", "POST")}
                  >
                    تایید گزارش
                  </button>
                )}
                {isSuperAdmin && isLocked && (
                  <button
                    className="btn btn-outline-secondary approval-btn"
                    onClick={() => doApproval("/approvals/budget", "DELETE")}
                  >
                    لغو تایید
                  </button>
                )}
              </div>
            </div>
          </div>
        )}

        {/* جدول */}
        <div className="table-card">
          <div className="save-footer">
            {isAdmin && (
              <button
                className="btn btn-success"
                onClick={addRow}
                disabled={isLocked}
                style={{ marginLeft: "10px" }}
              >
                + افزودن ردیف
              </button>
            )}
            <button
              className="btn-save"
              onClick={saveRows}
              disabled={saving || isLocked}
            >
              {saving ? "در حال ذخیره..." : "ذخیره تغییرات"}
            </button>
          </div>

          <div className="table-responsive">
            <table className="table table-hover align-middle mb-0 cost-table">
              <thead>
                <tr>
                  {isAdmin && <th style={{ width: "40px" }}></th>}
                  <th>عنوان</th>
                  <th>شرح</th>
                  {monthFields.map((f) => (
                    <th key={f}>{monthLabels[f] ?? f}</th>
                  ))}
                  <th>مجموع</th>
                </tr>
                {/* ردیف دکمه‌های جمع ستون */}
                <tr className="col-sum-row">
                  {isAdmin && <td></td>}
                  <td></td>
                  <td></td>
                  {monthFields.map((f) => (
                    <td key={f} style={{ padding: "2px 6px" }}>
                      <button
                        className="btn btn-link btn-sm p-0 col-sum-btn"
                        onClick={() => toggleSum(f)}
                        title="نمایش جمع ستون"
                      >Σ</button>
                      {visibleSums[f] && (
                        <span className="col-sum-value">
                          {Math.round(calcColSum(f)).toLocaleString("en-US")}
                        </span>
                      )}
                    </td>
                  ))}
                  <td style={{ padding: "2px 6px" }}>
                    <button
                      className="btn btn-link btn-sm p-0 col-sum-btn"
                      onClick={() => toggleSum("mjmv")}
                      title="نمایش جمع ستون"
                    >Σ</button>
                    {visibleSums["mjmv"] && (
                      <span className="col-sum-value">
                        {Math.round(calcColSum("mjmv")).toLocaleString("en-US")}
                      </span>
                    )}
                  </td>
                </tr>
              </thead>
              <tbody>
                {loading && (
                  <tr><td colSpan={monthFields.length + 4}>در حال دریافت...</td></tr>
                )}
                {!loading && rows.length === 0 && (
                  <tr><td colSpan={monthFields.length + 4}>داده‌ای وجود ندارد</td></tr>
                )}
                {!loading && rows.map((row, index) => (
                  <tr key={row.id ?? row.tempId ?? index}>
                    {isAdmin && (
                      <td>
                        <button
                          className="btn btn-sm btn-outline-danger"
                          disabled={isLocked}
                          onClick={() => deleteRow(index)}
                          title="حذف ردیف"
                        >×</button>
                      </td>
                    )}
                    {/* عنوان - فقط نمایشی */}
                    <td style={{ minWidth: "200px", fontWeight: "500" }}>
                      {row.values?.nvan ?? "-"}
                    </td>
                    {/* شرح - قابل ویرایش */}
                    <td style={{ minWidth: "160px" }}>
                      <input
                        className="form-control"
                        type="text"
                        disabled={isLocked}
                        value={row.values?.shrh ?? ""}
                        onChange={(e) => updateCell(index, "shrh", e.target.value)}
                      />
                    </td>
                    {/* ماه‌ها */}
                    {monthFields.map((f) => (
                      <td key={f} style={{ minWidth: "100px" }}>
                        <NumericCell
                          value={row.values?.[f]}
                          disabled={isLocked}
                          onChange={(val) => updateCell(index, f, val)}
                        />
                      </td>
                    ))}
                    {/* مجموع */}
                    <td style={{ minWidth: "110px" }}>
                      <NumericCell
                        value={row.values?.mjmv}
                        disabled={isLocked}
                        onChange={(val) => updateCell(index, "mjmv", val)}
                      />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="save-footer">
            <button
              className="btn-save"
              onClick={saveRows}
              disabled={saving || isLocked}
            >
              {saving ? "در حال ذخیره..." : "ذخیره تغییرات"}
            </button>
          </div>
        </div>
      </div>
    </MainLayout>
  );
}
