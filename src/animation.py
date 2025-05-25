import pygame

class Ball:
    def __init__(self, screen_size, ball_size):
        self.screen_size = screen_size
        self.ball_size = ball_size
        self.ball_position = [screen_size[0]//2, screen_size[1]//2]
        self.ball_velocity = [0, 0]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.ball_position, self.ball_size)
        pygame.draw.circle(screen, (255, 0, 0), self.ball_position, self.ball_size-2)

    def moove(self):
        self.ball_position[0] += self.ball_velocity[0]
        self.ball_position[1] += self.ball_velocity[1]


class Circle:
    def __init__ (self, screen_size, circle_radius):
        self.screen_size = screen_size
        self.circle_radius = circle_radius
        self.circle_position = [screen_size[0]//2, screen_size[1]//2]
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.circle_position, self.circle_radius)
        pygame.draw.circle(screen, (0, 0, 0), self.circle_position, self.circle_radius-6)