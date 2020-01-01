#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dehazer import *

from PIL import Image
import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help="Input haze image path")
parser.add_argument(
    '-o', '--output', help="Output haze free image path (optional)")
args = parser.parse_args()


def main(inputPath, outputPath='./output/output.jpg'):
    inputImage = Image.open(inputPath)
    image = np.asarray(inputImage)
    dehazedImage = Dehazer.dehaze(image)
    outputImage = Image.fromarray(np.uint8(dehazedImage))
    outputImage.save(outputPath)
    print(outputPath)


if __name__ == "__main__":
    if args.input is not None:
        if args.output is not None:
            main(args.input, args.output)
        else:
            main(args.input)
    else:
        print("NoInputImageError")
