import pygame
from constants import *
import player
import asteroid
import asteroidfield
import sys
import shot



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Init pygame and creating containers
    
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    game_clock = pygame.time.Clock()
    dt = 0
    #container definition for classes (Player, Asteroid, asteroidfield)
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, drawable, updatable)
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
        
        for ast_thing in asteroids:
            if player_char.check_collisions(ast_thing) == True:
                sys.exit()
            for shot_p in shots:
                if shot_p.check_collisions(ast_thing) == True:
                    ast_thing.split()
                    shot_p.kill()
        
        
        # player_char.draw(screen)
        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
