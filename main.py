import pygame
import sys
from circleshape import *
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.asteroids_group = asteroids
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if shot.check_collision(asteroid):
                    print(f"Shot at ({shot.position.x}, {shot.position.y}) destroyed asteroid at ({asteroid.position.x}, {asteroid.position.y})")
                    shot.kill()
                    asteroid.split()   
        for drawable in drawables:
            drawable.draw(screen) 
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()