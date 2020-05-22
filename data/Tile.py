import pygame
from data.GLOBALS import *

class Tile:
    def __init__(self, screen, color, location):
        self.screen = screen
        self.color = color
        self.location = location
        self.width = TILE_SIZE
        self.height = TILE_SIZE

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.location[0], self.location[1], self.width, self.height))

    def move(self, new_location):
        self.location = new_location

    def get_tile_cords(self):
        x = self.location[0]
        y = self.location[1]

        x /= 20
        y /= 20

        return x, y