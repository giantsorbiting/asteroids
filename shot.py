import pygame
from constants import *
from circleshape import CircleShape
class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)  # Transparent surface
        pygame.draw.circle(self.image, "white", (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)  # Draw the circle onto the image
        self.rect = self.image.get_rect(center=(position.x, position.y))
        self.velocity = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(position.x, position.y)
    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (int(self.position.x), int(self.position.y))
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)