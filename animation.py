# eduviz/animations.py
class AnimateCircle:
    def __init__(self, circle, duration):
        self.circle = circle
        self.duration = duration

    def animate(self):
        print(f"Animating circle with radius {self.circle.radius} over {self.duration} seconds")