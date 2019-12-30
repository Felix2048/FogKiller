from dehazer.filter import *
from dehazer.core import *
import numpy as np
import unittest

from PIL import Image
import matplotlib.pyplot as plt


class CoreTest(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)
        self.origin = Image.open('../../image/forest1.jpg')
        self.image = np.asarray(self.origin)
        self.darkChannel = DarkChannel.getDarkChannel(self.image)

    # def test_box_filter(self):
    #     plt.figure('DarkChannel')
    #     plt.imshow(self.darkChannel, cmap='gray')
    #     plt.show()
    #     boxFiltered = BoxFilter.filter(self.darkChannel)
    #     plt.figure('BoxFiltered')
    #     plt.imshow(boxFiltered, cmap='gray')
    #     plt.show()
    #     self.assertTrue(boxFiltered is not None)

    # def test_guided_filter(self):
    #     plt.figure('DarkChannel')
    #     plt.imshow(self.darkChannel, cmap='gray')
    #     plt.show()
    #     guidedFilter = GuidedFilter.filter(
    #         self.darkChannel, self.image, s=None)
    #     plt.figure('GuidedFilter')
    #     plt.imshow(guidedFilter, cmap='gray')
    #     plt.show()
    #     self.assertTrue(guidedFilter is not None)

    def test_fast_guided_filter(self):
        plt.figure('DarkChannel')
        plt.imshow(self.darkChannel, cmap='gray')
        plt.show()
        fastGuidedFilter = GuidedFilter.filter(self.darkChannel, self.image)
        plt.figure('FastGuidedFilter')
        plt.imshow(fastGuidedFilter, cmap='gray')
        plt.show()
        self.assertTrue(fastGuidedFilter is not None)
