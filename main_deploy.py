import streamlit as st
import cv2
import tempfile
import time

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Smart Crowd Monitor", layout="wide")

st.title("🎓 Smart Campus Crowd Monitoring System")

area = st.selectbox("📍 Select Area", ["Library", "Canteen", "Auditorium"])

col1, col2, col3 = st.columns(3)
current_placeholder = col1.empty()
total_placeholder = col2.empty()
limit_placeholder = col3.empty()

alert_placeholder = st.empty()
frame_placeholder = st.empty()

# Area limits
if area == "Library":
    MAX_LIMIT = 5
elif area == "Canteen":
    MAX_LIMIT = 8
else:
    MAX_LIMIT = 12

video = st.file_uploader("📂 Upload Video", type=["mp4", "avi"])

if not video:
    st.warning("Upload a video to start monitoring")
    st.stop()

tfile = tempfile.NamedTemporaryFile(delete=False)
tfile.write(video.read())

cap = cv2.VideoCapture(tfile.name)

# HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

total_seen = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect people
    boxes, _ = hog.detectMultiScale(frame, winStride=(8,8))

    current_count = len(boxes)
    total_seen += current_count

    # Draw boxes
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    # UI update
    current_placeholder.metric("👥 Current", current_count)
    total_placeholder.metric("📊 Total Seen", total_seen)
    limit_placeholder.metric("⚠️ Limit", MAX_LIMIT)

    if current_count > MAX_LIMIT:
        alert_placeholder.error("🚨 Crowd Limit Exceeded!")
    else:
        alert_placeholder.success("✅ Safe")

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame, channels="RGB")

    time.sleep(0.05)

cap.release()