import pygame
from sys import exit
from ballClass import Ball
from vectorClass import Vector2, dist, reflection

pygame.init()

# Game properties :
WIDTH, HEIGHT = 1200, 1200
display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)  # | pygame.FULLSCREEN)

# Simulation properties :
simulationOffset = Vector2(WIDTH / 2, HEIGHT / 2)
radius = 600
centerVec = Vector2(radius, radius)
timeSteps = 25
FPS = 60
clock = pygame.time.Clock()
widthBalls = 600
heightBalls = 6
balls = []
pause = True

# Text :
fpsFont = pygame.font.SysFont("comic sans", 20)

# Entities :
for x in range(1, 1 + widthBalls):
    for y in range(1, 1 + heightBalls):
        balls.append(
            Ball(radius=10, center_pos=(simulationOffset.x - widthBalls / 2 + x * 1 + 0, simulationOffset.y + y * 29),
                 color=(
                     (x * y * 255 / (widthBalls * heightBalls)) % 255,
                     (x * y * 255 / (widthBalls * heightBalls)) % 255,
                     (x * y * 255 / (widthBalls * heightBalls)) % 255),
                 velocity=(0, -10 / timeSteps)))


def draw_screen():
    display.fill((0, 0, 0))
    pygame.draw.circle(display, (25, 25, 25), simulationOffset.return_tuple(), radius)
    display.blit(fpsText, (10, 10))
    if pause:
        for b in balls:
            b.draw(display)


# Main loop :
while 1:
    clock.tick(FPS)
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
            if dist(ball.position + ball.velocity * timeSteps, centerVec) < radius:
                ball.position += ball.velocity * timeSteps
            else:
                for _ in range(timeSteps):
                    if dist(ball.position, centerVec) >= radius:
                        ball.velocity = reflection(ball.velocity, Vector2(radius - ball.position.x,
                                                                          radius - ball.position.y).get_normalized())
                    ball.update()
            ball.draw(display)

    pygame.display.update()
