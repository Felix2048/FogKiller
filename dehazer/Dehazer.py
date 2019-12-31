#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from .core import *
from .filter import *

from PIL import Image
import matplotlib.pyplot as plt

R, G, B = 0, 1, 2   # RGB index
RGB = 3


class Dehazer:
    """
    Dehazer: Single Image Haze Removal

    Reference:

    - http://kaiminghe.com/publications/cvpr09.pdf

    - http://kaiminghe.com/publications/eccv10guidedfilter.pdf

    - https://arxiv.org/abs/1505.00996

    """

    @staticmethod
    def dehaze(image, patchSize=15, p=0.0001, AMax=240, w=0.95, tMin=0.1,
               useFilter=True, r=40, epsilon=1e-3, s=4, viewProgress=True):
        """
        Get the transmission t of the RGB image data from a numpy array

        # Arguments

        - image:    3 * M * N numpy array of the input image, where 3 stands for
                    the RGB channels, M is the height, and N is the width

        - patchSize:    patch size

        - p:    the top p brightest pixels in the dark channel

        - AMax: threshold of atmosphere

        - w:    a constant parameter (0 < w <= 1) to optionally keep a very small
            amount of haze for the distant objects (aerial perspective)

        - patchSize:        patch size

        - tMin:     threshold of transmission rate

        - useFilter:    boolean to choose whether or not to use guided filter

        - r:   square window of a radius r (integer)

        - epsilon:  argument for guided filter regularization

        - s:    subsampling ratio for fast guided filter, None stands for only
                use guided filter

        - viewProgress: boolean to choose whether or not to show the dehazing
                        progress

        # Returns

        -   3 * M * N numpy array of the haze free output image, where 3 stands
            for the RGB channels, M is the height, and N is the width

        """

        M, N, _ = image.shape

        Idark = DarkChannel.getDarkChannel(image, patchSize=patchSize)

        A = Atmosphere.getAtmosphere(image, Idark, p=p, AMax=AMax)

        origin_t = Transmission.getTransmission(
            image, A, w=w, patchSize=patchSize)

        t = origin_t
        if useFilter:
            normImage = (image - image.min()) / (image.max() - image.min())
            t = GuidedFilter.filter(
                t, normImage, r=r, epsilon=epsilon, s=s)
        t = np.maximum(t, tMin)

        J = np.empty_like(image)
        for channel in range(3):
            J[:, :, channel] = (image[:, :, channel] -
                                A[channel]) / t + A[channel]

        if viewProgress:
            plt.figure('I')
            plt.imshow(image)
            plt.show()

            plt.figure('Idark')
            plt.imshow(Idark, cmap='gray')
            plt.show()

            plt.figure('A')
            colors = ['r', 'g', 'b']
            plt.title('Atmosphere')
            plt.scatter([0, 1, 2], A, c=colors, marker='o')
            plt.xlabel('RGB Channel')
            plt.ylabel('Atmosphere Value')
            plt.show()

            plt.figure('origin t')
            plt.imshow(origin_t, cmap='gray')
            plt.show()

            plt.figure('t')
            plt.imshow(t, cmap='gray')
            plt.show()

            plt.figure('J')
            plt.imshow(J)
            plt.show()

        return J
