const API_URL = import.meta.env.VITE_API_URL ?? "";

export async function apiFetch(url, options = {}) {
  const token = localStorage.getItem("access_token");
  const headers = { ...options.headers, Authorization: `Bearer ${token}` };
  return fetch(API_URL + url, { ...options, headers });
}