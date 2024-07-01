import pygame
from math import sin, cos, radians
from const import *

def manual_rotation(point, center, angle):
    angle_rad = radians(angle)
    x_shifted = point[0] - center[0]
    y_shifted = point[1] - center[1]
    xn = x_shifted * cos(angle_rad) - y_shifted * sin(angle_rad)
    yn = x_shifted * sin(angle_rad) + y_shifted * cos(angle_rad)
    return [xn + center[0], yn + center[1]]

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Защита")
clock = pygame.time.Clock()

m = 100
k = 0.1

x = [i for i in range(WIDTH)]
ind_x = 0
angle = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    if ind_x < len(x):
        cur_x = x[ind_x]
        ind_x += 1

    y = int(m * sin(k * cur_x)) + HEIGHT // 2
    points = [[cur_x - 50, y - 50], [cur_x + 50, y - 50], [cur_x + 50, y + 50], [cur_x - 50, y + 50]]
    center = [cur_x, y]

    rotated_points = [manual_rotation(point, center, angle) for point in points]
    angle += 1  

    pygame.draw.polygon(screen, BLACK, rotated_points)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
