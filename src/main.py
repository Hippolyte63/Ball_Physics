import pygame
from animation import Ball, Circle
import numpy as np

size = (700, 700)
ball_radius = 30
random_velocity = np.array([np.random.uniform(-10, 10), np.random.uniform(-10, 10)])

# Initiation
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ball Animation")

clock = pygame.time.Clock()
Circles = [
    Circle(size, 230),
    Circle(size, 200)
]
ball = Ball(size, ball_radius, random_velocity, obstacles=Circles)



# Boucle d'événements pour garder la fenêtre ouverte
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.move()
    ball.ball_velocity *= 0.995 # slow down the ball over time (friction)
    ball.ball_velocity[1] += 0.3
    screen.fill((0, 0, 0))
    for circle in Circles:
        circle.draw(screen)
    ball.draw(screen)
    pygame.display.flip()

    clock.tick(60)

# Quitter Pygame proprement
pygame.quit()