#!/usr/bin/env python3
# coding: utf-8
"""
main.py
10-16-2020
jack skrable
"""

import math
import argparse
import string
import sys
import numpy as np
from PIL import Image, ImageEnhance



# Progress bar for cli
def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

# # read image
# im = Image.open('./images/branch.jpg')

# # convert to array
# im_arr = np.array(im)

# # convert to image
# im_new = Image.fromarray(im_arr)


def read_image(path):
    return np.array(Image.open(path))


def show_image(arr):
    print('Displaying image...')
    Image.fromarray(arr).show()


def save_image(arr, path):
    print('Saving image to {}...'.format(path))
    Image.fromarray(arr).save(path)


def color_boost(arr, color='green', scale=2):
    """
    Takes in a 3D array of RGB pixels.
    Boosts color in param by multiplying pixel value by scale.
    Reduces other colors by dividing by scale.
    Returns 3D array of RGB pixels.
    """

    color_map = {'red': [0], 'green': [1], 'blue':[2], 'yellow':[0,1], 'purple': [0,2], 'turquoise': [1,2]}
    print('Boosting {}...'.format(color))
    edit = np.copy(arr)

    # scale up colors to enhance
    for col in color_map[color]:
        edit[:,:,col] = arr[:,:,col] * scale    

    # scale down non-enhanced colors
    # for col in [i for i in range(3) if i not in color_map[color]]:
    #     edit[:,:,col] = arr[:,:,col] / scale

    return edit



def color_extract(arr, color):
    """
    Takes in a 3D array of RGB pixels.
    Extracts pixel values only of the specified color.
    Returns 3D array of RGB pixels.
    """
    color_map = {'red': 0, 'green': 1, 'blue':2}

    edit = np.copy(arr)
    edit[:,:,color_map[color]] = arr[:,:,color_map[color]]
    for color in [k for k in color_map if k not in color]:
        edit[:,:,color_map[color]] = 0

    return edit


def gamma_compression(arr):
    """
    Takes in a 3D array of RGB pixels.
    Using linear approximation of gamma compression, converts
    to grayscale. Sums the linear equation, makes RGB equal to the sum.
    Returns 3D array of RGB pixels.
    """
    print('Converting to grayscale...')
    edit = np.copy(arr)
    edit[:,:,0] = arr[:,:,0] * 0.299
    edit[:,:,1] = arr[:,:,1] * 0.587
    edit[:,:,2] = arr[:,:,2] * 0.114
    gray = np.expand_dims(edit.sum(axis=2), axis=2)
    final = np.uint8(np.append(gray, np.append(gray, gray, 2), 2))
    return final


def only_one(arr, color='green'):
    """
    Takes in a 3D array of RGB pixels.
    Converts pixels to grayscale using gamma_compression.
    Replaces grayscale with original pixel value for specified color.
    Returns 3D array of pixels.
    """
    # color_map = {'red': 0, 'green': 1, 'blue':2}
    color_map = {'red': [0], 'green': [1], 'blue':[2], 'yellow':[0,1], 'purple': [0,2], 'turquoise': [1,2]}
    edit = gamma_compression(arr)
    for col in color_map[color]:
        edit[:,:,color_map[color]] = arr[:,:,color_map[color]]
    return edit


def saturate(arr, scale=2.0):
    """
    Takes in a 3D array of RGB pixels.
    Converts array to PIL object. Creates a saturation object.
    Saturates the image by factor of scale. Converts back to array of pixels.
    Returns 3D array of pixels.
    """
    im = Image.fromarray(arr)
    sat = ImageEnhance.Color(im)
    edit = np.array(sat.enhance(scale))
    return edit



def composite(base, mod, threshold):

    first = read_image('./first.jpg')
    second = read_image('./second-1.jpg')

    output = first.copy()

    size = first.shape[0]


    # keeps mostly _second right now
    for i, row in enumerate(first):
        progress(i+1, size, 'of image processing complete')
        for ii, pixel in enumerate(row):
            for iii, px in enumerate(pixel):
                if abs(int(px) - (second[i][ii][iii])) > 25:
                    output[i][ii][iii] = second[i][ii][iii]


# MAIN
###########################################################################
grafitti = read_image('./images/grafitti.jpg')
subway = read_image('./images/subway.jpg')
branch = read_image('./images/branch.jpg')
hotel = read_image('./images/hotel.jpg')
leaf = read_image('./images/leaf.jpg')
sign = read_image('./images/sign.jpg')



"""
turn into class for easy access?
Need points between 6 main colors on map.
Need some edge blending??
"""