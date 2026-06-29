import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./MainLayout.css";

const API_URL = import.meta.env.VITE_API_URL ?? "";

export default function MainLayout({ children }) {
  const [user, setUser] = useState(null);
  const [formGroups, setFormGroups] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      window.location.href = "/login";
      return;
    }

    fetch(API_URL + "/me", {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(res => {
        if (!res.ok) throw new Error();
        return res.json();
      })
      .then(data => {
        setUser(data);
        return fetch(API_URL + "/forms/menu", {
          headers: { Authorization: `Bearer ${token}` }
        });
      })
      .then(res => res.json())
      .then(menu => setFormGroups(menu))
      .catch(() => {
        localStorage.removeItem("access_token");
        window.location.href = "/login";
      });
  }, []);

  function logout() {
    localStorage.removeItem("access_token");
    window.location.href = "/login";
  }

  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <Link
            className="navbar-brand"
            to={user?.role === "ADMIN" || user?.role === "ADMINISTRATOR" ? "/admin-dashboard" : "/dashboard"}
          >
            گزارشات
          </Link>

          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span className="navbar-toggler-icon" />
          </button>

          <div className="collapse navbar-collapse justify-content-between" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link
                  className="nav-link"
                  to={user?.role === "ADMIN" || user?.role === "ADMINISTRATOR" ? "/admin-dashboard" : "/dashboard"}
                >
                  داشبورد
                </Link>
              </li>

              {formGroups.map(group => (
                <li key={group.group} className="nav-item dropdown">
                  <a href="#" className="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown">
                    {group.group}
                  </a>
                  <ul className="dropdown-menu">
                    {group.items.map(item => (
                      <li key={item.key}>
                        <Link className="dropdown-item" to={`/forms/${item.key}`}>
                          {item.title}
                        </Link>
                      </li>
                    ))}
                  </ul>
                </li>
              ))}

              {user?.role === "ADMINISTRATOR" && (
                <li className="nav-item dropdown">
                  <a href="#" className="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown">
                    مدیریت سیستم
                  </a>
                  <ul className="dropdown-menu">
                    <li><Link className="dropdown-item" to="/users">مدیریت کاربران</Link></li>
                    <li><Link className="dropdown-item" to="/months">مدیریت سال مالی</Link></li>
                  </ul>
                </li>
              )}
            </ul>

            <button className="btn btn-outline-light" onClick={logout}>خروج</button>
          </div>
        </div>
      </nav>

      <div className="main-content">{children}</div>
    </>
  );
}
