import pygame
from pygame.locals import *


class MainView(object):
    def __init__(self, settings):
        self._screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        # Load Game Background
        self._background = pygame.image.load(settings.BACKGROUND_IMAGE)

    @property
    def screen(self):
        return self._screen

    @property
    def background(self):
        return self._background
