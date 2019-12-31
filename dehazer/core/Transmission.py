#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

from dehazer.core.DarkChannel import getDarkChannel


def getTransmission(I, A, w=0.95, patchSize=15):
    """
    Get the transmission t of the RGB image data from a numpy array

    # Arguments

    - I:    3 * M * N numpy array of the input image, where 3 stands for
          the RGB channels, M is the height, and N is the width

    - A:    3-element list contains atmosphere light ([0, L-1]) for each RGB
            channel

    - w:    a constant parameter (0 < w <= 1) to optionally keep a very small
            amount of haze for the distant objects (aerial perspective)

    - patchSize:        patch size

    # Returns

    - M * N numpy array of the transmission rate [0.0, 1.0] of the input image

    """

    t = 1 - w * getDarkChannel(I / A, patchSize)

    return t
