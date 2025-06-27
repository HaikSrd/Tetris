import pygame
from params import *
import numpy as np
import functions


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(screen_size)
BG = functions.Background(screen)
clock = pygame.time.Clock()
manipulation = functions.Shape

main_grid = np.zeros((21, 10))
for i in range(10):
    main_grid[20, i] = 2

game = True
while game:
    shape, color = manipulation.gen()
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

    counter = 0
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
                    block = False
                    for j in ones:
                        if main_grid[j[0], j[1] + 1] == 2:
                            block = True
                    if not block:
                        for i in range(len(ones)):
                            ones[i, 1] += 1
                elif event.key == pygame.K_LEFT:
                    block = False
                    for j in ones:
                        if main_grid[j[0], j[1] - 1] == 2:
                            block = True
                    if not block:
                        for i in range(len(ones)):
                            ones[i, 1] -= 1
                elif event.key == pygame.K_DOWN:
                    for i in range(len(ones)):
                        ones[i, 0] += 1
                elif event.key == pygame.K_UP:
                    ones, rotation_counter = manipulation.rotate(shape, rotation_counter, ones)


        for i in range(len(ones)):
            if counter % 15 == 0:
                ones[i, 0] += 1
            instance[ones[i, 0], ones[i,1]] = 1

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
        counter += 1
        clock.tick(60)
