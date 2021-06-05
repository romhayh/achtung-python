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

class Player(Snake):
    
    def __init__(self, color, x, y, sid, left, right):
        super().__init__(color, x, y, sid)
        self.left = left
        self.right = right
        
    def update_velocity(self):
        if keyboard.is_pressed(self.left):
            self.angle = BETA
        elif keyboard.is_pressed(self.right):
            self.angle = -BETA
        else:
            self.angle = 0
        # rotate and normalize
        super().update_velocity()
        
snake1 = Player(COLORS_ARRAY[1], WINDOW_WIDTH / 8, WINDOW_HEIGHT / 8, 1, 'A', 'D')
snake2 = Player(COLORS_ARRAY[2], WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, 2, 'LEFT', 'RIGHT')
snake3 = Player(COLORS_ARRAY[3], WINDOW_WIDTH / 3, WINDOW_HEIGHT / 3, 3, 'M', 'N')
players = [snake1,snake2, snake3]
