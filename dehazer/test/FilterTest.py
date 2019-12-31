from dehazer.filter import *
from dehazer.core import *
import numpy as np
import unittest

from PIL import Image
import matplotlib.pyplot as plt


class FilterTest(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)
        self.origin = Image.open('../../image/forest1.jpg')
        self.image = np.asarray(self.origin)
        self.darkChannel = DarkChannel.getDarkChannel(self.image)
        self.A = Atmosphere.getAtmosphere(
            self.image, self.darkChannel)
        self.t = Transmission.getTransmission(
            self.image, self.darkChannel, self.A)
        self.normImage = (self.image - self.image.min()) / \
            (self.image.max() - self.image.min())

    def test_box_filter(self):
        boxFiltered = BoxFilter.filter(self.t)
        plt.figure('BoxFiltered')
        plt.imshow(boxFiltered, cmap='gray')
        plt.show()
        self.assertTrue(boxFiltered is not None)

    def test_guided_filter(self):
        guidedFilter = GuidedFilter.filter(
            self.t, self.normImage, s=None)
        plt.figure('GuidedFilter')
        plt.imshow(guidedFilter, cmap='gray')
        plt.show()
        self.assertTrue(guidedFilter is not None)

    def test_fast_guided_filter(self):
        fastGuidedFilter = GuidedFilter.filter(
            self.t, self.normImage, s=4)
        plt.figure('FastGuidedFilter')
        plt.imshow(fastGuidedFilter, cmap='gray')
        plt.show()
        self.assertTrue(fastGuidedFilter is not None)
