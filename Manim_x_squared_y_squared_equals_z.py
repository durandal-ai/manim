import numpy as np
from manim import *
import math


class ThreeDGraph(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        target_point = np.array([0, 0, 3])
        self.set_camera_orientation(phi=60 * DEGREES, theta=-30 * DEGREES, frame_center=target_point)

        graph = Surface(
            lambda u, v: np.array([u, v, u**2 + v**2]),
            u_range=(-2, 2),
            v_range=(-2, 2),
            resolution=(15, 15),
            fill_color=BLUE,
            fill_opacity=0.2,
            stroke_color=GRAY,
            stroke_width=0.1
        )
        
        self.add(axes)
        self.play(Create(graph))
        self.wait(10)