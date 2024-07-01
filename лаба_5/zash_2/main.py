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

def get_points(arr):
    new_arr = []

    cur_ind = 0
    is_end = False
    while not is_end:
        if cur_ind < len(arr):
            while cur_ind < len(arr) and arr[cur_ind] is None:
                cur_ind += 1

            if cur_ind == len(arr) and arr[cur_ind - 1] is None:
                is_end = True
            if not is_end:
                new_arr.append(arr[cur_ind])
                arr[cur_ind] = None
                cur_ind += 4
        else:
            cur_ind = 0
    new_arr.append(new_arr[0])

    return new_arr

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Защита")
clock = pygame.time.Clock()

RADIUS = 200
RADIUS_POINT = 5
angle = 360 / 11

x_start = CENTER_X
y_start = CENTER_Y - RADIUS

screen.fill(WHITE)

pygame.draw.circle(screen, BLACK, (CENTER_X, CENTER_Y), 200, 1)

arr = []
vers = 11
while (vers > 0):
    pygame.draw.circle(screen, BLACK, (x_start, y_start), RADIUS_POINT)
    arr.append((x_start, y_start))
    x_start, y_start = manual_rotation((x_start, y_start), (CENTER_X, CENTER_Y), angle)
    vers -= 1

new_arr = get_points(arr)
for i in range(len(arr)):
    pygame.draw.line(screen, BLACK, new_arr[i], new_arr[i+1], 3)

pygame.display.flip()
