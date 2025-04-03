# moderation.py
from app.database import get_db_connection

def flag_post(post_id, reason):
    conn = get_db_connection()
    conn.execute("INSERT INTO flags (post_id, reason) VALUES (?, ?)", (post_id, reason))
    conn.commit()
    conn.close()

def escalate_post(post_id):
    conn = get_db_connection()
    num_flags = conn.execute("SELECT COUNT(*) FROM flags WHERE post_id = ?", (post_id,)).fetchone()[0]
    user_id = conn.execute("SELECT user_id FROM posts WHERE post_id = ?", (post_id,)).fetchone()[0]

    if num_flags == 1:
        conn.execute("INSERT INTO user_ban_history (user_id, action) VALUES (?, 'warned')", (user_id,))
    elif num_flags == 3:
        conn.execute("DELETE FROM posts WHERE post_id = ?", (post_id,))
        conn.execute("INSERT INTO user_ban_history (user_id, action) VALUES (?, 'deleted_post')", (user_id,))
    elif num_flags > 5:
        conn.execute("UPDATE users SET ban_status = TRUE WHERE user_id = ?", (user_id,))
        conn.execute("INSERT INTO user_ban_history (user_id, action) VALUES (?, 'banned')", (user_id,))
    
    conn.commit()
    conn.close()
