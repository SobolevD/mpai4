from matplotlib import pyplot as plt
from skimage.io import imshow


def create_figure(noise1, noise2, img_with_T, img_with_TandL):
    fig = plt.figure(figsize=(20, 10))
    fig.add_subplot(2, 2, 1)
    plt.title("Noise image for T-object")
    imshow(noise1, cmap='gray')  # , vmin=0, vmax=255
    fig.add_subplot(2, 2, 2)
    plt.title("Noise image for T & Inverse T-object")
    imshow(noise2, cmap='gray')  # , vmin=0, vmax=255
    fig.add_subplot(2, 2, 3)
    plt.title("T-object image")
    imshow(img_with_T, cmap='gray', vmin=0, vmax=255)
    fig.add_subplot(2, 2, 4)
    plt.title("T & Inverse T-object image")
    imshow(img_with_TandL, cmap='gray', vmin=0, vmax=255)
    return fig


def create_fields_figure(img_with_objects, correlate_field_objects, bordered_img_of_field_objects, noise_img_with_objects,
                         correlate_field_noise_objects, bordered_img_of_field_noise_objects, model_name):
    fig = plt.figure(figsize=(20, 10))
    fig.add_subplot(2, 3, 1)
    plt.title("objects without noise")
    imshow(img_with_objects, cmap='gray', vmin=0, vmax=255)
    fig.add_subplot(2, 3, 2)
    plt.title(f"Correlated field of objects with {model_name}")
    imshow(correlate_field_objects, cmap='gray') # , vmin=0, vmax=255
    fig.add_subplot(2, 3, 3)
    plt.title("Bordered processing correlated field of objects")
    imshow(bordered_img_of_field_objects, cmap='gray', vmin=0, vmax=255)
    fig.add_subplot(2, 3, 4)
    plt.title("objects with noise")
    imshow(noise_img_with_objects, cmap='gray', vmin=0, vmax=255)
    fig.add_subplot(2, 3, 5)
    plt.title(f"Correlated field of objects with {model_name}")
    imshow(correlate_field_noise_objects, cmap='gray') # , vmin=0, vmax=255
    fig.add_subplot(2, 3, 6)
    plt.title("Bordered processing correlated field of objects")
    imshow(bordered_img_of_field_noise_objects, cmap='gray', vmin=0, vmax=255)
    return fig
