from dehazer import *
import numpy as np
import unittest

from PIL import Image
import matplotlib.pyplot as plt


class CoreTest(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)
        self.origin = Image.open('../../image/forest1.jpg')
        self.image = np.asarray(self.origin)

    def test_dehaze(self):
        dehazedImage = Dehazer.dehaze(self.image)
        self.assertTrue(dehazedImage is not None)
