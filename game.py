import pygame
import sys
import os

size = weight, height = 600, 600
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(fps)