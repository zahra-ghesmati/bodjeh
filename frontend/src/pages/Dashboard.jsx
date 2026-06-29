import { useEffect, useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { apiFetch } from "../services/api";
import "../components/GenericForm.css";
import "./Dashboard.css";
import {
  Link,
  useSearchParams
} from "react-router-dom";

export default function Dashboard() {
const [searchParams] =
    useSearchParams();
  const companies = [
    "سيمان مازندران",
    "گروه صنايع سيمان کرمان",
    "بين المللي ساروج بوشهر",
    "سيمان شمال",
    "توليدي سيمان فيروزکوه"
  ];

  const months = [
    "فروردين",
    "ارديبهشت",
    "خرداد",
    "تير",
    "مرداد",
    "شهريور",
    "مهر",
    "آبان",
    "آذر",
    "دي",
    "بهمن",
    "اسفند"
  ];
const [search, setSearch] = useState("");



const [
  budgetFilter,
  setBudgetFilter
] = useState("all");

const [
  actualFilter,
  setActualFilter
] = useState("all");
  const [years, setYears] = useState([]);
  const [rows, setRows] = useState([]);

  const [currentUser, setCurrentUser] =
    useState(null);

  const [selectedCompany, setSelectedCompany] =
    useState("");

  const [selectedYear, setSelectedYear] =
    useState("");

  const [selectedMonth, setSelectedMonth] =
    useState("");

  const visibleCompanies =
    currentUser?.role === "COMPANY_USER"
      ? currentUser.companies
      : companies;
useEffect(() => {

  const company =
    searchParams.get("company");

  const year =
    searchParams.get("year");

  const month =
    searchParams.get("month");

  if (company) {
    setSelectedCompany(company);
  }

  if (year) {
    setSelectedYear(year);
  }

  if (month) {
    setSelectedMonth(month);
  }

}, [searchParams]);
  useEffect(() => {

    loadCurrentUser();
    loadYears();

  }, []);

  useEffect(() => {

    if (
      selectedCompany &&
      selectedYear &&
      selectedMonth
    ) {
      loadDashboard();
    }

  }, [
    selectedCompany,
    selectedYear,
    selectedMonth
  ]);

  async function loadCurrentUser() {

    try {

      const response =
        await apiFetch("/me");

      const data =
        await response.json();

      setCurrentUser(data);

      const companyFromUrl =
        searchParams.get("company");

      if (companyFromUrl) {

        setSelectedCompany(
          companyFromUrl
        );

      } else if (
        data.role === "COMPANY_USER" &&
        data.companies.length > 0
      ) {

        setSelectedCompany(
          data.companies[0]
        );

      } else {

        setSelectedCompany(
          companies[0]
        );

      }

    } catch (error) {

      console.error(error);

    }
  }

  async function loadYears() {

    try {

      const response =
        await apiFetch(
          "/api/months/years"
        );

      const data =
        await response.json();

      setYears(data);

const yearFromUrl =
  searchParams.get("year");

const monthFromUrl =
  searchParams.get("month");

if (yearFromUrl) {

  setSelectedYear(
    yearFromUrl
  );

} else if (data.length > 0) {

  setSelectedYear(
    data[0]
  );

}

setSelectedMonth(
  monthFromUrl ||
  "فروردين"
);
       

    } catch (error) {

      console.error(error);

    }
  }

async function loadDashboard() {

  try {

    const response =
      await apiFetch(
        `/dashboard/status?company=${encodeURIComponent(
          selectedCompany
        )}&year=${encodeURIComponent(
          selectedYear
        )}&month=${encodeURIComponent(
          selectedMonth
        )}`
      );

    const data =
      await response.json();

    console.log("dashboard data:", data);

    setRows(data);

  } catch (error) {

    console.error(error);

  }

}
function getStatusIcon(status){

  switch(status){

    case "completed":
      return "✓";

    case "closed":
      return "🔒";

    case "incomplete":
      return "⚠";

    default:
      return "○";
  }

}
  function getStatusText(status) {

    switch (status) {

      case "not_started":
        return "ثبت نشده";

      case "incomplete":
        return "ناقص";

      case "completed":
        return "تکمیل شده";

      case "closed":
        return "بسته شده";

      default:
        return "-";
    }
  }

  function getStatusClass(status) {

    switch (status) {

      case "not_started":
        return "status-gray";

      case "incomplete":
        return "status-orange";

      case "completed":
        return "status-blue";

      case "closed":
        return "status-green";

      default:
        return "";
    }
  }
const filteredRows =
  rows
    .filter(row => {

      if (
        search.trim() &&
        !row.title.includes(
          search.trim()
        )
      ) {
        return false;
      }

      if (
  budgetFilter !== "all" &&
  row.budget_status !== budgetFilter
) {
  return false;
}

if (
  actualFilter !== "all" &&
  row.actual_status !== actualFilter
) {
  return false;
}

      return true;

    });
const budgetStats = {
  not_started: 0,
  incomplete: 0,
  completed: 0,
  closed: 0
};

const actualStats = {
  not_started: 0,
  incomplete: 0,
  completed: 0,
  closed: 0
};
const totalForms = rows.length;
rows.forEach(row => {

  if (
    budgetStats[row.budget_status] !== undefined
  ) {
    budgetStats[row.budget_status]++;
  }

  if (
    actualStats[row.actual_status] !== undefined
  ) {
    actualStats[row.actual_status]++;
  }

});
  return (
    <MainLayout>

      <div className="page">

        <h2 className="page-title">
  داشبورد وضعیت فرم‌ها
  <small
    style={{
      fontSize: "14px",
      marginRight: "10px",
      color: "#888"
    }}
  >
    ({totalForms} فرم)
  </small>
</h2>

        <div className="controls">

          <div className="controls-grid">

            <div>

              <label>
                شرکت
              </label>

              <select
                className="form-select"
                value={selectedCompany}
                onChange={(e) =>
                  setSelectedCompany(
                    e.target.value
                  )
                }
              >
                {visibleCompanies.map(c => (
                  <option
                    key={c}
                    value={c}
                  >
                    {c}
                  </option>
                ))}
              </select>

            </div>

            <div>

              <label>
                سال مالی
              </label>

              <select
                className="form-select"
                value={selectedYear}
                onChange={(e) =>
                  setSelectedYear(
                    e.target.value
                  )
                }
              >
                {years.map(y => (
                  <option
                    key={y}
                    value={y}
                  >
                    {y}
                  </option>
                ))}
              </select>

            </div>

            <div>

              <label>
                ماه
              </label>

              <select
                className="form-select"
                value={selectedMonth}
                onChange={(e) =>
                  setSelectedMonth(
                    e.target.value
                  )
                }
              >
                {months.map(m => (
                  <option
                    key={m}
                    value={m}
                  >
                    {m}
                  </option>
                ))}
              </select>

            </div>

          </div>

        </div>


<div className="dashboard-section">



  <div className="dashboard-stats">

    <div
      className="stat-card gray"
      onClick={() => {
        setBudgetFilter("not_started");
        setActualFilter("all");
      }}
    >
      <div className="stat-value">
        {budgetStats.not_started}
      </div>

      <div className="stat-title">
         بودجه ثبت نشده
      </div>
    </div>

    <div
      className="stat-card orange"
      onClick={() => {
        setBudgetFilter("incomplete");
        setActualFilter("all");
      }}
    >
      <div className="stat-value">
        {budgetStats.incomplete}
      </div>

      <div className="stat-title">
         بودجه ناقص
      </div>
    </div>

    <div
      className="stat-card blue"
      onClick={() => {
        setBudgetFilter("completed");
        setActualFilter("all");
      }}
    >
      <div className="stat-value">
        {budgetStats.completed}
      </div>

      <div className="stat-title">
          بودجه تکمیل شده
      </div>
    </div>

    <div
      className="stat-card green"
      onClick={() => {
        setBudgetFilter("closed");
        setActualFilter("all");
      }}
    >
      <div className="stat-value">
        {budgetStats.closed}
      </div>

      <div className="stat-title">
        بودجه بسته شده
      </div>
    </div>

  </div>

</div>

<div className="dashboard-section">


  <div className="dashboard-stats">

    <div
      className="stat-card gray"
      onClick={() => {
        setActualFilter("not_started");
        setBudgetFilter("all");
      }}
    >
      <div className="stat-value">
        {actualStats.not_started}
      </div>

      <div className="stat-title">
      عملکرد ثبت نشده
      </div>
    </div>

    <div
      className="stat-card orange"
      onClick={() => {
        setActualFilter("incomplete");
        setBudgetFilter("all");
      }}
    >
      <div className="stat-value">
        {actualStats.incomplete}
      </div>

      <div className="stat-title">
        عملکرد ناقص
      </div>
    </div>

    <div
      className="stat-card blue"
      onClick={() => {
        setActualFilter("completed");
        setBudgetFilter("all");
      }}
    >
      <div className="stat-value">
        {actualStats.completed}
      </div>

      <div className="stat-title">
        عملکرد تکمیل شده
      </div>
    </div>

    <div
      className="stat-card green"
      onClick={() => {
        setActualFilter("closed");
        setBudgetFilter("all");
      }}
    >
      <div className="stat-value">
        {actualStats.closed}
      </div>

      <div className="stat-title">
        عملکرد بسته شده
      </div>
    </div>

  </div>

</div>
        <div className="table-card">
<div className="dashboard-tools">

  <div className="search-box">
    <input
      type="text"
      className="form-control"
      placeholder="جستجوی نام فرم..."
      value={search}
      onChange={(e) =>
        setSearch(e.target.value)
      }
    />
  </div>

  <div className="filters-box">

    <select
  className="form-select"
  value={budgetFilter}
  onChange={(e) =>
    setBudgetFilter(e.target.value)
  }
>
      <option value="all">
         وضعیت‌های بودجه
      </option>

      <option value="not_started">
        ثبت نشده
      </option>

      <option value="incomplete">
        ناقص
      </option>

      <option value="completed">
        تکمیل شده
      </option>

      <option value="closed">
        بسته شده
      </option>

    </select>

    <select
  className="form-select"
  value={actualFilter}
  onChange={(e) =>
    setActualFilter(e.target.value)
  }
>
<option value="all">
         وضعیت‌های عملکرد
      </option>

      <option value="not_started">
        ثبت نشده
      </option>

      <option value="incomplete">
        ناقص
      </option>

      <option value="completed">
        تکمیل شده
      </option>

      <option value="closed">
        بسته شده
      </option>

    </select>

  </div>

</div>
          <table className="table table-hover align-middle mb-0 dashboard-table">

            <thead>

              <tr>

                <th>
                  فرم
                </th>

                <th>
                  بودجه
                </th>

                <th>
                  عملکرد
                </th>
                <th>عملیات</th>

              </tr>

            </thead>

            <tbody>
{filteredRows.length === 0 && (
  <tr>
    <td colSpan="4">
      هیچ فرمی با فیلترهای انتخاب شده یافت نشد
    </td>
  </tr>
)}
              {filteredRows.map(row => (

                <tr
                  key={row.form_key}
                  className={
                      row.budget_status === "closed" &&
                      row.actual_status === "closed"
                        ? "row-closed"
                        : ""
                    }
                >

                  <td>
                    <Link
                      className="form-link"
                      to={`/forms/${row.form_key}?company=${encodeURIComponent(
                        selectedCompany
                      )}&year=${encodeURIComponent(
                        selectedYear
                      )}&month=${encodeURIComponent(
                        selectedMonth
                      )}`}
                    >
                      {row.title}
                    </Link>

                  </td>

                  <td>

                    <span
                      className={`status-badge ${getStatusClass(
                        row.budget_status
                      )}`}
                    >
                      <span className="status-dot"></span>
                      
                      {getStatusText(row.budget_status)}
                    </span>

                  </td>

                  <td>

                    <span
                      className={`status-badge ${getStatusClass(
                        row.actual_status
                      )}`}
                    >
                      <span className="status-dot"></span>
                      
                      {getStatusText(
                        row.actual_status
                      )}
                    </span>

                  </td>
                  <td>

                    <Link
                      to={`/forms/${row.form_key}?company=${encodeURIComponent(
                        selectedCompany
                      )}&year=${encodeURIComponent(
                        selectedYear
                      )}&month=${encodeURIComponent(
                        selectedMonth
                      )}`}
                      className="btn-open-form"
                    >
                      ورود
                    </Link>
                    
                  </td>
                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

    </MainLayout>
  );
}