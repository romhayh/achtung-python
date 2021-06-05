import pygame
import numpy as np

from constants import *

screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill(DARKGREY)
pygame.display.flip()
pygame.display.set_caption("Achtung")


grid = np.zeros(
    shape=(WINDOW_WIDTH, WINDOW_HEIGHT),

    # u for unsigned
    # int is the data type
    # 8 is the number of bits
    dtype=np.int8
)
