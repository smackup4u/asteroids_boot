import pygame
from constants import *
import player
import asteroid
import asteroidfield



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Init pygame and creating containers
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    game_clock = pygame.time.Clock()
    dt = 0
    #container definition for classes (Player, Asteroid, asteroidfield)
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player_char = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()
    # Gameloop (you can end the programm either by closing the game window or Ctrl+C in the commandline)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(0)
        dt = game_clock.tick(60) / 1000
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        # player_char.draw(screen)
        pygame.display.flip()
        



if __name__ == "__main__":
    main()
