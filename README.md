# Bodjeh (Budget Reporting System) 🚀

Bodjeh is a web-based budget data collection and management system built with **FastAPI**, **React**, and **SQL Server**. The application replaces Excel-based data entry with validated web forms and stores the information in a structured relational database that can be consumed directly by existing **Power BI** reports.

The main goal of the project is to improve data quality, reduce manual errors, and provide a reliable workflow for collecting budget and operational data from different departments.

---

# Overview

Many organizations still collect budget and financial information through Excel files. As the amount of data grows, maintaining consistency becomes difficult and manual corrections consume valuable time.

Bodjeh addresses these challenges by providing:

* Centralized web-based data entry
* Input validation
* Secure authentication
* Structured SQL Server database
* REST API for frontend communication
* Seamless integration with Power BI

Instead of replacing the reporting system, Bodjeh acts as the data collection layer before the data reaches Power BI.

---

# Features

Current features include:

* JWT Authentication
* User login
* Dynamic data entry forms
* CRUD operations
* SQL Server integration
* Data validation
* RESTful API
* Responsive React interface
* Power BI compatible database structure

### Planned Features

* Role-based permissions
* Audit logs
* File attachments
* Dashboard improvements
* Export capabilities

---

# Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication

### Frontend

* React
* Vite
* Bootstrap
* React Router

### Database

* Microsoft SQL Server

### Deployment

* Uvicorn
* NSSM
* IIS Reverse Proxy

---

# How It Works

The application follows a simple workflow:

1. Users authenticate using JWT.
2. Users enter budget or operational data through web forms.
3. The backend validates all submitted information.
4. Valid data is stored in SQL Server.
5. Existing Power BI dashboards read data directly from the database.

This architecture minimizes manual intervention and significantly reduces data inconsistencies.

---

# Project Structure

```text
bodjeh/
│
├── app/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── database.py
│   └── main.py
│
├── frontend/
│
├── requirements.txt
├── package.json
├── README.md
└── .env
```

---

# Getting Started

## Clone the repository

```bash
git clone git@github.com:zahra-ghesmati/bodjeh.git
cd bodjeh
```

---

## Backend Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn app.main:app --reload
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will start in development mode and connect to the FastAPI backend.

---

# Production Deployment

Typical deployment on Windows Server consists of:

* Building the React frontend
* Configuring the production `.env`
* Running FastAPI as a Windows Service using NSSM
* Configuring IIS as a reverse proxy
* Connecting the application to SQL Server

---

# API Documentation

After starting the backend, Swagger UI is available at:

```text
http://localhost:8000/docs
```

---

# Screenshots

> TODO: Add screenshots of:
>
> * Login page
> * Dashboard
> * Dynamic forms
> * User management

---

# Roadmap

* [ ] Role-based permissions
* [ ] Audit logging
* [ ] Better dashboard
* [ ] Export to Excel
* [ ] Improved validation
* [ ] Docker support

---

# Author

**Zahra Ghesmati**

Backend Developer

GitHub: https://github.com/zahra-ghesmati

LinkedIn: https://www.linkedin.com/in/zahra-ghesmati/

---
