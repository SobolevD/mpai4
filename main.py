from math import sqrt

import numpy as np
from skimage.io import show

from border_processing import border_processing
from consts import IMAGE_HEIGHT, IMAGE_LENGTH, MODEL_T, MODEL_INVERSE_T, WHITE_NOISE_PARAMETER, WHITE_NOISE_MORE_PARAMETER
from correlator import correlate
from helpers import check_and_correct_limits, create_random_objects
from histogram import create_figure, create_fields_figure
from linear_constrast import linear_contrast


def GET_AVERAGE_DISPERSION(img1, img2):
    img1_dispersion = np.var(img1)
    img2_dispersion = np.var(img2)
    return (img1_dispersion + img2_dispersion) / 2


def get_img_with_T():
    return create_random_objects(IMAGE_HEIGHT, IMAGE_LENGTH, MODEL_T, objects_count)


def get_img_with_both_objects_types():
    img_with_T_random1 = create_random_objects(IMAGE_HEIGHT, IMAGE_LENGTH, MODEL_T, objects_count)
    img_with_inverse_T_random1 = create_random_objects(IMAGE_HEIGHT, IMAGE_LENGTH, MODEL_INVERSE_T, objects_count)
    return (img_with_T_random1 + img_with_inverse_T_random1) / 2


def create_white_noise_with_correction(dispersion, coefficient):
    white_noise = np.random.normal(loc=0, scale=float(sqrt(dispersion / coefficient)),
                     size=(IMAGE_HEIGHT, IMAGE_LENGTH)).astype(int)
    corrective = np.abs(white_noise.min())
    return check_and_correct_limits(white_noise + corrective)


if __name__ == '__main__':

    # 1. Create objects
    # ==================================================================
    objects_count = 10

    img_with_objects_T = get_img_with_T()
    img_with_T_and_inverse_T_random = get_img_with_both_objects_types()
    # ==================================================================

    # 2. Create white noises
    # ==================================================================
    avg_dispersion = GET_AVERAGE_DISPERSION(img_with_objects_T, img_with_T_and_inverse_T_random)

    white_noise = create_white_noise_with_correction(avg_dispersion, WHITE_NOISE_PARAMETER)
    white_noise_more = create_white_noise_with_correction(avg_dispersion, WHITE_NOISE_MORE_PARAMETER)
    # ==================================================================

    # 3. Noise overlay
    # ==================================================================
    noised_img_with_T = check_and_correct_limits(img_with_objects_T + white_noise_more)
    noised_img_with_both_object_types = check_and_correct_limits(img_with_T_and_inverse_T_random + white_noise)
    # ==================================================================

    # 4. Show images with objects and objects in noise
    # ==================================================================
    create_figure(white_noise_more, white_noise, img_with_objects_T, img_with_T_and_inverse_T_random)
    show()
    create_figure(white_noise_more, white_noise, noised_img_with_T, noised_img_with_both_object_types)
    show()
    # ==================================================================

    # 5. Make correlate
    # ==================================================================
    correlate_field_T_model1 = correlate(img_with_objects_T, MODEL_T)
    correlate_field_TandL_model1 = correlate(img_with_T_and_inverse_T_random, MODEL_T)
    correlate_field_TandL_model2 = correlate(img_with_T_and_inverse_T_random, MODEL_INVERSE_T)

    correlate_field_noise_T_model1 = correlate(noised_img_with_T, MODEL_T)
    correlate_field_noise_both_object_types_model1 = correlate(noised_img_with_both_object_types, MODEL_T)
    correlate_field_noise_both_object_types_model2 = correlate(noised_img_with_both_object_types, MODEL_INVERSE_T)
    # ==================================================================

    # 6. Make contrast
    # ==================================================================
    max_in_T = correlate_field_T_model1.max()
    max_in_L = correlate_field_TandL_model2.max()

    contrast1 = linear_contrast(correlate_field_T_model1, max_in_T)
    contrast2 = linear_contrast(correlate_field_TandL_model1, max_in_T)
    contrast3 = linear_contrast(correlate_field_TandL_model2, max_in_T)

    noise_contrast1 = linear_contrast(correlate_field_noise_T_model1, max_in_T)
    noise_contrast2 = linear_contrast(correlate_field_noise_both_object_types_model1, max_in_T)
    noise_contrast3 = linear_contrast(correlate_field_noise_both_object_types_model2, max_in_T)
    # ==================================================================

    # 7. Borders processing
    # ==================================================================
    border1 = border_processing(contrast1, 180)
    border2 = border_processing(contrast2, 150)
    border3 = border_processing(contrast3, 150)

    noise_border1 = border_processing(noise_contrast1, 210)
    noise_border2 = border_processing(noise_contrast2, 170)
    noise_border3 = border_processing(noise_contrast3, 170)
    # ==================================================================

    # 8. Show result images
    # ==================================================================

    create_fields_figure(img_with_objects_T,
                         correlate_field_T_model1,
                         border1,
                         noised_img_with_T,
                         correlate_field_noise_T_model1,
                         noise_border1,
                         'model T')
    show()
    create_fields_figure(img_with_T_and_inverse_T_random,
                         correlate_field_TandL_model1,
                         border2,
                         noised_img_with_both_object_types,
                         correlate_field_noise_both_object_types_model1,
                         noise_border2,
                         'model T')
    show()
    create_fields_figure(img_with_T_and_inverse_T_random,
                         correlate_field_TandL_model2,
                         border3,
                         noised_img_with_both_object_types,
                         correlate_field_noise_both_object_types_model2,
                         noise_border3,
                         'model inverse T')
    show()


