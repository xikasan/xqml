# -*- coding: utf-8 -*-

import numpy as np

from .base import BaseFunc


class Circle(BaseFunc):

    xdim = 2

    num_div_plot = 50

    is_regression = False

    def __init__(self, r=np.sqrt(2/np.pi), center=(0.0, 0.0), seed=None):
        super().__init__(seed)
        self.r = r
        self.center = np.asarray(center).reshape(1, 2)

    def __str__(self):
        return "Circle(r=2/pi)"

    def fbody(self, xs, *args, **kwargs):
        rs = np.linalg.norm(xs - self.center, axis=1)
        ys = np.ones((xs.shape[0], 1))
        ys[rs > self.r] = -1
        return ys
