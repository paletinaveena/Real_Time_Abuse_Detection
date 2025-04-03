import sys
import os
import time
import streamlit as st
import pandas as pd

# ✅ Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Local imports
from app.database import get_db_connection

# --- Page Config ---
st.set_page_config(page_title="Moderation Dashboard", layout="wide")

# --- Title ---
st.title("🛡️ Real-Time Moderation Dashboard")

# --- Auto-Refresh Settings ---
with st.sidebar:
    st.header("🔄 Refresh Settings")
    enable_auto = st.checkbox("Enable Auto Refresh", value=True)
    interval = st.slider("Refresh Interval (seconds)", min_value=10, max_value=300, value=60)
    if st.button("🔁 Manual Refresh"):
        st.rerun()

# --- Fetch Data from DB ---
conn = get_db_connection()
query = """
    SELECT p.post_id, u.username, p.content, f.reason, f.timestamp
    FROM posts p
    JOIN flags f ON p.post_id = f.post_id
    JOIN users u ON p.user_id = u.user_id
    ORDER BY f.timestamp DESC
"""
df = pd.read_sql(query, conn)
if not df.empty:
    last_scan_time = df["timestamp"].max()
    st.info(f"🕒 Last scanned at: {last_scan_time.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.warning("⚠️ No flagged tweets found yet.")
conn.close()

# --- Sidebar Filters ---
with st.sidebar:
    st.header("🔍 Filters")
    selected_usernames = st.multiselect("Filter by Username", options=df["username"].unique())
    selected_reasons = st.multiselect("Filter by Reason", options=df["reason"].unique())

# --- Apply Filters ---
if selected_usernames:
    df = df[df["username"].isin(selected_usernames)]
if selected_reasons:
    df = df[df["reason"].isin(selected_reasons)]

# --- Timestamp Handling ---
df["timestamp"] = pd.to_datetime(df["timestamp"])

# --- Flag Trends Over Time ---
st.subheader("📈 Flags Over Time (Hourly)")
flag_trend = df.set_index("timestamp").resample("1H").size()
st.line_chart(flag_trend)

# --- Flag Reasons Breakdown ---
st.subheader("📊 Flag Reasons")
st.bar_chart(df["reason"].value_counts())

# --- Show Flagged Posts Table ---
st.subheader("🚨 Flagged Posts")
st.dataframe(df, use_container_width=True)

# --- Auto-refresh Logic ---
if enable_auto:
    time.sleep(interval)
    st.rerun()
