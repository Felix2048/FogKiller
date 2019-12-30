#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


class BoxFilter:

    @staticmethod
    def filter(inputImage, radius):
        """
        Get the transmission t of the RGB image data from a numpy array

        # Arguments

        - inputImage:   M * N numpy array of a gray image data
                        normalized to [0.0, 1.0]

        - radius:   square window of a radius radius (integer)

        # Returns

        - M * N numpy array of the filtered input image

        """

        M, N = inputImage.shape
        output = np.zeros_like(inputImage)

        sumY = np.cumsum(inputImage, axis=0)
        output[:radius + 1] = sumY[radius: 2 * radius + 1]
        output[radius + 1:M - radius] = sumY[2 *
                                             radius + 1:] - sumY[:M - 2 * radius - 1]
        output[-radius:] = np.tile(sumY[-1], (radius, 1)) - \
            sumY[M - 2 * radius - 1:M - radius - 1]

        sumX = np.cumsum(output, axis=1)
        output[:, :radius + 1] = sumX[:, radius:2 * radius + 1]
        output[:, radius + 1:N - radius] = sumX[:, 2 *
                                                radius + 1:] - sumX[:, :N - 2 * radius - 1]
        output[:, -radius:] = np.tile(sumX[:, -1][:, None], (1, radius)) - \
            sumX[:, N - 2 * radius - 1:N - radius - 1]

        return output
