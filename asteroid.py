import pygame
import random
from constants import *
from circleshape import *
class Asteroid(CircleShape):
    asteroids_group = None
    def __init__(self, position, radius):
        super().__init__(position.x, position.y, radius)  # CircleShape still needs x,y
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.asteroids = pygame.sprite.Group()
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position.xy, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.x = self.position.x
        self.y = self.position.y
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.uniform(20, 50)
        first_new_vector = self.velocity.rotate(random_angle)
        second_new_vector = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
        first_new_asteroid = Asteroid(pygame.Vector2(self.position), new_radius)
        second_new_asteroid = Asteroid(pygame.Vector2(self.position), new_radius)
    
        first_new_asteroid.velocity = first_new_vector * 1.2
        second_new_asteroid.velocity = second_new_vector * 1.2
    
        Asteroid.asteroids_group.add(first_new_asteroid, second_new_asteroid)
        self.kill()