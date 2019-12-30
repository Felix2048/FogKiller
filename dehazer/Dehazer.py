#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from .core import *
from .filter import *


class Dehazer:
    """
    Dehazer: Single Image Haze Removal

    Reference:

    - http://kaiminghe.com/publications/cvpr09.pdf

    - http://kaiminghe.com/publications/eccv10guidedfilter.pdf

    - https://arxiv.org/abs/1505.00996

    """

    @staticmethod
    def dehaze(image, patchSize=15, p=0.0001, AMax=220, w=0.95, tMin=0.2,
               useFilter=False, r=40, epsilon=1e-3, s=4):
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

        - s:  subsampling ratio for fast guided filter


        # Returns

        -   3 * M * N numpy array of the haze free output image, where 3 stands
            for the RGB channels, M is the height, and N is the width

        """

        M, N, _ = image.shape

        Idark = DarkChannel.getDarkChannel(image, patchSize=patchSize)
        A = Atmosphere.getAtmosphere(image, Idark, p=p, AMax=AMax)
        t = Transmission.getTransmission(
            image, Idark, A, w=w, patchSize=patchSize, tMin=tMin)

        if useFilter:
            normImage = (image - image.min()) / (image.max() - image.min())
            t = GuidedFilter.filter(
                Idark, normImage, r=r, epsilon=epsilon, s=s)

        tTile = np.zeros_like(image)
        tTile[:, :, R] = tiledt[:, :, G] = tiledt[:, :, B] = t
        J = (image - A) / tTile + A

        return J
