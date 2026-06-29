import { useEffect, useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { apiFetch } from "../services/api";
import "./GenericForm.css";
import NumericCell from "./NumericCell";

export default function DynamicDataForm({ formKey }) {
  const [meta, setMeta] = useState(null);
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);
  const [approval, setApproval] = useState(null);

  const companies = ["سيمان مازندران", "گروه صنايع سيمان کرمان", "بين المللي ساروج بوشهر", "سيمان شمال", "توليدي سيمان فيروزکوه"];
  const months = ["فروردين", "ارديبهشت", "خرداد", "تير", "مرداد", "شهريور", "مهر", "آبان", "آذر", "دي", "بهمن", "اسفند"];
  const [years, setYears] = useState([]);
  const [company, setCompany] = useState("");
  const [year, setYear] = useState("");
  const [month, setMonth] = useState("فروردين");

  // ---- helpers ----
  const approvalType = meta?.approval?.type ?? "single";
  const budgetFields = meta?.approval?.budget_fields ?? [];
  const actualFields = meta?.approval?.actual_fields ?? [];

  // آیا ستون قفل شده؟
  function isFieldLocked(field) {
    if (!approval) return false;
    if (approvalType === "single") {
      return approval.budget_approved; // single = budget_approved کل فرم رو قفل می‌کنه
    }
    // double
    if (budgetFields.includes(field) && approval.budget_approved) return true;
    if (actualFields.includes(field) && approval.actual_approved) return true;
    return false;
  }

  // آیا دکمه ذخیره غیرفعاله؟
  function isSaveLocked() {
    if (!approval) return false;
    if (approvalType === "single") return approval.budget_approved;
    return approval.budget_approved && approval.actual_approved;
  }

  // ---- load ----
  useEffect(() => {
    setRows([]); setMeta(null); setApproval(null);
    loadMeta(); loadBase();
  }, [formKey]);

  useEffect(() => {
    if (company && year && month) {
      loadRows(); loadApproval();
    }
  }, [company, year, month, formKey]);

  async function loadBase() {
    try {
      const userRes = await apiFetch("/me");
      const user = await userRes.json();
      setCurrentUser(user);
      setCompany(user.role === "COMPANY_USER" && user.companies?.length ? user.companies[0] : "سيمان مازندران");

      const yearRes = await apiFetch("/api/months/years");
      const ys = await yearRes.json();
      setYears(Array.isArray(ys) ? ys : []);
      if (Array.isArray(ys) && ys.length) setYear(ys[0]);
    } catch (e) { console.error(e); }
  }

  async function loadMeta() {
    try {
      const res = await apiFetch(`/forms/${formKey}/meta`);
      const data = await res.json();
      if (!res.ok) { alert(data.detail || "خطا در دریافت ساختار فرم"); return; }
      setMeta(data);
    } catch (e) { alert("خطای شبکه در دریافت ساختار فرم"); }
  }

  async function loadApproval() {
    try {
      const res = await apiFetch(`/approvals/status?form_key=${formKey}&company=${encodeURIComponent(company)}&year=${encodeURIComponent(year)}&month=${encodeURIComponent(month)}`);
      setApproval(await res.json());
    } catch (e) { console.error(e); }
  }

  async function loadRows() {
    if (!company || !year || !month) return;
    setLoading(true);
    try {
      const res = await apiFetch(`/forms/${formKey}/rows?company=${encodeURIComponent(company)}&year=${encodeURIComponent(year)}&month=${encodeURIComponent(month)}`);
      const data = await res.json();
      if (!res.ok) { setRows([]); alert(data.detail || "خطا"); return; }
      setRows(Array.isArray(data) ? data : []);
    } catch (e) { setRows([]); alert("خطای شبکه"); }
    finally { setLoading(false); }
  }

  // ---- approval actions ----
  async function doApproval(url, method) {
    try {
      const res = await apiFetch(url, {
        method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ form_key: formKey, company, year, month }),
      });
      const data = await res.json();
      if (!res.ok) { alert(data.detail || "خطا"); return; }
      await loadApproval(); await loadRows();
    } catch (e) { alert("خطای شبکه"); }
  }

  // ---- edit ----
  function updateCell(index, field, value) {
    setRows(prev => {
      const next = [...prev];
      next[index] = { ...next[index], values: { ...(next[index].values || {}), [field]: value } };
      return next;
    });
  }

  function addRow() {
    const empty = {};
    meta?.columns?.forEach(col => { empty[col.field] = ""; });
    setRows(prev => [...prev, { id: null, tempId: Date.now(), values: empty }]);
  }

  function deleteRow(index) {
    setRows(prev => prev.filter((_, i) => i !== index));
  }

  // جمع هر ستون عددی
  function calcColSum(field) {
    return rows.reduce((sum, row) => {
      const v = parseFloat(row.values?.[field]);
      return sum + (isNaN(v) ? 0 : v);
    }, 0);
  }

  const [visibleSums, setVisibleSums] = useState({});
  function toggleSum(field) {
    setVisibleSums(prev => ({ ...prev, [field]: !prev[field] }));
  }

  async function saveRows() {
    if (!company || !year || !month) { alert("شرکت، سال و ماه را انتخاب کنید"); return; }
    try {
      setSaving(true);
      const payload = {
        company, year, month,
        rows: rows.map(row => ({
          id: row.id,
          values: Object.fromEntries(
            (meta?.columns || []).map(col => {
              const v = row.values?.[col.field];
              return [col.field, (v === "" || v == null) ? null : col.type === "number" ? Number(v) : v];
            })
          ),
        })),
      };
      const res = await apiFetch(`/forms/${formKey}/save`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      if (!res.ok) { alert(data.detail || "خطا در ذخیره"); return; }
      alert("اطلاعات ذخیره شد");
      await loadRows();
    } catch (e) { alert("خطای شبکه"); }
    finally { setSaving(false); }
  }

  const isAdmin = currentUser?.role === "ADMIN" || currentUser?.role === "ADMINISTRATOR";
  const isSuperAdmin = currentUser?.role === "ADMINISTRATOR";

  // ---- render approval panel ----
  function renderApprovalPanel() {
    if (!approval) return null;

    if (approvalType === "single") {
      return (
        <div className="approval-panel">
          <div className="approval-header"><h6>وضعیت تایید گزارش</h6></div>
          <div className="approval-content">
            <div className="approval-statuses">
              <div className={`approval-card ${approval.budget_approved ? "approved" : "pending"}`}>
                <div className="approval-icon">{approval.budget_approved ? "✓" : "⏳"}</div>
                <div>
                  <div className="approval-title">وضعیت گزارش</div>
                  <div className="approval-value">{approval.budget_approved ? "تایید شده" : "در انتظار تایید"}</div>
                </div>
              </div>
            </div>
            <div className="approval-actions">
              {isAdmin && !approval.budget_approved && (
                <button className="btn btn-success approval-btn" onClick={() => doApproval("/approvals/budget", "POST")}>
                  تایید گزارش
                </button>
              )}
              {isSuperAdmin && approval.budget_approved && (
                <button className="btn btn-outline-secondary approval-btn" onClick={() => doApproval("/approvals/budget", "DELETE")}>
                  لغو تایید
                </button>
              )}
            </div>
          </div>
        </div>
      );
    }

    // double (salary)
    return (
      <div className="approval-panel">
        <div className="approval-header"><h6>وضعیت تایید گزارش</h6></div>
        <div className="approval-content">
          <div className="approval-statuses">
            <div className={`approval-card ${approval.budget_approved ? "approved" : "pending"}`}>
              <div className="approval-icon">{approval.budget_approved ? "✓" : "⏳"}</div>
              <div>
                <div className="approval-title">بودجه</div>
                <div className="approval-value">{approval.budget_approved ? "تایید شده" : "در انتظار تایید"}</div>
              </div>
            </div>
            <div className={`approval-card ${approval.actual_approved ? "approved" : "pending"}`}>
              <div className="approval-icon">{approval.actual_approved ? "✓" : "⏳"}</div>
              <div>
                <div className="approval-title">عملکرد</div>
                <div className="approval-value">{approval.actual_approved ? "تایید شده" : "در انتظار تایید"}</div>
              </div>
            </div>
          </div>
          <div className="approval-actions">
            {isAdmin && !approval.budget_approved && (
              <button className="btn btn-success approval-btn" onClick={() => doApproval("/approvals/budget", "POST")}>تایید بودجه</button>
            )}
            {isAdmin && !approval.actual_approved && (
              <button className="btn btn-primary approval-btn" onClick={() => doApproval("/approvals/actual", "POST")}>تایید عملکرد</button>
            )}
            {isSuperAdmin && approval.budget_approved && (
              <button className="btn btn-outline-secondary approval-btn" onClick={() => doApproval("/approvals/budget", "DELETE")}>لغو تایید بودجه</button>
            )}
            {isSuperAdmin && approval.actual_approved && (
              <button className="btn btn-outline-secondary approval-btn" onClick={() => doApproval("/approvals/actual", "DELETE")}>لغو تایید عملکرد</button>
            )}
          </div>
        </div>
      </div>
    );
  }

  // ---- render ----
  const visibleCompanies = currentUser?.role === "COMPANY_USER" ? currentUser.companies : companies;

  return (
    <MainLayout>
      <div className="page">
        <h2 className="text-center mb-4">{meta?.title}</h2>

        <div className="controls">
          <div className="controls-grid">
            <div className="field">
              <label>شرکت:</label>
              <select className="form-select" value={company} onChange={e => setCompany(e.target.value)}>
                {visibleCompanies.map(c => <option key={c} value={c}>{c}</option>)}
              </select>
            </div>
            <div className="field">
              <label>سال مالی:</label>
              <select className="form-select" value={year} onChange={e => setYear(e.target.value)}>
                {years.map(y => <option key={y} value={y}>{y}</option>)}
              </select>
            </div>
            <div className="field">
              <label>ماه گزارش:</label>
              <select className="form-select" value={month} onChange={e => setMonth(e.target.value)}>
                {months.map(m => <option key={m} value={m}>{m}</option>)}
              </select>
            </div>
          </div>
        </div>

        {renderApprovalPanel()}

        <div className="table-card">
          <div className="save-footer">
            {meta?.allow_add_rows && (
              <button className="btn btn-success" onClick={addRow} style={{ marginLeft: "10px" }}>+ افزودن ردیف</button>
            )}
            <button className="btn-save" onClick={saveRows} disabled={saving || isSaveLocked()}>
              {saving ? "در حال ذخیره..." : "ذخیره تغییرات"}
            </button>
          </div>

          <div className="table-responsive">
            <table className="table table-hover align-middle mb-0 cost-table">
              <thead>
                <tr>
                  {meta?.allow_add_rows && isAdmin && <th style={{ width: "40px" }}></th>}
                  {meta?.columns?.map(col => <th key={col.field}>{col.title}</th>)}
                </tr>
                {/* ردیف جمع ستون‌ها */}
                <tr className="col-sum-row">
                  {meta?.allow_add_rows && isAdmin && <td></td>}
                  {meta?.columns?.map(col => (
                    <td key={col.field} style={{ padding: "2px 6px" }}>
                      {col.type === "number" ? (
                        <div>
                          <button
                            className="btn btn-link btn-sm p-0 col-sum-btn"
                            onClick={() => toggleSum(col.field)}
                            title="نمایش جمع ستون"
                          >
                            Σ
                          </button>
                          {visibleSums[col.field] && (
                            <span className="col-sum-value">
                              {Math.round(calcColSum(col.field)).toLocaleString("en-US")}
                            </span>
                          )}
                        </div>
                      ) : null}
                    </td>
                  ))}
                </tr>
              </thead>
              <tbody>
                {loading && <tr><td colSpan={(meta?.columns?.length || 10) + 1}>در حال دریافت...</td></tr>}
                {!loading && rows.length === 0 && <tr><td colSpan={(meta?.columns?.length || 10) + 1}>داده‌ای وجود ندارد</td></tr>}
                {!loading && rows.map((row, index) => (
                  <tr key={row.id ?? row.tempId ?? index}>
                    {meta?.allow_add_rows && isAdmin && (
                      <td>
                        <button
                          className="btn btn-sm btn-outline-danger"
                          onClick={() => deleteRow(index)}
                          disabled={isSaveLocked()}
                          title="حذف ردیف"
                        >×</button>
                      </td>
                    )}
                    {meta?.columns?.map(col => (
                      <td key={col.field}>
                        {col.editable ? (
                          col.type === "number" ? (
                            <NumericCell
                              value={row.values?.[col.field]}
                              disabled={isFieldLocked(col.field)}
                              onChange={val => updateCell(index, col.field, val)}
                            />
                          ) : (
                            <input
                              className="form-control"
                              type="text"
                              disabled={isFieldLocked(col.field)}
                              value={row.values?.[col.field] ?? ""}
                              onChange={e => updateCell(index, col.field, e.target.value)}
                            />
                          )
                        ) : (
                          row.values?.[col.field] ?? "-"
                        )}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="save-footer">
            <button className="btn-save" onClick={saveRows} disabled={saving || isSaveLocked()}>
              {saving ? "در حال ذخیره..." : "ذخیره تغییرات"}
            </button>
          </div>
        </div>
      </div>
    </MainLayout>
  );
}