#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


def getDarkChannel(I, patchSize=15):
    """
    Get the dark channel prior of the RGB image data from a numpy array

    # Arguments

    - I:  3 * M * N numpy array of the input image, where 3 stands for
          the RGB channels, M is the height, and N is the width

    - patchSize:  patch size

    # Returns

    - M * N numpy array of the Dark Chanel of the input image

    """

    M, N, _ = I.shape

    padding = ((int(patchSize / 2), int(patchSize / 2)),
               (int(patchSize / 2), int(patchSize / 2)), (0, 0))
    paddedImage = np.pad(I, padding, 'edge')
    darkChannel = np.zeros((M, N))
    for i, j in np.ndindex(darkChannel.shape):
        darkChannel[i, j] = np.min(paddedImage[i:i + patchSize,
                                               j: j + patchSize, :])

    return darkChannel
