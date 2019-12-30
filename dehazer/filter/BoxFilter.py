#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


class BoxFilter:

    @staticmethod
    def filter(p, r=40):
        """
        Get the box filtered RGB image data from a numpy array

        # Arguments

        - p(InputImage):   M * N numpy array of a gray image data
                        normalized to [0.0, 1.0]

        - r:   square window of a radius r (integer)

        # Returns

        - M * N numpy array of the filtered output image

        """

        M, N = p.shape
        r = min(r, int(M / 2 - 1), int(N / 2 - 1))
        output = np.zeros_like(p)

        sumY = np.cumsum(p, axis=0)
        output[:r + 1] = sumY[r: 2 * r + 1]
        output[r + 1:M - r] = sumY[2 *
                                   r + 1:] - sumY[:M - 2 * r - 1]
        output[-r:] = np.tile(sumY[-1], (r, 1)) - \
            sumY[M - 2 * r - 1:M - r - 1]

        sumX = np.cumsum(output, axis=1)
        output[:, :r + 1] = sumX[:, r:2 * r + 1]
        output[:, r + 1:N - r] = sumX[:, 2 *
                                      r + 1:] - sumX[:, :N - 2 * r - 1]
        output[:, -r:] = np.tile(sumX[:, -1][:, None], (1, r)) - \
            sumX[:, N - 2 * r - 1:N - r - 1]

        return output
