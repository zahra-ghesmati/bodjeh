import { useEffect, useState } from "react";

import MainLayout from "../layouts/MainLayout";
import { apiFetch } from "../services/api";

export default function MonthsPage() {

  const [years, setYears] =
    useState([]);

  const [loading, setLoading] =
    useState(false);

  const [newYear, setNewYear] =
    useState("");

  useEffect(() => {

    loadYears();

  }, []);

  async function loadYears() {

    try {

      setLoading(true);

      const response =
        await apiFetch(
          "/api/months/years"
        );

      const data =
        await response.json();

      setYears(
        Array.isArray(data)
          ? data
          : []
      );

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }

  }

  async function createYear() {

    if (!newYear.trim()) {

      alert(
        "سال مالی را وارد کنید"
      );

      return;

    }

    try {

      const response =
        await apiFetch(
          `/api/months/${newYear}`,
          {
            method: "POST"
          }
        );

      const data =
        await response.json();

      if (!response.ok) {

        alert(
          data.detail ||
          "خطا در ایجاد سال"
        );

        return;

      }

      alert(
        "سال مالی ایجاد شد"
      );

      setNewYear("");

      loadYears();

    } catch (error) {

      console.error(error);

      alert(
        "خطای شبکه"
      );

    }

  }

  async function deleteYear(
    year
  ) {

    const confirmed =
      window.confirm(
        `سال ${year} حذف شود؟`
      );

    if (!confirmed) {

      return;

    }

    try {

      const response =
        await apiFetch(
          `/api/months/${year}`,
          {
            method: "DELETE"
          }
        );

      const data =
        await response.json();

      if (!response.ok) {

        alert(
          data.detail ||
          "خطا در حذف سال"
        );

        return;

      }

      alert(
        "سال حذف شد"
      );

      loadYears();

    } catch (error) {

      console.error(error);

      alert(
        "خطای شبکه"
      );

    }

  }

  return (

    <MainLayout>

      <div className="page">

        <h2 className="text-center mb-4">
          مدیریت سال‌های مالی
        </h2>

        <div className="table-card p-4 mb-4">

          <div className="row g-3 align-items-end">

            <div className="col-md-4">

              <label className="form-label">
                سال مالی
              </label>

              <input
                className="form-control"
                placeholder="1405-1406"
                value={newYear}
                onChange={(e) =>
                  setNewYear(
                    e.target.value
                  )
                }
              />

            </div>

            <div className="col-md-2">

              <button
                className="btn btn-primary w-100"
                onClick={
                  createYear
                }
              >
                ایجاد
              </button>

            </div>

          </div>

        </div>

        <div className="table-card">

          <div className="table-responsive">

            <table className="table table-hover align-middle mb-0">

              <thead>

                <tr>

                  <th>
                    سال مالی
                  </th>

                  <th>
                    عملیات
                  </th>

                </tr>

              </thead>

              <tbody>

                {loading && (

                  <tr>

                    <td
                      colSpan="2"
                      className="text-center"
                    >
                      در حال بارگذاری...
                    </td>

                  </tr>

                )}

                {!loading &&
                  years.length === 0 && (

                  <tr>

                    <td
                      colSpan="2"
                      className="text-center"
                    >
                      اطلاعاتی یافت نشد
                    </td>

                  </tr>

                )}

                {!loading &&
                  years.map(
                    (year) => (

                    <tr
                      key={year}
                    >

                      <td>
                        {year}
                      </td>

                      <td>

                        <button
                          className="btn btn-danger btn-sm"
                          onClick={() =>
                            deleteYear(
                              year
                            )
                          }
                        >
                          حذف
                        </button>

                      </td>

                    </tr>

                  ))}

              </tbody>

            </table>

          </div>

        </div>

      </div>

    </MainLayout>

  );

}