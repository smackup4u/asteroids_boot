import circleshape
import pygame
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    
    def draw(self, screen):
        shot_white = pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 1)
        return shot_white

    def update(self, dt):
        self.position += self.velocity * dt
