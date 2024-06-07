# examples/example_interactive_quiz.py
from eduviz import EduViz, CircleVisualization

def main():
    viz = EduViz()
    
    circle = CircleVisualization(5)
    
    viz.add_element(circle)
    
    viz.render()

if __name__ == "__main__":
    main()