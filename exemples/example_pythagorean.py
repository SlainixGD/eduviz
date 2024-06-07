# examples/example_pythagorean.py
from eduviz import EduViz, CircleVisualization, SquareVisualization

def main():
    viz = EduViz()
    
    circle = CircleVisualization(5)
    square = SquareVisualization(10)
    
    viz.add_element(circle)
    viz.add_element(square)
    
    viz.render()

if __name__ == "__main__":
    main()