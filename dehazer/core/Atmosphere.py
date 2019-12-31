#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import math


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

    M, N = darkChannel.shape

    numPixels = int(max(math.floor(M * N * p), 1))
    darkChannelVector = darkChannel.reshape(M * N, 1)
    IVector = I.reshape(M * N, 3)
    indices = darkChannelVector.argsort()[M * N - numPixels::]

    ASum = np.zeros(3)
    for index in range(numPixels):
        ASum += np.squeeze(IVector[indices[index]])

    A = ASum / numPixels
    A = np.minimum(A, AMax)

    return A
