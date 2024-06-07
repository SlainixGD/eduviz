# tests/test_core.py
import unittest
from eduviz.core import EduViz
from eduviz.visualizations import CircleVisualization, SquareVisualization

class TestEduViz(unittest.TestCase):
    def test_add_and_render_elements(self):
        viz = EduViz()
        circle = CircleVisualization(5)
        square = SquareVisualization(10)

        viz.add_element(circle)
        viz.add_element(square)

        # Check that elements are added
        self.assertIn(circle, viz.elements)
        self.assertIn(square, viz.elements)

if __name__ == '__main__':
    unittest.main()