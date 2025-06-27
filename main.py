import pygame
from background import Background
from params import *
import numpy as np
import functions


pygame.init()

screen = pygame.display.set_mode(screen_size)
BG = Background(screen)
clock = pygame.time.Clock()

main_grid = np.zeros((21, 10))
for i in range(10):
    main_grid[20, i] = 2

game = True
while game:
    shape, color = functions.shape_gen()
    ones = functions.ones_gen(shape)
    rotation_counter = 0

    for i in range(20):
        clear = True
        for j in range(10):
            if main_grid[i, j] == 0:
                clear = False
        if clear:
            main_grid = np.delete(main_grid, i, axis=0)
            main_grid = np.vstack([np.zeros((1,10)), main_grid])

    running = True
    while running:
        instance = np.copy(main_grid)
        BG.borders()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game = False
                elif event.key == pygame.K_RIGHT:
                    for i in range(len(ones)):
                        ones[i, 1] += 1
                elif event.key == pygame.K_LEFT:
                    for i in range(len(ones)):
                        ones[i, 1] -= 1
                elif event.key == pygame.K_DOWN:
                    for i in range(len(ones)):
                        ones[i, 0] += 1
                elif event.key == pygame.K_UP:
                    if shape == 'l':
                        if rotation_counter == 0:
                            ones[1] += [1, 1]
                            ones[2] += [-1, -1]
                            ones[3] += [0, -2]
                            rotation_counter += 1
                        elif rotation_counter == 1:
                            ones[1] += [1, -1]
                            ones[2] += [-1, +1]
                            ones[3] += [-2, 0]
                            rotation_counter += 1
                        elif rotation_counter == 2:
                            ones[1] += [-1, -1]
                            ones[2] += [+1, +1]
                            ones[3] += [0, 2]
                            rotation_counter += 1
                        elif rotation_counter == 3:
                            ones[1] += [-1, +1]
                            ones[2] += [+1, -1]
                            ones[3] += [2, 0]
                            rotation_counter = 0
                    elif shape == 'cross':
                        if rotation_counter == 0:
                            ones[0] += [1, 1]
                            rotation_counter += 1
                        elif rotation_counter == 1:
                            ones[3] += [+1, -1]
                            rotation_counter += 1
                        elif rotation_counter == 2:
                            ones[2] += [-1, -1]
                            rotation_counter += 1
                        elif rotation_counter == 3:
                            ones[0] += [-1, -1]
                            ones[2] += [1, 1]
                            ones[3] += [-1, 1]
                            rotation_counter = 0
                    elif shape == 'line':
                        if rotation_counter == 0:
                            ones[0] += [1, 0]
                            ones[1] += [+2, 1]
                            ones[2] += [0, -1]
                            ones[3] += [-1, -2]
                            rotation_counter += 1
                        elif rotation_counter == 1:
                            ones[0] += [0, -1]
                            ones[1] += [1, -2]
                            ones[2] += [-1, 0]
                            ones[3] += [-2, 1]
                            rotation_counter += 1
                        elif rotation_counter == 2:
                            ones[0] += [-1, 0]
                            ones[1] += [-2, -1]
                            ones[2] += [0, 1]
                            ones[3] += [1, 2]
                            rotation_counter += 1
                        elif rotation_counter == 3:
                            ones[0] += [0, 1]
                            ones[1] += [-1, 2]
                            ones[2] += [1, 0]
                            ones[3] += [2, -1]
                            rotation_counter = 0
                    elif shape == 'lightning':
                        if rotation_counter == 0:
                            ones[0] += [1, -1]
                            ones[1] += [1, 1]
                            ones[2] += [0, -2]
                            rotation_counter += 1
                        elif rotation_counter == 1:
                            ones[0] += [-1, -1]
                            ones[1] += [1, -1]
                            ones[2] += [-2, 0]
                            rotation_counter += 1
                        elif rotation_counter == 2:
                            ones[0] += [-1, 1]
                            ones[1] += [-1, -1]
                            ones[2] += [0, 2]
                            rotation_counter += 1
                        elif rotation_counter == 3:
                            ones[0] += [1, 1]
                            ones[1] += [-1, 1]
                            ones[2] += [2, 0]
                            rotation_counter = 0

        for i in ones:
            instance[i[0], i[1]] = 1

        #drawing the shape on the screen
        for i in range(20):
            for j in range(10):
                if instance[i,j] == 1:
                    functions.initial(screen, (j,i), color)
                elif instance[i,j] == 2:
                    functions.initial(screen, (j,i), (255,255,255))


        for i in ones:
            if main_grid[i[0] + 1, i[1]] == 2:
                for j in ones:
                    main_grid[j[0], j[1]] = 2
                running = False

        pygame.display.update()

