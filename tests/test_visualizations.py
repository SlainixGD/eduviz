# tests/test_visualizations.py
import unittest
from eduviz.visualizations import CircleVisualization, SquareVisualization

class TestVisualizations(unittest.TestCase):
    def test_circle_visualization(self):
        circle = CircleVisualization(5)
        self.assertEqual(circle.radius, 5)

    def test_square_visualization(self):
        square = SquareVisualization(10)
        self.assertEqual(square.side_length, 10)

if __name__ == '__main__':
    unittest.main()