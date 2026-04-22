import streamlit as st
import cv2
from detector import Detector
from counter import Counter
from alert import IntrusionDetector

st.title("AI Surveillance System")

run = st.checkbox("Start Camera")

frame_window = st.image([])
counter_text = st.empty()
alert_text = st.empty()

detector = Detector()
counter = Counter()
intrusion = IntrusionDetector((200, 100, 400, 300))

cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        break

    results = detector.detect(frame)

    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xywh.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy().astype(int)

        # counting
        up, down = counter.update(boxes, ids)

        # intrusion
        alerts = intrusion.check(boxes)

        # draw boxes
        annotated = results[0].plot()

        # draw line
        cv2.line(annotated, (0, 250), (640, 250), (255, 0, 0), 2)

        # draw intrusion zone
        cv2.rectangle(annotated, (200, 100), (400, 300), (0, 0, 255), 2)

        frame_window.image(annotated, channels="BGR")

        counter_text.write(f"⬆️ Up: {up} | ⬇️ Down: {down}")

        if alerts:
            alert_text.error("🚨 INTRUSION DETECTED!")
        else:
            alert_text.success("✅ Area Clear")

cap.release()