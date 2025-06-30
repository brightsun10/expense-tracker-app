# 💸 Personal Expense Tracker (FastAPI + SQLite)

A minimalist web application to **track personal expenses** — built with **FastAPI**, **Jinja2**, and **SQLite**.

This project enables users to log their daily expenses, categorize them, and view summarized insights. It's lightweight, fast, and deployable with minimal setup.

---

## ✨ Features

- Add, view, and delete expenses
- Auto-generated timestamps
- Category-wise total breakdown
- Beautiful web UI (using Jinja2 templates)
- Simple database using SQLite

---

## 🖼️ Screenshots

> 📸 _Add your app UI screenshots here if available_  
> Or run locally to view the dashboard.

---

## 🚀 Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| Web Framework | FastAPI       |
| Database     | SQLite         |
| Templates    | Jinja2         |
| Styling      | HTML + CSS (via `/static`) |

---

## 📁 Project Structure

expense-tracker-app/

│

├── app.py / main.py # Main FastAPI app

├── templates/

│ └── index.html # Jinja2 UI template

├── static/

│ └── style.css # (Optional) CSS styles

├── expenses.db # SQLite database

├── README.md

└── requirements.txt

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/brightsun10/expense-tracker-app.git

cd expense-tracker-app

### 2. Create a Virtual Environment (optional but recommended)

python -m venv venv

source venv/bin/activate       # Windows: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Application

uvicorn main:app --reload

Now, visit: http://localhost:8000

## ✏️ Usage
Navigate to / to view the dashboard.

Use the form to add a new expense.

Each entry shows: description, amount, category, and timestamp.

Click "Delete" to remove any record.

## 💾 Data Persistence

Expenses are stored in expenses.db (SQLite).

The DB is created automatically on first run using init_db().

## ✅ Requirements
Python 3.8+

FastAPI

Uvicorn

Jinja2

## 📦 You can install all dependencies with:

pip install fastapi uvicorn jinja2 python-multipart


## 🙋‍♂️ Author

Made with ❤️ by Nithin P (brightsun10)

📄 License
This project is open-source under the MIT License.
