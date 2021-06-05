import pygame
from time import sleep
from math import radians, sin, cos, sqrt
import keyboard
import numpy as np
from numba import njit
import random

from constants import *
from screen_globals import *
from snake import *
from player import *


pygame.init()


def dryRun():
    '''
    # Dry run
    simple function for running the `@njit`ed functions
    for the first time in order to make an executable code for the "real" run
    '''
    rotate(np.zeros((2), dtype=np.float32), 0)
    normalize(np.ones((2), np.float32), 1.0)
    updateLastSteps(
        source=np.zeros((AMOUNT_OF_STEPS, 2), dtype=np.int16),
        pos=np.array((0, 0), dtype=np.float32)
    )


dryRun()
clock = pygame.time.Clock()


finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    for p in players:
        if p.isAlive:
            p.update()
            p.draw()

    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
