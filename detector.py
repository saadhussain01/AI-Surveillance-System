import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self):
        self.model = YOLO("yolov8l.pt")

    def detect(self, frame):
        results = self.model.track(
        frame,
        persist=True,
        conf=0.5
    )
        return results