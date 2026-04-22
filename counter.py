class Counter:
    def __init__(self, line_y=250):
        self.line_y = line_y
        self.count_up = 0
        self.count_down = 0
        self.track_history = {}

    def update(self, boxes, ids):
        for box, track_id in zip(boxes, ids):
            x, y, w, h = box
            center_y = int(y + h / 2)

            if track_id not in self.track_history:
                self.track_history[track_id] = []

            self.track_history[track_id].append(center_y)

            if len(self.track_history[track_id]) >= 2:
                prev_y = self.track_history[track_id][-2]

                if prev_y < self.line_y and center_y >= self.line_y:
                    self.count_down += 1
                elif prev_y > self.line_y and center_y <= self.line_y:
                    self.count_up += 1

        return self.count_up, self.count_down