import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        results = self.model.track(frame, persist=True, classes=[0])  # only person
        return results