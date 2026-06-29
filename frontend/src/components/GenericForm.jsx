import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";
import { apiFetch } from "../services/api";
import "./GenericForm.css";
import NumericCell from "./NumericCell";
import { useSearchParams } from "react-router-dom";

export default function GenericForm({ formKey }) {
  const [meta, setMeta] = useState(null);
  const [currentUser, setCurrentUser] = useState(null);
  const [searchParams] = useSearchParams();

  const [approvalStatus, setApprovalStatus] = useState({
    budget_approved: false,
    actual_approved: false,
  });
  const companies = ["سيمان مازندران", "گروه صنايع سيمان کرمان", "بين المللي ساروج بوشهر", "سيمان شمال", "توليدي سيمان فيروزکوه"];

  const months = ["فروردين", "ارديبهشت", "خرداد", "تير", "مرداد", "شهريور", "مهر", "آبان", "آذر", "دي", "بهمن", "اسفند"];

  const [years, setYears] = useState([]);
  const [rows, setRows] = useState([]);
  const [saving, setSaving] = useState(false);
  const [visibleSums, setVisibleSums] = useState({});

  function toggleSum(key) {
    setVisibleSums(prev => ({ ...prev, [key]: !prev[key] }));
  }

  function calcColSum(key) {
    return (Array.isArray(rows) ? rows : []).reduce((sum, row) => {
      const v = parseFloat(row[key]);
      return sum + (isNaN(v) ? 0 : v);
    }, 0);
  }
  const visibleCompanies = currentUser?.role === "COMPANY_USER" ? currentUser.companies : companies;
  const [selectedCompany, setSelectedCompany] = useState("");

  const [selectedYear, setSelectedYear] = useState("");

  const [selectedMonth, setSelectedMonth] = useState("");
  // ۱. این بلوک وقتی فرم عوض می‌شود (مثلاً از منو) همه چیز را ریست می‌کند
  useEffect(() => {
    setRows([]);
    setApprovalStatus({ budget_approved: false, actual_approved: false });

    // ابتدا پارامترهای URL را چک می‌کنیم
    const qCompany = searchParams.get("company");
    const qYear = searchParams.get("year");
    const qMonth = searchParams.get("month");

    if (qCompany) setSelectedCompany(qCompany);
    if (qYear) setSelectedYear(qYear);
    if (qMonth) setSelectedMonth(qMonth);
    else setSelectedMonth("فروردين"); // پیش‌فرض برای ورود مستقیم

    // حالا اطلاعات پایه را لود می‌کنیم
    loadYears();
    loadCurrentUser();
    loadMeta();
  }, [formKey, searchParams]); // وقتی فرم عوض شد، دوباره اجرا شود

  // ۲. این بلوک فقط وقتی اجرا می‌شود که هر ۳ فیلتر پر شده باشند (برای لود کردن دیتا)
  useEffect(() => {
    if (selectedCompany && selectedYear && selectedMonth) {
      loadRows();
      loadApprovalStatus();
    }
  }, [formKey, selectedCompany, selectedYear, selectedMonth]);

  async function loadMeta() {
    try {
      const response = await apiFetch(`/forms/${formKey}/meta`);

      const data = await response.json();

      setMeta(data);
    } catch (error) {
      console.error(error);
    }
  }
  async function loadCurrentUser() {
    try {
      const response = await apiFetch("/me");
      const data = await response.json();
      setCurrentUser(data);

      // اگر از قبل (توسط URL) انتخاب نشده بود، حالا پیش‌فرض ست کن
      setSelectedCompany((prev) => {
        if (prev) return prev; // اگر پر است، دست نزن
        if (data.role === "COMPANY_USER" && data.companies.length > 0) return data.companies[0];
        return companies[0];
      });
    } catch (error) {
      console.error(error);
    }
  }

  async function approveBudget() {
    try {
      const response = await apiFetch("/approvals/budget", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          form_key: formKey,

          company: selectedCompany,

          year: selectedYear,

          month: selectedMonth,
        }),
      });
      const data = await response.json();

      if (!response.ok) {
        alert(data.detail || "خطا در تایید بودجه");

        return;
      }
      await loadApprovalStatus();
      await loadRows();
    } catch (error) {
      console.error(error);
      alert("خطای شبکه");
    }
  }
  async function approveActual() {
    try {
      const response = await apiFetch("/approvals/actual", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          form_key: formKey,

          company: selectedCompany,

          year: selectedYear,

          month: selectedMonth,
        }),
      });
      const data = await response.json();

      if (!response.ok) {
        alert(data.detail || "خطا در تایید بودجه");

        return;
      }
      await loadApprovalStatus();
      await loadRows();
    } catch (error) {
      console.error(error);
    }
  }
  async function unapproveBudget() {
    try {
      await apiFetch("/approvals/budget", {
        method: "DELETE",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          form_key: formKey,
          company: selectedCompany,
          year: selectedYear,
          month: selectedMonth,
        }),
      });

      await loadApprovalStatus();
      await loadRows();
    } catch (error) {
      console.error(error);
    }
  }
  async function unapproveActual() {
    try {
      await apiFetch("/approvals/actual", {
        method: "DELETE",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          form_key: formKey,
          company: selectedCompany,
          year: selectedYear,
          month: selectedMonth,
        }),
      });

      await loadApprovalStatus();
      await loadRows();
    } catch (error) {
      console.error(error);
    }
  }
  async function loadApprovalStatus() {
    if (!selectedCompany || !selectedYear || !selectedMonth) {
      return;
    }
    try {
      const response = await apiFetch(
        `/approvals/status?form_key=${formKey}&company=${encodeURIComponent(selectedCompany)}&year=${encodeURIComponent(selectedYear)}&month=${encodeURIComponent(selectedMonth)}`,
      );

      const data = await response.json();

      setApprovalStatus(data);
    } catch (error) {
      console.error(error);
    }
  }
  async function loadYears() {
    try {
      const response = await apiFetch("/api/months/years");
      const data = await response.json();
      setYears(data);

      // اگر از قبل (توسط URL) انتخاب نشده بود، حالا پیش‌فرض ست کن
      setSelectedYear((prev) => {
        if (prev) return prev; // اگر پر است، دست نزن
        return data.length > 0 ? data[0] : "";
      });
    } catch (error) {
      console.error(error);
    }
  }

  async function loadRows() {
    if (!selectedCompany || !selectedYear || !selectedMonth) {
      return;
    }
    try {
      const response = await apiFetch(`/forms/${formKey}/rows?company=${encodeURIComponent(selectedCompany)}&year=${encodeURIComponent(selectedYear)}&month=${encodeURIComponent(selectedMonth)}`);

      const data = await response.json();

      if (!response.ok) {
        setRows([]);

        alert(data.detail || "خطا در دریافت اطلاعات");

        return;
      }

      setRows(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error(error);
    }
  }
  async function saveRows() {
    try {
      setSaving(true);
      console.log(
        rows.map((row) => ({
          budget: row.budget,
          actual: row.actual,
        })),
      );
      const response = await apiFetch(`/forms/${formKey}/save`, {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          company: selectedCompany,
          year: selectedYear,
          month: selectedMonth,

          rows: rows.map((row) => ({
            id: row.id,

            dimension1: row.dimension1,

            dimension2: row.dimension2,

            dimension3: row.dimension3,

            budget: row.budget === "" || row.budget === null || row.budget === undefined ? null : Number(row.budget),

            actual: row.actual === "" || row.actual === null || row.actual === undefined ? null : Number(row.actual),
          })),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail || "خطا در ذخیره");

        return;
      }

      alert("اطلاعات ذخیره شد");

      await loadRows();
    } catch (error) {
      console.error(error);

      alert("خطای شبکه");
    } finally {
      setSaving(false);
    }
  }

  return (
    <MainLayout>
      <div className="page">
        <h2 className="text-center mb-4">{meta?.title}</h2>

        <div className="controls">
          <div className="controls-grid">
            <div className="field">
              <label>شرکت:</label>

              <select className="form-select" value={selectedCompany} onChange={(e) => setSelectedCompany(e.target.value)}>
                {visibleCompanies.map((company) => (
                  <option key={company} value={company}>
                    {company}
                  </option>
                ))}
              </select>
            </div>

            <div className="field">
              <label>سال مالی:</label>

              <select className="form-select" value={selectedYear} onChange={(e) => setSelectedYear(e.target.value)}>
                {years.map((year) => (
                  <option key={year} value={year}>
                    {year}
                  </option>
                ))}
              </select>
            </div>

            <div className="field">
              <label>ماه گزارش:</label>

              <select className="form-select" value={selectedMonth} onChange={(e) => setSelectedMonth(e.target.value)}>
                {months.map((month) => (
                  <option key={month} value={month}>
                    {month}
                  </option>
                ))}
              </select>
            </div>
          </div>
        </div>
        <div className="approval-panel">
          <div className="approval-header">
            <h6>وضعیت تایید گزارش</h6>
          </div>

          <div className="approval-content">
            <div className="approval-statuses">
              <div className={`approval-card ${approvalStatus.budget_approved ? "approved" : "pending"}`}>
                <div className="approval-icon">{approvalStatus.budget_approved ? "✓" : "⏳"}</div>

                <div>
                  <div className="approval-title">بودجه</div>

                  <div className="approval-value">{approvalStatus.budget_approved ? "تایید شده" : "در انتظار تایید"}</div>
                </div>
              </div>

              <div className={`approval-card ${approvalStatus.actual_approved ? "approved" : "pending"}`}>
                <div className="approval-icon">{approvalStatus.actual_approved ? "✓" : "⏳"}</div>

                <div>
                  <div className="approval-title">عملکرد</div>

                  <div className="approval-value">{approvalStatus.actual_approved ? "تایید شده" : "در انتظار تایید"}</div>
                </div>
              </div>
            </div>

            <div className="approval-actions">
              {(currentUser?.role === "ADMIN" || currentUser?.role === "ADMINISTRATOR") && !approvalStatus.budget_approved && (
                <button className="btn btn-success approval-btn" onClick={approveBudget}>
                  تایید بودجه
                </button>
              )}

              {(currentUser?.role === "ADMIN" || currentUser?.role === "ADMINISTRATOR") && !approvalStatus.actual_approved && (
                <button className="btn btn-primary approval-btn" onClick={approveActual}>
                  تایید عملکرد
                </button>
              )}

              {currentUser?.role === "ADMINISTRATOR" && approvalStatus.budget_approved && (
                <button className="btn btn-outline-secondary approval-btn" onClick={unapproveBudget}>
                  لغو تایید بودجه
                </button>
              )}

              {currentUser?.role === "ADMINISTRATOR" && approvalStatus.actual_approved && (
                <button className="btn btn-outline-secondary approval-btn" onClick={unapproveActual}>
                  لغو تایید عملکرد
                </button>
              )}
            </div>
          </div>
        </div>

        <div className="table-card">
          <div className="save-footer">
            <button className="btn-save" onClick={saveRows} disabled={saving || (approvalStatus.budget_approved && approvalStatus.actual_approved)}>
              {saving ? "در حال ذخیره..." : "ذخیره تغییرات"}
            </button>
          </div>
          <div className="table-responsive">
            <table className="table table-hover align-middle mb-0 cost-table">
              <colgroup>
                {meta?.columns?.map((col) => (
                  <col key={col.key} />
                ))}
                <col style={{ width: "180px" }} />
                <col style={{ width: "180px" }} />
              </colgroup>
              <thead>
                <tr>
                  {meta?.columns?.map((col) => (
                    <th key={col.key}>{col.title}</th>
                  ))}

                  <th>بودجه</th>

                  <th>عملکرد (واقعی)</th>
                </tr>
                {/* ردیف جمع ستون‌ها */}
                <tr className="col-sum-row">
                  {meta?.columns?.map((col) => (
                    <td key={col.key}></td>
                  ))}
                  <td style={{ padding: "2px 6px" }}>
                    <button className="btn btn-link btn-sm p-0 col-sum-btn" onClick={() => toggleSum("budget")} title="جمع بودجه">Σ</button>
                    {visibleSums["budget"] && (
                      <span className="col-sum-value">{Math.round(calcColSum("budget")).toLocaleString("en-US")}</span>
                    )}
                  </td>
                  <td style={{ padding: "2px 6px" }}>
                    <button className="btn btn-link btn-sm p-0 col-sum-btn" onClick={() => toggleSum("actual")} title="جمع عملکرد">Σ</button>
                    {visibleSums["actual"] && (
                      <span className="col-sum-value">{Math.round(calcColSum("actual")).toLocaleString("en-US")}</span>
                    )}
                  </td>
                </tr>
              </thead>

              <tbody>
                {(Array.isArray(rows) ? rows : []).map((row, index) => (
                  <tr key={row.id ?? index}>
                    {meta?.columns?.map((col) => (
                      <td key={col.key}>{row[col.key]}</td>
                    ))}

                    <td>
                      <NumericCell
                        value={row.budget}
                        disabled={approvalStatus.budget_approved}
                        onChange={(val) => {
                          const newRows = [...rows];
                          newRows[index].budget = val;
                          setRows(newRows);
                        }}
                      />
                    </td>

                    <td>
                      <NumericCell
                        value={row.actual}
                        disabled={approvalStatus.actual_approved}
                        onChange={(val) => {
                          const newRows = [...rows];
                          newRows[index].actual = val;
                          setRows(newRows);
                        }}
                      />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div className="save-footer">
            <button className="btn-save" onClick={saveRows} disabled={saving || (approvalStatus.budget_approved && approvalStatus.actual_approved)}>
              {saving ? "در حال ذخیره..." : "ذخیره تغییرات"}
            </button>
          </div>
        </div>
      </div>
    </MainLayout>
  );
}
