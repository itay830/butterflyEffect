import pygame
import time
from sys import exit
from ballClass import Ball
from vectorClass import Vector2, dist, reflection

pygame.init()

# Game properties :
WIDTH, HEIGHT = 1200, 1200
display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.FULLSCREEN)

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
heightBalls = 4
balls = []
ballsReflection = []

# Text :
fpsFont = pygame.font.SysFont("comic sans", 20)

# Entities :
for x in range(1, 1 + widthBalls):
    for y in range(1, 1 + heightBalls):
        balls.append(
            Ball(radius=25, center_pos=(widthBalls / 2 + x + 450, radius + y * 40), color=(
            (y * 255 * x * 255 / (widthBalls * heightBalls)) % 255,
            (y * 64 * x * 255 / (widthBalls * heightBalls)) % 255,
            (y * 125 * x * 255 / (widthBalls * heightBalls)) % 255),
                 velocity=(0, -10 / timeSteps)))


def draw_screen():
    display.fill((0, 0, 0))
    pygame.draw.circle(display, (25, 25, 25), (WIDTH / 2, HEIGHT / 2), radius)
    display.blit(fpsText, (10, 10))
    if pause:
        for b in balls:
            b.draw(display)


# Main loop :
while 1:
    clock.tick(FPS)
    dt = time.time() - prev_time
    prev_time = time.time()
    print("dt: ", dt)
    fpsText = fpsFont.render(str(round(clock.get_fps(), 2)), True, (255, 255, 255))

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
