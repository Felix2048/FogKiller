#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import scipy.ndimage
from dehazer.filter import BoxFilter
from itertools import combinations_with_replacement
from collections import defaultdict

R, G, B = 0, 1, 2   # RGB index
RGB = 3


class GuidedFilter:
    """
    Guided Image Filter

    Reference:

    - http://kaiminghe.com/publications/eccv10guidedfilter.pdf

    - https://arxiv.org/abs/1505.00996

    """

    @staticmethod
    def filter(p, I, r=40, epsilon=1e-3, s=4):
        """
        Get the guided filtered RGB image data from a numpy array

        # Arguments

        - p:   M * N numpy array of the gray input image data
                                        normalized to [0.0, 1.0]

        - I:   M * N * 3 numpy array of the RGB guided image data

        - r:   square window of a radius r (integer)

        - epsilon:  argument for guided filter regularization

        - s:  subsampling ratio for fast guided filter

        # Returns

        - M * N numpy array of the filtered output image

        """

        originP = p
        originI = I

        """
        Subsample via Bilinear Interpolation
        """
        if s is not None:
            I = scipy.ndimage.zoom(originI, (1/s, 1/s, 1), order=1)
            p = scipy.ndimage.zoom(originP, (1/s, 1/s), order=1)
            r = round(r / s)
        M, N = p.shape
        r = min(r, int(M / 2 - 1), int(N / 2 - 1))
        base = BoxFilter.filter(np.ones((M, N)), r)

        """
        Calculate mean and cov for each channel
        """
        # each channel of I filtered with the mean filter
        meanI = [BoxFilter.filter(I[:, :, channel], r) /
                 base for channel in range(RGB)]
        # p filtered with the mean filter
        meanp = BoxFilter.filter(p, r) / base
        # I filtered with p and then the mean filter
        meanIp = [BoxFilter.filter(
            I[:, :, channel] * p, r) / base for channel in range(RGB)]
        # covariance of I and p in each local patch
        covIp = [meanIp[channel] - meanI[channel]
                 * meanp for channel in range(RGB)]
        """
        Calculate mean for a and b
        """
        varI = defaultdict(dict)
        for i, j in combinations_with_replacement(range(RGB), 2):
            varI[i][j] = BoxFilter.filter(
                I[:, :, i] * I[:, :, j], r) / base - meanI[i] * meanI[j]
        a = np.zeros((M, N, 3))
        # Symmetric covariance matrix of I in each patch:
        # rr, rg, rb
        # rg, gg, gb
        # rb, gb, bb
        for y, x in np.ndindex(M, N):
            sigma = np.array([[varI[R][R][y, x], varI[R][G][y, x],
                               varI[R][B][y, x]],
                              [varI[R][G][y, x], varI[G][G][y, x],
                               varI[G][B][y, x]],
                              [varI[R][B][y, x], varI[G][B][y, x],
                               varI[B][B][y, x]]])
            cov = np.array([c[y, x] for c in covIp])
            a[y, x] = np.dot(cov, np.linalg.inv(sigma + epsilon * np.eye(3)))
        b = meanp - a[:, :, R] * meanI[R] - \
            a[:, :, G] * meanI[G] - a[:, :, B] * meanI[B]
        meanA = np.array([(BoxFilter.filter(a[:, :, channel], r)) /
                          base for channel in range(RGB)])
        meanB = BoxFilter.filter(b, r) / base

        """
        Upsample via Bilinear Interpolation
        """
        if s is not None:
            meanA = scipy.ndimage.zoom(meanA, [1, s, s], order=1)
            meanB = scipy.ndimage.zoom(meanB, [s, s], order=1)

        """
        Calculate output image q, where q = meanA. ∗ I + meanB
        """
        q = (meanA[R, :, :] * originI[:, :, R] + meanA[G, :, :] *
             originI[:, :, G] + meanA[B, :, :] * originI[:, :, B]) + meanB

        return q
