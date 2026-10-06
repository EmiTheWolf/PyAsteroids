from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
        self.colour = "white"

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.colour, self.position, SHOT_RADIUS, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
        