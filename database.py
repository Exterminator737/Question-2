import sqlite3

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

def add_user(data):
    """Replace the existing user (id=1)"""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO user (id, name, email, age) VALUES (1, ?, ?, ?)",
                (data["name"], data["email"], data["age"]))
    conn.commit()
    conn.close()

def get_user():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, age FROM user WHERE id = 1")
    row = cur.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "name": row[1], "email": row[2], "age": row[3]}
    else:
        return {"id": 1, "name": "", "email": "", "age": ""}

def update_user(fields):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    for key, value in fields.items():
        cur.execute(f"UPDATE user SET {key} = ? WHERE id = 1", (value,))
    conn.commit()
    conn.close()
