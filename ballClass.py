import pygame
from vectorClass import Vector2, rounding


class Ball(object):
    def __init__(self, radius, center_pos, color=(255, 255, 255), velocity=(0, 0)):
        self.radius = radius
        self.surf = pygame.Surface((radius * 2, radius * 2))
        self.surf.set_colorkey((0, 0, 0))
        self.position = Vector2(center_pos)
        self.rect = pygame.draw.circle(self.surf, color, (self.radius, self.radius), self.radius)
        self.velocity = Vector2(velocity)

    def __repr__(self):
        return f"POS: {int(self.position.x), int(self.position.y)}. Velocity: {int(self.velocity.x), int(self.velocity.y)}"

    def update(self):
        self.position += self.velocity

    def color_surf(self, color):
        pygame.draw.circle(self.surf, color, (self.radius, self.radius), self.radius)

    def draw(self, display):
        rounded_vec = rounding(self.position)
        self.rect.center = (rounded_vec.x, rounded_vec.y)
        display.blit(self.surf, self.rect)


class Wall:
    def __init__(self, pos, size):
        self.surf = pygame.Surface(size)
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(center=pos)

    def draw(self, display):
        display.blit(self.surf, self.rect)


