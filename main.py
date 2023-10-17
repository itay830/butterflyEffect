# import comp
import pygame
import time
from ballClass import Ball
from sys import exit
from vectorClass import Vector2, dist, reflection

pygame.init()

# Game properties :
WIDTH, HEIGHT = 1200, 1200
display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

# Simulation properties :
radius = 600
timeSteps = 25
prev_time = 0
FPS = 60
clock = pygame.time.Clock()
gravity = -1 / timeSteps
pause = True
reflected = False
widthBalls = 400
heightBalls = 3
balls = []
ballsReflection = []

# Entities :
for x in range(widthBalls):
    for y in range(heightBalls):
        balls.append(
            Ball(radius=3, center_pos=(radius - widthBalls / 2 + x*2, radius + y), color=(x % 255 + 1, x * y % 120 + 1, x * y % 60 + 1),
                 velocity=(0, -10 / timeSteps)))


def draw_screen():
    display.fill((96, 96, 96))
    pygame.draw.circle(display, (150, 150, 150), (radius, radius), radius)



# Main loop :
while 1:
    clock.tick(FPS)
    dt = time.time() - prev_time
    prev_time = time.time()
    print(dt)

    # Event listening :
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                pause = not pause

    # Logic :
    draw_screen()

    if not pause:
        for ball in balls:
            if dist(ball.position + ball.velocity * timeSteps, Vector2(radius, radius)) < radius:
                ball.position += ball.velocity * timeSteps
            else:
                for _ in range(timeSteps):
                    if dist(ball.position, Vector2(radius, radius)) >= radius:
                        n = Vector2(radius - ball.position.x, radius - ball.position.y).get_normalized()
                        ball.velocity = reflection(ball.velocity, n)
                    ball.update()
            ball.draw(display)

    pygame.display.update()
