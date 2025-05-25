import pygame
from animation import Ball, Circle

size = (700, 700)
ball_size = 40

# Initiation
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ball Animation")

clock = pygame.time.Clock()
ball = Ball(size, ball_size)
circle = Circle(size, 300)

# Boucle d'événements pour garder la fenêtre ouverte
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.moove()
    ball.ball_velocity[1] += 0.3
    screen.fill((0, 0, 0))
    circle.draw(screen)
    ball.draw(screen)
    pygame.display.flip()

    clock.tick(60)

# Quitter Pygame proprement
pygame.quit()