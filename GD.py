from manim import *
import numpy as np
import math

class PlotGraph(Scene):
    def construct(self):
        # Create the axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            axis_config={"color": BLUE},
        )

        # Create the graph of y=x^2
        graph = axes.plot(lambda x: x**2, color=WHITE)

        alpha = ValueTracker(0)
        point = always_redraw(
            lambda: Dot(
                graph.point_from_proportion(alpha.get_value()),
                color=BLUE
            ))

        tangent = always_redraw(
            lambda: TangentLine(
                graph,
                alpha=alpha.get_value(),
                color=YELLOW,
                length=4
            ))

        # Display the axes and graph
        self.play(Create(axes), Create(graph), run_time=2)
        self.add(point, tangent)
        self.play(alpha.animate.set_value(1), rate_func=linear, run_time=20)
        self.wait(10)

        