# eduviz/visualizations.py
class CircleVisualization:
    def __init__(self, radius):
        self.radius = radius

    def render(self):
        print(f"Rendering a circle with radius {self.radius}")

class SquareVisualization:
    def __init__(self, side_length):
        self.side_length = side_length

    def render(self):
        print(f"Rendering a square with side length {self.side_length}")
