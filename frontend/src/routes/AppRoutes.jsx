import { BrowserRouter, Routes, Route, useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import ProtectedRoute from "./ProtectedRoute";
import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import UsersPage from "../pages/UsersPage";
import UserFormPage from "../pages/UserFormPage";
import MonthsPage from "../pages/MonthsPage";
import GenericFormPage from "../pages/GenericFormPage";
import AdminDashboard from "../pages/AdminDashboard";
import DynamicDataFormPage from "../pages/DynamicDataFormPage";
import CashFlowForm from "../components/CashFlowForm";

const API_URL = import.meta.env.VITE_API_URL ?? "";

function FormController() {
  const { formKey } = useParams();
  const [formType, setFormType] = useState(null);

  useEffect(() => {
    if (formKey === "cash_flow") {
      setFormType("cash_flow");
      return;
    }

    setFormType(null);

    async function fetchFormType() {
      try {
        const token = localStorage.getItem("access_token");
        const res = await fetch(`${API_URL}/forms/${formKey}/meta`, {
          headers: { Authorization: `Bearer ${token}` }
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();
        setFormType(data.type);
      } catch (err) {
        console.error("Error fetching form config:", err);
      }
    }

    if (formKey) fetchFormType();
  }, [formKey]);

  if (!formType) return <div>Loading...</div>;
  if (formType === "cash_flow") return <CashFlowForm />;
  if (formType === "dynamic") return <DynamicDataFormPage formKey={formKey} />;
  return <GenericFormPage formKey={formKey} />;
}

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
        <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
        <Route path="/admin-dashboard" element={<AdminDashboard />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/forms/:formKey"
          element={<ProtectedRoute><FormController /></ProtectedRoute>}
        />
        <Route path="/cash-flow" element={<ProtectedRoute><CashFlowForm /></ProtectedRoute>} />
        <Route path="/users" element={<UsersPage />} />
        <Route path="/users/new" element={<UserFormPage />} />
        <Route path="/users/edit/:id" element={<UserFormPage />} />
        <Route path="/months" element={<MonthsPage />} />
      </Routes>
    </BrowserRouter>
  );
}