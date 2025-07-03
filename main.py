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
first_turn = True
next_shape = 0
next_color = []
lines_cleared = 0
score = 0
while game:
    in_loop_clear = 0
    shape, color = next_shape, next_color
    if first_turn:
        shape, color = manipulation.gen()
        first_turn = False

    next_shape, next_color = manipulation.gen()

    ones = functions.ones_gen(shape)
    for i in ones:
        if main_grid[i[0],i[1]] == 2:
            main_grid = np.zeros((21, 10))
            for i in range(10):
                main_grid[20, i] = 2
            lines_cleared += 1
            in_loop_clear += 1

    rotation_counter = 0
    for i in range(20):
        clear = True
        for j in range(10):
            if main_grid[i, j] == 0:
                clear = False
        if clear:
            main_grid = np.delete(main_grid, i, axis=0)
            main_grid = np.vstack([np.zeros((1,10)), main_grid])
            lines_cleared += 1
            in_loop_clear += 1

    if in_loop_clear == 1:
        score += 40
    elif in_loop_clear == 2:
        score += 100
    elif in_loop_clear == 3:
        score += 300
    elif in_loop_clear == 4:
        score += 1200

    counter = 0
    running = True
    while running:
        space = False
        instance = np.copy(main_grid)

        BG.borders()
        BG.draw_next_block(next_shape)
        BG.scroing_system(lines_cleared, score)
        BG.next_block()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game = False
                elif event.key == pygame.K_RIGHT:
                    if np.max(ones[:,-1]) != 9:
                        block = False
                        for j in ones:
                            if main_grid[j[0], j[1] + 1] == 2:
                                block = True
                        if not block:
                            for i in range(len(ones)):
                                ones[i, 1] += 1
                elif event.key == pygame.K_LEFT:
                    if np.min(ones[:,-1]) != 0:
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
                    one_two = np.copy(ones)
                    new_ones, new_rotation_counter = manipulation.rotate(shape, rotation_counter, ones)
                    if np.max(new_ones[:,-1]) <= 9 and np.min(new_ones[:,-1] >= 0):
                        ones = new_ones
                        rotation_counter = new_rotation_counter
                    else:
                        ones = one_two
                elif event.key == pygame.K_SPACE: # gotto add the space button that brings the blok all the way down at once
                    pass


        for i in range(len(ones)):
            if counter % 15 == 0 and counter != 0:
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
