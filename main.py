
from fastapi import FastAPI
import sqlite3

app = FastAPI()

# SQLite3 연결 함수
def get_db_connection():
    conn = sqlite3.connect('fake_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# 모든 사용자 조회 API
@app.get("/users")
def read_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return {"users": [dict(user) for user in users]}

# 특정 사용자 조회 API
@app.get("/users/{user_id}")
def read_user(user_id: int):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user is None:
        return {"error": "User not found"}
    return dict(user)
