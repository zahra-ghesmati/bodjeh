import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";
import { apiFetch } from "../services/api";

export default function UsersPage() {

  const navigate = useNavigate();
  
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [currentUser, setCurrentUser] =useState(null);
useEffect(() => {

  loadCurrentUser();

}, []);
async function loadCurrentUser() {

  try {

    const response =
      await apiFetch("/me");

    const user =
      await response.json();

    if (
      user.role !==
      "ADMINISTRATOR"
    ) {

      navigate("/");

      return;

    }

    setCurrentUser(user);

    loadUsers();

  } catch (error) {

    console.error(error);

    navigate("/");

  }

}
  async function loadUsers() {

    try {

      setLoading(true);

      const response =
        await apiFetch("/api/users");

      if (!response.ok) {

        console.error(
          "Users API Error:",
          response.status
        );

        setUsers([]);
        return;

      }

      const data =
        await response.json();

      console.log("users:", data);

      setUsers(
        Array.isArray(data)
          ? data
          : []
      );

    } catch (error) {

      console.error(error);
      setUsers([]);

    } finally {

      setLoading(false);

    }

  }
if (!currentUser) {

  return (
    <MainLayout>
      <div className="page">
        در حال بارگذاری...
      </div>
    </MainLayout>
  );

}
  return (
    <MainLayout>

      <div className="page">

        <h2 className="text-center mb-4">
          مدیریت کاربران
        </h2>

        <div className="controls">

          <div className="d-flex justify-content-between align-items-center">

            <div>
              تعداد کاربران:
              {" "}
              <strong>
                {users.length}
              </strong>
            </div>

            <button
              className="btn btn-primary"
              onClick={() =>
                navigate("/users/new")
              }
            >
              + افزودن کاربر
            </button>

          </div>

        </div>

        <div className="table-card">

          <div className="table-responsive">

            <table className="table table-hover align-middle mb-0 cost-table">

              <thead>

                <tr>

                  <th>نام کاربری</th>
                  <th>نام کامل</th>
                  <th>نقش</th>
                  <th>شرکت</th>
                  <th>وضعیت</th>
                  <th>عملیات</th>

                </tr>

              </thead>

              <tbody>

                {loading && (

                  <tr>
                    <td
                      colSpan="6"
                      className="text-center"
                    >
                      در حال بارگذاری...
                    </td>
                  </tr>

                )}

                {!loading &&
                  users.length === 0 && (

                  <tr>
                    <td
                      colSpan="6"
                      className="text-center"
                    >
                      کاربری یافت نشد
                    </td>
                  </tr>

                )}

                {!loading &&
                  users.map((user) => (

                  <tr key={user.id}>

                    <td>{user.username}</td>

                    <td>{user.full_name}</td>

                    <td>{user.role}</td>

                    <td>
                      {user.company_name || "-"}
                    </td>

                    <td>

                      <span
                        className={
                          user.is_active
                            ? "badge bg-success"
                            : "badge bg-danger"
                        }
                      >
                        {
                          user.is_active
                            ? "فعال"
                            : "غیرفعال"
                        }
                      </span>

                    </td>

                    <td>

                      <button
                        className="btn btn-outline-primary btn-sm"
                        onClick={() =>
                          navigate(
                            `/users/edit/${user.id}`
                          )
                        }
                      >
                        ویرایش
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