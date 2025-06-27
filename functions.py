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
            0: cross_color,
            1: lightning_color,
            2: l_color,
            3: square_color,
            4: line_color
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
            pygame.draw.line(self.screen, border_color, (40*i, 0), (40*i, screen_size[1]), 4)
        for i in range(20):
            pygame.draw.line(self.screen, border_color, (0,40*i), (screen_size[0] - border_size, 40*i), 4)
        pygame.draw.line(self.screen, border_color, (screen_size[0] - border_size, 0), (screen_size[0] - border_size, screen_size[1]), 6)

        #need to make a 4*4 block that shows the next piece
    def next_block(self):
        left = screen_size[0] - (border_size/2) - 2*block_size
        right = screen_size[0] - (border_size/2) + 2*block_size
        bottom = next_block_top + 4*block_size
        size = 4*block_size
        pygame.draw.rect(self.screen,border_color, pygame.Rect(left - 10, next_block_top - 10, size + 23, size + 23), width = 6)



    def draw_next_block(self, next_block):
        shape = ones_gen(next_block)
        shape = shape.astype('float64')
        shape[:,1] -= 3.0
        colors = {
            0: cross_color,
            1: lightning_color,
            2: l_color,
            3: square_color,
            4: line_color
        }
        left = screen_size[0] - (border_size / 2) - 2 * block_size

        if next_block == "square":
            shape[:,0] += 1
            color = colors[3]
        elif next_block == "lightning":
            shape[:, 0] += 0.5
            color = colors[1]
        elif next_block == "cross":
            shape[:, 0] += 1
            shape[:, 1] += 0.5
            color = colors[0]
        elif next_block == "l":
            shape[:, 0] += 0.5
            color = colors[2]
        elif next_block == "line":
            shape[:, 1] += 0.5
            color = colors[4]

        for i in shape:
            pygame.draw.rect(self.screen, color,
                             (left + i[1] * block_size, next_block_top + i[0] * block_size, block_size, block_size),
                             border_radius=5)
            pygame.draw.rect(self.screen, np.array(color) - 50,
                             (left + i[1] * block_size + 4, next_block_top + i[0] * block_size + 4, block_size - 8,
                              block_size - 8), border_radius=5)