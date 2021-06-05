import numpy as np

# colors
DARKGREY = (59, 59, 64)
HEAD_COLOR = (254, 255, 1)

# color array for the snakes:
COLORS_ARRAY = np.array([
    DARKGREY,
    [255, 0, 0],
    [0, 255, 0],
    [128, 0, 128]
])

WINDOW_WIDTH: np.int16 = 1080
WINDOW_HEIGHT: np.int16 = 900
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

RADIUS: np.int16 = 5

HORIZONTAL_VELOCITY: np.int16 = 3
VERTICAL_VELOCITY: np.int16 = 100
BETA: np.float32 = np.deg2rad(10)
SPEED = 4.5
DRAW_SAFETY_CONST = 2


FPS = 60
AMOUNT_OF_STEPS = 5