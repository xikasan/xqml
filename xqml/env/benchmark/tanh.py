# -*- coding: utf-8 -*-

import numpy as np

from .base import BaseFunc


class Tanh(BaseFunc):

    is_regression = True

    def __init__(self, seed=None):
        super().__init__(seed)

    def __str__(self):
        return "tanh(5x)"

    def fbody(self, xs, *args, **kwargs):
        return np.tanh(5 * xs)
