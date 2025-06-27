import numpy as np
import pygame
from params import *

# initial takes coordinates and draws a block in there like (1,1)
def initial(screen, cords, color):
    x, y = cords[0]*40, cords[1]*40
    pygame.draw.rect(screen, color, [x, y, block_size,block_size], border_radius=5)
    pygame.draw.rect(screen, [color[0] - 50, color[1] - 50, color[2] - 50], [x + 4, y + 4, block_size - 8,block_size - 8], border_radius=5)

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

class Shape:
    @staticmethod
    def gen():
        shapes = {
            0: 'cross',
            1: 'lightning',
            2: 'l',
            3: 'square',
            4: 'line'
        }
        colors = {
            0: [174, 230, 189],
            1: [70, 201, 60],
            2: [60, 93, 201],
            3: [92, 105, 125],
            4: [184, 51, 76]
        }
        random_num = np.random.randint(5)
        return shapes[random_num], colors[random_num]

    @staticmethod
    def rotate(shape, rotation_counter, ones):
        if shape == 'l':
            if rotation_counter == 0:
                ones[1] += [1, 1]
                ones[2] += [-1, -1]
                ones[3] += [0, -2]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 1:
                ones[1] += [1, -1]
                ones[2] += [-1, +1]
                ones[3] += [-2, 0]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 2:
                ones[1] += [-1, -1]
                ones[2] += [+1, +1]
                ones[3] += [0, 2]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 3:
                ones[1] += [-1, +1]
                ones[2] += [+1, -1]
                ones[3] += [2, 0]
                rotation_counter = 0
                return ones, rotation_counter
        elif shape == 'cross':
            if rotation_counter == 0:
                ones[0] += [1, 1]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 1:
                ones[3] += [+1, -1]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 2:
                ones[2] += [-1, -1]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 3:
                ones[0] += [-1, -1]
                ones[2] += [1, 1]
                ones[3] += [-1, 1]
                rotation_counter = 0
                return ones, rotation_counter
        elif shape == 'line':
            if rotation_counter == 0:
                ones[0] += [1, 0]
                ones[1] += [+2, 1]
                ones[2] += [0, -1]
                ones[3] += [-1, -2]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 1:
                ones[0] += [0, -1]
                ones[1] += [1, -2]
                ones[2] += [-1, 0]
                ones[3] += [-2, 1]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 2:
                ones[0] += [-1, 0]
                ones[1] += [-2, -1]
                ones[2] += [0, 1]
                ones[3] += [1, 2]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 3:
                ones[0] += [0, 1]
                ones[1] += [-1, 2]
                ones[2] += [1, 0]
                ones[3] += [2, -1]
                rotation_counter = 0
                return ones, rotation_counter
        elif shape == 'lightning':
            if rotation_counter == 0:
                ones[0] += [1, -1]
                ones[1] += [1, 1]
                ones[2] += [0, -2]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 1:
                ones[0] += [-1, -1]
                ones[1] += [1, -1]
                ones[2] += [-2, 0]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 2:
                ones[0] += [-1, 1]
                ones[1] += [-1, -1]
                ones[2] += [0, 2]
                rotation_counter += 1
                return ones, rotation_counter
            elif rotation_counter == 3:
                ones[0] += [1, 1]
                ones[1] += [-1, 1]
                ones[2] += [2, 0]
                rotation_counter = 0
                return ones, rotation_counter
        elif shape == "square":
            return ones, rotation_counter

class Background:
    def __init__(self, screen):
        self.screen = screen
    def borders(self):
        self.screen.fill(background_color)
        for i in range(10):
            pygame.draw.line(self.screen, (50,50,50), (40*i, 0), (40*i, screen_size[1]), 4)
        for i in range(20):
            pygame.draw.line(self.screen, (50,50,50), (0,40*i), (screen_size[0], 40*i), 4)

