import streamlit as st
import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import time
import tempfile

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Smart Crowd Monitor", layout="wide")

# ---------------- UI ----------------
st.title("🎓 Smart Campus Crowd Monitoring System")
st.write("Upload a video to analyze crowd density using AI.")

area = st.selectbox("📍 Select Area", ["Library", "Canteen", "Auditorium"])

# Dashboard
col1, col2, col3 = st.columns(3)
current_placeholder = col1.empty()
total_placeholder = col2.empty()
limit_placeholder = col3.empty()

alert_placeholder = st.empty()
frame_placeholder = st.empty()

# Upload video
video_file = st.file_uploader("📂 Upload Video", type=["mp4", "avi"])

if not video_file:
    st.warning("Please upload a video to start analysis")
    st.stop()

# Save temp video
tfile = tempfile.NamedTemporaryFile(delete=False)
tfile.write(video_file.read())

# ---------------- MODEL ----------------
model = YOLO("yolov8n.pt")
tracker = DeepSort(max_age=30)

cap = cv2.VideoCapture(tfile.name)

total_count = set()
MAX_LIMIT = 5

# ---------------- LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        st.success("✅ Video processing completed")
        break

    results = model(frame)

    detections = []
    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        cls = int(box.cls[0])

        if cls == 0 and conf > 0.4:
            w = x2 - x1
            h = y2 - y1
            detections.append(([x1, y1, w, h], conf, "person"))

    tracks = tracker.update_tracks(detections, frame=frame)

    current_count = 0

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        total_count.add(track_id)
        current_count += 1

        l, t, r, b = map(int, track.to_ltrb())
        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)

    # UI updates
    current_placeholder.metric("👥 Current", current_count)
    total_placeholder.metric("📊 Total Seen", len(total_count))
    limit_placeholder.metric("⚠️ Limit", MAX_LIMIT)

    if current_count > MAX_LIMIT:
        alert_placeholder.error("🚨 Crowd Limit Exceeded!")
    else:
        alert_placeholder.success("✅ Crowd Under Control")

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame, channels="RGB")

    time.sleep(0.03)

cap.release()