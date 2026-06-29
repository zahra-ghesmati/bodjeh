import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { apiFetch } from "../services/api";

export default function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");

    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);

    try {
      const response = await fetch(
        (import.meta.env.VITE_API_URL ?? "") + "/login",
        { method: "POST", body: formData }
      );

      if (!response.ok) {
        setError("نام کاربری یا رمز عبور اشتباه است");
        return;
      }

      const data = await response.json();
      localStorage.setItem("access_token", data.access_token);

      const meResponse = await apiFetch("/me");
      if (!meResponse.ok) throw new Error("Failed to load user");

      const user = await meResponse.json();

      if (user.role === "ADMIN" || user.role === "ADMINISTRATOR") {
        navigate("/admin-dashboard");
      } else {
        navigate("/dashboard");
      }

    } catch {
      setError("خطا در ارتباط با سرور");
    }
  }

  return (
    <div className="container">
      <div className="card shadow mx-auto mt-5" style={{ maxWidth: "450px" }}>
        <div className="card-body p-4">
          <h3 className="text-center mb-4">ورود به سیستم</h3>

          {error && <div className="alert alert-danger">{error}</div>}

          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">نام کاربری</label>
              <input
                type="text"
                className="form-control"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>

            <div className="mb-3">
              <label className="form-label">رمز عبور</label>
              <input
                type="password"
                className="form-control"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>

            <button type="submit" className="btn btn-primary w-100">
              ورود
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
