import numpy as np


def linear_contrast_function(img, fmin, fmax):
    if img < fmin:
        img = 0
    elif img > fmax:
        img = 255
    else:
        img = (255*img - 255*fmin)/(fmax-fmin)
    return img


def linear_contrast(img, fmax):
    fmin = img.min()
    lin = np.vectorize(linear_contrast_function)
    contrast_img = lin(img, fmin, fmax)
    return contrast_img
