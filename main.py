from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import sqlite3
from datetime import datetime
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Setup app
app = FastAPI(title="Personal Expense Tracker")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
DB_PATH = "expenses.db"  # No absolute path

# Ensure database exists
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        conn.commit()

init_db()

@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("SELECT * FROM expenses ORDER BY timestamp DESC").fetchall()
    total = sum(row[2] for row in rows)
    categories = list(set(row[3] for row in rows))
    category_totals = {c: sum(row[2] for row in rows if row[3] == c) for c in categories}
    return templates.TemplateResponse("index.html", {
        "request": request,
        "expenses": rows,
        "total": total,
        "category_totals": category_totals
    })

@app.post("/add")
def add_expense(description: str = Form(...), amount: float = Form(...), category: str = Form(...)):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO expenses (description, amount, category, timestamp)
            VALUES (?, ?, ?, ?)
        """, (description, amount, category, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/delete/{id}")
def delete_expense(id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (id,))
        conn.commit()
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
