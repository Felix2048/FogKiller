#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np


@staticmethod
def cv2pil(input_pil_image):
    """
    Convert PIL image to OpenCV image

    # Arguments
      input_pil_image: PIL Image

    # Returns
      OpenCV image
    """
    output_cv2_image = cv2.cvtColor(
        np.asarray(input_pil_image), cv2.COLOR_RGB2BGR)
    return output_cv2_image
