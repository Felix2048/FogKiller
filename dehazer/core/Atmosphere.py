#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


def getAtmosphere(I, darkChannel, p=0.0001, AMax=240):
    """
    Get the atmosphere light of the RGB image data from a numpy array

    # Arguments

    - I:  3 * M * N numpy array of the input image, where 3 stands for
          the RGB channels, M is the height, and N is the width

    - darkChannel:  the dark channel prior of the image as an M * N numpy array

    - p:  the top p brightest pixels in the dark channel

    - AMax: threshold of atmosphere

    # Returns

    - 3-element list contains atmosphere light ([0, L-1]) for each RGB channel

    """

    # M, N = darkChannel.shape
    # flattenI = I.reshape(M * N, 3)
    # flattenDarkChannel = darkChannel.ravel()
    # # get the indexes of the top p brightest pixels in the dark channel
    # brightestIndex = (-flattenDarkChannel).argsort()[:int(M * N * p)]
    # # take the highest intensity for each channel
    # A = np.max(flattenI.take(brightestIndex, axis=0), axis=0)

    mean_perpix = np.mean(I, axis=2).reshape(-1)
    mean_topper = mean_perpix[:int(I.shape[0] * I.shape[1] * p)]
    A = np.mean(mean_topper)

    # set a threshold for atmosphere
    if AMax is not None:
        A = np.minimum(A, AMax)

    return A
