# 🎓 Smart Campus Crowd Monitoring System

## 🚀 Overview
This project is an AI-powered system that monitors crowd density in real time using computer vision. It helps improve campus safety and resource management by detecting overcrowding and triggering alerts.

---

## 🧠 Problem Statement
In campuses, overcrowding in areas like libraries, canteens, and auditoriums can lead to safety risks and inefficient resource usage. There is no real-time system to monitor and control this.

---

## 💡 Solution
We built a system using:
- YOLOv8 for person detection
- DeepSORT for tracking individuals
- Streamlit for dashboard UI

The system:
- Detects people in real time
- Tracks unique individuals
- Counts current and total crowd
- Triggers alerts when limits are exceeded

---

## 🔥 Features
- 👥 Real-time crowd detection
- 🎯 Unique person tracking using DeepSORT
- 📊 Live dashboard with metrics
- 🚨 Crowd limit alert system
- 📍 Area-based monitoring (Library, Canteen, Auditorium)
- 📂 Video upload support (for cloud deployment)

---

## 🛠️ Tech Stack
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- DeepSORT
- Streamlit

---

## 📁 Project Structure
- crowd-monitor/
- │
- ├── main_local.py     # Webcam version (demo)
- ├── main_deploy.py    # Deployment version (upload video)
- ├── requirements.txt
- ├── README.md
- └── yolov8n.pt (optional)