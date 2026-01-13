# Todo App

A full-stack Todo application built with **FastAPI** for the backend and **React + Vite** for the frontend.  
Users can create, read, update, and delete todos with a responsive UI and persistent database.

---

## 🏗️ Project Structure

Todo-app/
├── backend/ # FastAPI backend
│ ├── app/
│ │ ├── main.py # FastAPI application entry
│ │ ├── core/ # Database and dependency files
│ │ ├── models/ # SQLAlchemy models
│ │ ├── schemas/ # Pydantic schemas
│ │ └── routes/ # API routes
│ ├── create_db.py # Script to initialize the database
│ └── requirements.txt # Python dependencies
│
├── frontend/ # React + Vite frontend
│ ├── public/ # Static files
│ ├── src/
│ │ ├── App.js # Main React component
│ │ ├── api/ # API calls
│ │ ├── components/ # React components
│ │ └── styles/ # CSS files
│ └── package.json # Node dependencies
│
├── venv/ # Python virtual environment (ignored in git)
├── .gitignore
└── README.md

---

## ⚡ Features

- Create, read, update, and delete todos
- Persistent storage with **MySQL**
- Clean React frontend with reusable components
- Backend API with **FastAPI**
- Easy to scale and extend

---

## 🚀 Getting Started

### Backend Setup

1. Navigate to the backend folder:

```bash
cd backend

