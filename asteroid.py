import pygame
import circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_white = pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        return asteroid_white
    
    def split(self):
        current_position = self.position
        current_velocity = self.velocity
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.kill()

        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            asteroid_new1 = Asteroid(current_position.x, current_position.y, new_radius)
            #asteroid_new1.velocity.rotate(current_velocity.rotate() - 40)
            asteroid_new1.velocity = current_velocity.rotate(60)
            asteroid_new2 = Asteroid(current_position.x, current_position.y, new_radius)
            #asteroid_new2.velocity.rotate(current_velocity.rotate() + 40)
            asteroid_new2.velocity = current_velocity.rotate(170)
        

    def update(self, dt):
        self.position += self.velocity * dt