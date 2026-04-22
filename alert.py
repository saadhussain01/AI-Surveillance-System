class IntrusionDetector:
    def __init__(self, zone):
        self.zone = zone  # (x1, y1, x2, y2)

    def check(self, boxes):
        alerts = []
        x1, y1, x2, y2 = self.zone

        for box in boxes:
            x, y, w, h = box
            cx = int(x + w / 2)
            cy = int(y + h / 2)

            if x1 < cx < x2 and y1 < cy < y2:
                alerts.append((cx, cy))

        return alerts