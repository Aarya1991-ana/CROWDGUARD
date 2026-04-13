import streamlit as st
import time
import random

st.set_page_config(page_title="Smart Crowd Monitor", layout="wide")

st.title("🎓 Smart Campus Crowd Monitoring System")

area = st.selectbox("📍 Select Area", ["Library", "Canteen", "Auditorium"])

col1, col2, col3 = st.columns(3)

current_placeholder = col1.empty()
total_placeholder = col2.empty()
limit_placeholder = col3.empty()

alert_placeholder = st.empty()

MAX_LIMIT = 5

if st.button("Start Simulation"):

    for _ in range(50):
        current_count = random.randint(1, 10)

        current_placeholder.metric("👥 Current", current_count)
        total_placeholder.metric("📊 Total (Approx)", current_count)
        limit_placeholder.metric("⚠️ Limit", MAX_LIMIT)

        if current_count > MAX_LIMIT:
            alert_placeholder.error("🚨 Crowd Limit Exceeded!")
        else:
            alert_placeholder.success("✅ Crowd Under Control")

        time.sleep(0.2)