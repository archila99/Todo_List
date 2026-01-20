# Todo App

A full-stack Todo application built with **FastAPI** (Python) for the backend and **React + Vite** for the frontend, utilizing **MySQL** for persistence and **JWT** for secure authentication.

## ⚡ Features

- **Authentication**: User Registration and Login using JWT (JSON Web Tokens).
- **Secure Password Hashing**: Uses `bcrypt` for storing passwords securely.
- **CRUD Operations**: Create, Read, Delete todos securely (user-scoped).
- **Responsive UI**: Built with React and CSS for a clean user experience.
- **Database**: Persistent storage with MySQL.

---

## 🏗️ Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Uvicorn, Python-Jose (JWT), Passlib (Bcrypt)
- **Frontend**: React, Vite, React Router DOM
- **Database**: MySQL

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js & npm
- MySQL Server running locally

### 1. Backend Setup

Navigate to the backend directory:
```bash
cd backend
```

Create and activate a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the database setup script (ensure MySQL is running):
```bash
# Update DATABASE_URL in app/core/database.py or .env if needed
python3 create_db.py
```

Start the backend server:
```bash
uvicorn app.main:app --reload --port 8000
```
The API will be available at `http://127.0.0.1:8000`.

### 2. Frontend Setup

Navigate to the frontend directory:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Start the development server:
```bash
npm run dev
```
The app will be running at `http://localhost:5173`.

---

## 🧪 Testing Credentials

A test user has been created for your convenience:
- **Username**: `ali`
- **Password**: `1111`

---

## 📝 API Endpoints

- `POST /auth/register`: Register a new user.
- `POST /auth/login`: Login and receive an access token.
- `GET /todos/`: Get all todos for the authenticated user.
- `POST /todos/`: Create a new todo.
- `DELETE /todos/{id}`: Delete a specific todo.

---

## 🛠️ Configuration

- **Database URL**: Configure in `backend/app/core/database.py`.
- **Secret Key**: Managed in `backend/app/config.py` (ensure this is kept secret in production).
