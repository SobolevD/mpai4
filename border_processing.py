import numpy as np

from consts import MAX_BRIGHTNESS_VALUE, MIN_BRIGHTNESS_VALUE


def border_processing_function(element_value, border_val):
    if element_value >= border_val:
        return MAX_BRIGHTNESS_VALUE
    else:
        return MIN_BRIGHTNESS_VALUE


def border_processing(img_as_arrays, border_val):
    vector_img = np.vectorize(border_processing_function)
    new_img = vector_img(img_as_arrays, border_val)
    return new_img
