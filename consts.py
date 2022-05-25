import numpy as np

MAX_BRIGHTNESS_VALUE = 255
MIN_BRIGHTNESS_VALUE = 0
IMAGE_HEIGHT = 64
IMAGE_LENGTH = 64

WHITE_NOISE_MORE_PARAMETER = 0.1
WHITE_NOISE_PARAMETER = 0.25

MODEL_T = np.array([[1, 1, 1],
                    [0, 1, 0],
                    [0, 1, 0]])

MODEL_INVERSE_T = np.array([[0, 1, 0],
                            [0, 1, 0],
                            [1, 1, 1]])
