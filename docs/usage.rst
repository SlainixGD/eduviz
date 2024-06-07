Usage
=====

Here are some examples of how to use EduViz.

Creating a Circle Visualization
-------------------------------

.. code-block:: python

   from eduviz.visualizations import CircleVisualization

   circle = CircleVisualization(radius=5)
   circle.render()

Creating and Animating a Circle
-------------------------------

.. code-block:: python

   from eduviz.visualizations import CircleVisualization
   from eduviz.animations import AnimateCircle

   circle = CircleVisualization(radius=5)
   animation = AnimateCircle(circle, duration=2)
   animation.animate()
