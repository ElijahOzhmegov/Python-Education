import pygame
from time import sleep


def draw_square(screen, A, B, C, D, alpha, deep=10):
    if deep == 0: return
    new_ABCD = []
    for M, N in (A, B), (B, C), (C, D), (D, A):
        pygame.draw.aaline(screen, WHITE, M, N)
        new_ABCD.append(((1 - alpha)*M[0] + alpha*N[0], (1 - alpha)*M[1] + alpha*N[1]))

    draw_square(screen, *new_ABCD, alpha, deep-1)


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 600, 600

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])

running = True
alpha, pace = 0.0, 0.001
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.key.get_pressed(): running = False

    screen.fill(BLACK)
    draw_square(screen, (100, 100), (500, 100), (500, 500), (100, 500), alpha, 300)
    alpha += pace; sleep(0.001)
    pygame.display.flip()

    if alpha > 1 or alpha < 0: pace = -pace

