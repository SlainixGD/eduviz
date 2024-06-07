# tests/test_animations.py
import unittest
from eduviz.animations import AnimateCircle
from eduviz.visualizations import CircleVisualization

class TestAnimations(unittest.TestCase):
    def test_animate_circle(self):
        circle = CircleVisualization(5)
        animation = AnimateCircle(circle, 2)
        self.assertEqual(animation.circle, circle)
        self.assertEqual(animation.duration, 2)

if __name__ == '__main__':
    unittest.main()