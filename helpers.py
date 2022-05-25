import numpy as np
import random
from scipy import signal

from consts import MIN_BRIGHTNESS_VALUE, MAX_BRIGHTNESS_VALUE


def correct_limits_function(element_value):
    if element_value < MIN_BRIGHTNESS_VALUE:
        return MIN_BRIGHTNESS_VALUE
    if element_value > MAX_BRIGHTNESS_VALUE:
        return MAX_BRIGHTNESS_VALUE
    return element_value


def check_and_correct_limits(img_as_arrays):
    vector_img = np.vectorize(correct_limits_function)
    new_img = vector_img(img_as_arrays)
    return new_img


def create_random_objects(height_img, width_img, object_model, number_of_objects):
    img = np.zeros((height_img, width_img))
    for k in range(0, number_of_objects):
        i = random.randint(0, 63)
        j = random.randint(0, 63)
        img[i][j] = 64
    img = signal.convolve2d(img, object_model, boundary="symm", mode="same")
    img = img + 96
    return img

