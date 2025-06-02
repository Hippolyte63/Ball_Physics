import pygame
import numpy as np

class Circle:
    def __init__ (self, screen_size, circle_radius, width=6):
        self.screen_size = screen_size
        self.circle_outter_radius = circle_radius
        self.circle_position = np.array([screen_size[0]//2, screen_size[1]//2])
        self.width = width
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.circle_position, self.circle_outter_radius)
        pygame.draw.circle(screen, (0, 0, 0), self.circle_position, self.circle_outter_radius - self.width)


class Ball:
    def __init__(self, screen_size, ball_radius, initial_velocity=np.array([0, 0]), obstacles=None):
        self.screen_size = screen_size
        self.ball_radius = ball_radius
        self.ball_position = np.array([screen_size[0] // 2, screen_size[1] // 2], dtype=float) # float to ensure compatibility with velocity
        self.ball_velocity = initial_velocity
        if len(initial_velocity) != 2:
            raise ValueError("Ball velocity must be a list of two elements [vx, vy]")
        self.obstacles = obstacles if obstacles is not None else []

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.ball_position, self.ball_radius)
        pygame.draw.circle(screen, (255, 0, 0), self.ball_position, self.ball_radius-2)

    def move(self):

        # Update ball position with velocity
        self.ball_position += self.ball_velocity
        # Ensure ball position is within the screen limits
        self.ball_position = np.clip(self.ball_position, self.ball_radius, np.array(self.screen_size) - self.ball_radius)


        # Bounce off circles
        for obstacle in self.obstacles:
            collision = False
            direction = self.ball_position - obstacle.circle_position
            distance = np.linalg.norm(direction)
            
            normal = direction / distance if distance !=0 else np.array([1, 0])
            
            collision = False

            # Rebond Intérieur
            if distance > obstacle.circle_outter_radius - obstacle.width - self.ball_radius:
                collision = True
                # Replace ball at surface
                self.ball_position = obstacle.circle_position + (obstacle.circle_outter_radius - obstacle.width - self.ball_radius) * normal

            if collision:
                # The tangential velocity is conserved (v - v.n) while the normal component is reversed (-v.n)
                self.ball_velocity -= 2 * np.dot(self.ball_velocity, normal) * normal

        for i in range(2):

            # Bounce off walls
            if self.ball_position[i] <= self.ball_radius or self.ball_position[i] >= self.screen_size[i] - self.ball_radius:
                self.ball_velocity[i] *= -1
                
