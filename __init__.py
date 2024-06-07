# eduviz/__init__.py
from .core import EduViz
from .visualizations import CircleVisualization, SquareVisualization
from .animations import AnimateCircle
from .media import MediaHandler

__all__ = ['EduViz', 'CircleVisualization', 'SquareVisualization', 'AnimateCircle', 'MediaHandler']