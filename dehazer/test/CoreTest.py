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

    # def test_dark_channel(self):
    #     plt.figure('origin')
    #     plt.imshow(self.origin)
    #     plt.show()
    #     self.darkChannel = DarkChannel.getDarkChannel(self.image)
    #     plt.figure('darkChannel')
    #     plt.imshow(self.darkChannel, cmap='gray')
    #     plt.show()
    #     self.assertTrue(self.darkChannel is not None)

    def test_atmosphere(self):
        p = 0.0001
        maxA = 220
        A = Atmosphere.getAtmosphere(
            self.image, self.darkChannel, p=p, maxA=maxA)
        self.assertIsNotNone(A)
        self.assertLessEqual(A[0], maxA)
        self.assertLessEqual(A[1], maxA)
        self.assertLessEqual(A[2], maxA)

        colors = ['r', 'g', 'b']
        plt.title('Atmosphere')
        plt.scatter([0, 1, 2], A, c=colors, marker='o')
        plt.xlabel('RGB Channel')
        plt.ylabel('Atmosphere Value')
        plt.show()
