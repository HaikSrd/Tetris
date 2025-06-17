import pygame
from params import *

class Background:
    def __init__(self, screen):
        self.screen = screen
    def borders(self):
        self.screen.fill(background_color)
        for i in range(10):
            pygame.draw.line(self.screen, (50,50,50), (40*i, 0), (40*i, screen_size[1]), 4)
        for i in range(20):
            pygame.draw.line(self.screen, (50,50,50), (0,40*i), (screen_size[0], 40*i), 4)
