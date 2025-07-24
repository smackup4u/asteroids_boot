import pygame
import circleshape

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_white = pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        return asteroid_white

    def update(self, dt):
        self.position += self.velocity * dt