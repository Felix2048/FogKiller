#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
from PIL import Image


@staticmethod
def cv2pil(input_cv2_image):
    """
    Convert OpenCV image to PIL image

    # Arguments
      input_cv2_image: OpenCV image

    # Returns
      PIL Image
    """
    output_pil_image = Image.fromarray(
        cv2.cvtColor(input_cv2_image, cv2.COLOR_BGR2RGB))
    return output_pil_image
