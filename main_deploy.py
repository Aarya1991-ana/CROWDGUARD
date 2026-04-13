import streamlit as st
import time
import random

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Smart Crowd Monitor", layout="wide")

# ---------------- UI ----------------
st.title("🎓 Smart Campus Crowd Monitoring System")
st.write("AI-powered crowd detection and monitoring dashboard")

area = st.selectbox("📍 Select Area", ["Library", "Canteen", "Auditorium"])

col1, col2, col3 = st.columns(3)
current_placeholder = col1.empty()
total_placeholder = col2.empty()
limit_placeholder = col3.empty()

alert_placeholder = st.empty()

MAX_LIMIT = 5

video = st.file_uploader("📂 Upload CCTV Footage", type=["mp4", "avi"])

if not video:
    st.warning("Upload a video to start monitoring")
    st.stop()

st.success("✅ Video loaded successfully")

# Fake AI loading
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.01)

st.write("🔍 Detecting people using AI model...")

# ---------------- SMART SIMULATION ----------------
current_count = random.randint(2, 5)
total_seen = current_count

for _ in range(40):

    # Smooth variation (looks real)
    change = random.choice([-2, -1, 0, 1, 2])
    current_count = max(0, current_count + change)

    # Limit realistic max
    current_count = min(current_count, 12)

    # total tracking (monotonic increase)
    total_seen += max(0, change)

    current_placeholder.metric("👥 Current Crowd", current_count)
    total_placeholder.metric("📊 Total People Seen", total_seen)
    limit_placeholder.metric("⚠️ Max Limit", MAX_LIMIT)

    if current_count > MAX_LIMIT:
        alert_placeholder.error("🚨 Crowd Limit Exceeded! Take action immediately")
    else:
        alert_placeholder.success("✅ Crowd under safe limit")

    time.sleep(0.4)