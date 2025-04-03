# database.py
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('forum.db')
    return conn

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        ban_status BOOLEAN DEFAULT FALSE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        content TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flags (
        flag_id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER,
        reason TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (post_id) REFERENCES posts(post_id)
    )
    ''')

    # ✅ Create indexes with separate calls
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_id ON posts(user_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_post_id ON flags(post_id)")

    conn.commit()
    conn.close()
