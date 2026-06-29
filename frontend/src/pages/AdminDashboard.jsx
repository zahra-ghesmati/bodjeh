import { useEffect, useState } from "react";
import MainLayout from "../layouts/MainLayout";
import { apiFetch } from "../services/api";
import { Link } from "react-router-dom";
export default function AdminDashboard() {



 const [selectedYear] =
  useState("1404-1405");

const [selectedMonth] =
  useState("ارديبهشت");   
  const [rows, setRows] = useState([]);

  useEffect(() => {

    loadData();

  }, []);

async function loadData() {

  try {

const response =
  await apiFetch(
    `/dashboard/admin?year=${selectedYear}&month=${selectedMonth}`
  );

    console.log("status", response.status);

    const data =
      await response.json();

    console.log("data", data);

    setRows(data);

  } catch (e) {

    console.error("ERROR", e);

  }

}

const totals = {

  budgetNotStarted: 0,
  budgetIncomplete: 0,
  budgetCompleted: 0,
  budgetClosed: 0,

  actualNotStarted: 0,
  actualIncomplete: 0,
  actualCompleted: 0,
  actualClosed: 0

};

rows.forEach(row => {

  totals.budgetNotStarted +=
    row.budget.not_started;

  totals.budgetIncomplete +=
    row.budget.incomplete;

  totals.budgetCompleted +=
    row.budget.completed;

  totals.budgetClosed +=
    row.budget.closed;

  totals.actualNotStarted +=
    row.actual.not_started;

  totals.actualIncomplete +=
    row.actual.incomplete;

  totals.actualCompleted +=
    row.actual.completed;

  totals.actualClosed +=
    row.actual.closed;

});
  return (

  <MainLayout>

    <div className="page">

        <div
        style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: "20px"
        }}
        >

        <h2 className="page-title">
            داشبورد مدیریتی
        </h2>

        <div
            style={{
            fontWeight: "bold"
            }}
        >
            ماه: {selectedMonth}
            {" | "}
            سال مالی:
            <span dir="ltr">
            {" "}
            {selectedYear}
            </span>
        </div>

        </div>
      <div className="dashboard-stats">

        <div className="stat-card gray">
          <div className="stat-value">
            {totals.budgetNotStarted}
          </div>
          <div className="stat-title">
            بودجه ثبت نشده
          </div>
        </div>

        <div className="stat-card orange">
          <div className="stat-value">
            {totals.budgetIncomplete}
          </div>
          <div className="stat-title">
            بودجه ناقص
          </div>
        </div>

        <div className="stat-card blue">
          <div className="stat-value">
            {totals.budgetCompleted}
          </div>
          <div className="stat-title">
            بودجه تکمیل
          </div>
        </div>

        <div className="stat-card green">
          <div className="stat-value">
            {totals.budgetClosed}
          </div>
          <div className="stat-title">
            بودجه بسته
          </div>
        </div>

      </div>

      <div className="dashboard-stats">

        <div className="stat-card gray">
          <div className="stat-value">
            {totals.actualNotStarted}
          </div>
          <div className="stat-title">
            عملکرد ثبت نشده
          </div>
        </div>

        <div className="stat-card orange">
          <div className="stat-value">
            {totals.actualIncomplete}
          </div>
          <div className="stat-title">
            عملکرد ناقص
          </div>
        </div>

        <div className="stat-card blue">
          <div className="stat-value">
            {totals.actualCompleted}
          </div>
          <div className="stat-title">
            عملکرد تکمیل
          </div>
        </div>

        <div className="stat-card green">
          <div className="stat-value">
            {totals.actualClosed}
          </div>
          <div className="stat-title">
            عملکرد بسته
          </div>
        </div>

      </div>

      <div className="table-card">

        <table className="table table-hover">

          <thead>

            <tr>

              <th>
                شرکت
              </th>

              <th>
                درصد پیشرفت
              </th>

              <th>
                بودجه
              </th>

              <th>
                عملکرد
              </th>

            </tr>

          </thead>

          <tbody>

            {rows.map(row => (

              <tr key={row.company}>

                <td>

  <Link
    to={`/dashboard?company=${encodeURIComponent(
      row.company
    )}&year=${encodeURIComponent(
      selectedYear
    )}&month=${encodeURIComponent(
      selectedMonth
    )}`}
  >
    {row.company}
  </Link>

</td>

                <td>

                  <div
                    className="progress"
                  >

                    <div
                      className="progress-bar"
                      style={{
                        width:
                          `${row.progress}%`
                      }}
                    >
                      {row.progress}%
                    </div>

                  </div>

                </td>

                    <td>

                    🟢 بسته: {row.budget.closed}

                    <br />

                    🔵 تکمیل: {row.budget.completed}

                    <br />

                    🟠 ناقص: {row.budget.incomplete}

                    </td>

                    <td>

                    🟢 بسته: {row.actual.closed}

                    <br />

                    🔵 تکمیل: {row.actual.completed}

                    <br />

                    🟠 ناقص: {row.actual.incomplete}

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