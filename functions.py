import numpy as np
import pygame
from params import *
# initial takes coordinates and draws a block in there like (1,1)
def initial(screen, top_left, color = 255):
    x, y = top_left[0]*40, top_left[1]*40
    pygame.draw.rect(screen, (color, color, color), [x, y, block_size,block_size], border_radius=5)
    pygame.draw.rect(screen, (color - 50, color - 50, color - 50), [x + 4, y + 4, block_size - 8,block_size - 8], border_radius=5)

#gives us shapes
def shape_gen():
    shapes = {
        0: 'cross',
        1: 'lightning',
        2: 'l',
        3: 'square',
        4: 'line'
    }
    return shapes[np.random.randint(5)]

#generating ones
def ones_gen(shape):
    if shape == 'cross':
        return np.array([[1, 3], [1, 4], [1, 5], [0, 4]])
    elif shape == 'lightning':
        return np.array([[1, 5], [0, 4], [2, 5], [1, 4]])
    elif shape == 'l':
        return np.array([[1, 4], [0, 4], [2, 4], [2, 5]])
    elif shape == 'square':
        return np.array([[0, 5], [0, 4], [1, 5], [1, 4]])
    elif shape == 'line':
        return np.array([[1, 4], [0, 4], [2, 4], [3, 4]])