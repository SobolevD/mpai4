from cmath import sqrt

import numpy as np


def correlate(img, model):
    t = np.array(model) * 1/np.sum(np.square(model))
    new_img = list(img.copy().astype(float))
    mean_val = np.mean(new_img)
    size = np.shape(new_img)
    help_array = np.array(np.ones(len(new_img[0]))*mean_val)
    new_img.insert(0, help_array)
    new_img.append(help_array)
    for i in range(0, size[0] + 2, 1):
        new_img[i] = list(new_img[i])
        new_img[i].insert(0, mean_val)
        new_img[i].append(mean_val)
    new_img = np.array(new_img)
    reserve_img = img.copy().astype(float)

    for i in range(1, size[0] + 1, 1):
        for j in range(1, size[1] + 1, 1):
            x = new_img[i-1:i+2, j-1:j+2]  # mask 3x3
            sum_of_sqr = 0
            for row in x:
                for el in row:
                    sum_of_sqr += el*el
            if sum_of_sqr == 0:
                sum_of_sqr = 1
            b_correlation_function = 0
            for k in range(0, len(x), 1):
                for l in range(0, len(x[0]), 1):
                    b_correlation_function += x[k][l] * t[k][l]
            b_correlation_function /= sqrt(sum_of_sqr)
            reserve_img[i-1][j-1] = int(b_correlation_function*255)
    return reserve_img
