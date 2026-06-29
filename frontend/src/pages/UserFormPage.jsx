import { useEffect, useState } from "react";
import {
  useNavigate,
  useParams
} from "react-router-dom";

import MainLayout from "../layouts/MainLayout";
import { apiFetch } from "../services/api";

export default function UserFormPage() {

  const navigate = useNavigate();
  const { id } = useParams();
const [currentUser, setCurrentUser] =
  useState(null);
  const isEdit =
    Boolean(id);

  const [loading, setLoading] =
    useState(false);

  const [saving, setSaving] =
    useState(false);

  const [roles, setRoles] =
    useState([]);

  const [companies, setCompanies] =
    useState([]);

  const [form, setForm] =
    useState({
      username: "",
      full_name: "",
      password: "",
      role_id: "",
      company_name: "",
      is_active: true
    });

useEffect(() => {

  checkAccess();

}, []);

async function checkAccess() {

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

    await loadMeta();

    if (isEdit) {

      await loadUser();

    }

  } catch (error) {

    console.error(error);

    navigate("/");

  }

}

  async function loadMeta() {

    try {

      const rolesResponse =
        await apiFetch(
          "/api/users/meta/roles"
        );

      const rolesData =
        await rolesResponse.json();

      setRoles(rolesData);

      const companiesResponse =
        await apiFetch(
          "/api/users/meta/companies"
        );

      const companiesData =
        await companiesResponse.json();

      setCompanies(companiesData);

    } catch (error) {

      console.error(error);

    }

  }

  async function loadUser() {

    try {

      setLoading(true);

      const response =
        await apiFetch(
          `/api/users/${id}`
        );

      const data =
        await response.json();

      setForm({
        username:
          data.username || "",

        full_name:
          data.full_name || "",

        password: "",

        role_id:
          data.role_id || "",

        company_name:
          data.company_name || "",

        is_active:
          data.is_active
      });

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }

  }

  function updateField(
    key,
    value
  ) {

    setForm(prev => ({
      ...prev,
      [key]: value
    }));

  }

  async function saveUser() {

    try {

      setSaving(true);

      const payload = {
        ...form
      };

      const response =
        await apiFetch(

          isEdit
            ? `/api/users/${id}`
            : "/api/users",

          {
            method:
              isEdit
                ? "PUT"
                : "POST",

            headers: {
              "Content-Type":
                "application/json"
            },

            body:
              JSON.stringify(
                payload
              )
          }

        );

      const data =
        await response.json();

      if (!response.ok) {

        alert(
          data.detail ||
          "خطا در ذخیره"
        );

        return;

      }

      alert(
        "اطلاعات ذخیره شد"
      );

      navigate("/users");

    } catch (error) {

      console.error(error);

      alert(
        "خطای شبکه"
      );

    } finally {

      setSaving(false);

    }

  }

  const selectedRole =
    roles.find(
      r =>
        Number(r.id) ===
        Number(form.role_id)
    );

  const showCompany =
    selectedRole?.name ===
    "COMPANY_USER";

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

          {
            isEdit
              ? "ویرایش کاربر"
              : "ایجاد کاربر جدید"
          }

        </h2>

        <div className="table-card">

          {loading ? (

            <div className="p-4 text-center">
              در حال بارگذاری...
            </div>

          ) : (

            <div
              className="p-4"
            >

              <div className="row g-3">

                <div className="col-md-6">

                  <label className="form-label">
                    نام کاربری
                  </label>

                  <input
                    className="form-control"
                    value={
                      form.username
                    }
                    onChange={e =>
                      updateField(
                        "username",
                        e.target.value
                      )
                    }
                  />

                </div>

                <div className="col-md-6">

                  <label className="form-label">
                    نام کامل
                  </label>

                  <input
                    className="form-control"
                    value={
                      form.full_name
                    }
                    onChange={e =>
                      updateField(
                        "full_name",
                        e.target.value
                      )
                    }
                  />

                </div>

                <div className="col-md-6">

                  <label className="form-label">

                    {
                      isEdit
                        ? "رمز عبور جدید (اختیاری)"
                        : "رمز عبور"
                    }

                  </label>

                  <input
                    type="password"
                    className="form-control"
                    value={
                      form.password
                    }
                    onChange={e =>
                      updateField(
                        "password",
                        e.target.value
                      )
                    }
                  />

                </div>

                <div className="col-md-6">

                  <label className="form-label">
                    نقش
                  </label>

                  <select
                    className="form-select"
                    value={
                      form.role_id
                    }
                    onChange={e =>
                      updateField(
                        "role_id",
                        e.target.value
                      )
                    }
                  >

                    <option value="">
                      انتخاب کنید
                    </option>

                    {roles.map(
                      role => (

                      <option
                        key={role.id}
                        value={role.id}
                      >
                        {role.name}
                      </option>

                    ))}

                  </select>

                </div>

                {showCompany && (

                  <div className="col-md-6">

                    <label className="form-label">
                      شرکت
                    </label>

                    <select
                      className="form-select"
                      value={
                        form.company_name
                      }
                      onChange={e =>
                        updateField(
                          "company_name",
                          e.target.value
                        )
                      }
                    >

                      <option value="">
                        انتخاب شرکت
                      </option>

                      {companies.map(
                        company => (

                        <option
                          key={company}
                          value={company}
                        >
                          {company}
                        </option>

                      ))}

                    </select>

                  </div>

                )}

                <div className="col-md-6">

                  <label className="form-label">
                    وضعیت
                  </label>

                  <select
                    className="form-select"
                    value={
                      form.is_active
                        ? "1"
                        : "0"
                    }
                    onChange={e =>
                      updateField(
                        "is_active",
                        e.target.value ===
                          "1"
                      )
                    }
                  >

                    <option value="1">
                      فعال
                    </option>

                    <option value="0">
                      غیرفعال
                    </option>

                  </select>

                </div>

              </div>

              <div
                className="mt-4 d-flex gap-2"
              >

                <button
                  className="btn-save"
                  onClick={
                    saveUser
                  }
                  disabled={
                    saving
                  }
                >

                  {
                    saving
                      ? "در حال ذخیره..."
                      : "ذخیره"
                  }

                </button>

                <button
                  className="btn btn-secondary"
                  onClick={() =>
                    navigate(
                      "/users"
                    )
                  }
                >
                  بازگشت
                </button>

              </div>

            </div>

          )}

        </div>

      </div>

    </MainLayout>

  );

}