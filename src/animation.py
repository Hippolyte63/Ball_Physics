import pygame

class Ball:
    def __init__(self, screen_size, ball_radius):
        self.screen_size = screen_size
        self.ball_radius = ball_radius
        self.ball_position = [screen_size[0]//2, screen_size[1]//2]
        self.ball_velocity = [0, 0]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.ball_position, self.ball_radius)
        pygame.draw.circle(screen, (255, 0, 0), self.ball_position, self.ball_radius-2)

    def moove(self):
        for i in range(2):

            # Uptade ball position with velocity
            self.ball_position[i] += self.ball_velocity[i]

            # Bounce off walls
            if self.ball_position[i] <= self.ball_radius or self.ball_position[i] >= self.screen_size[i] - self.ball_radius:
                self.ball_velocity[i] *= -1






class Circle:
    def __init__ (self, screen_size, circle_radius):
        self.screen_size = screen_size
        self.circle_radius = circle_radius
        self.circle_position = [screen_size[0]//2, screen_size[1]//2]
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.circle_position, self.circle_radius)
        pygame.draw.circle(screen, (0, 0, 0), self.circle_position, self.circle_radius-6)