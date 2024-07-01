import math
import random

import pygame

from const import *


# Функция для вычисления скорости вращения планеты вокруг своей орбиты
def calc_speed_orb(time, fps):
    degrees_per_second = 360 / time  # Градусов в секунду
    orbit_speed = degrees_per_second / fps  # Скорость вращения в градусах за кадр
    return orbit_speed


# Функция для создания звездного фона
def get_stars():
    stars = []
    num_stars = random.randint(50, 100)  # Случайное количество звезд
    for _ in range(num_stars):
        x = random.randint(0, WIDTH)  # Случайная позиция по горизонтали
        y = random.randint(0, HEIGHT)  # Случайная позиция по вертикали
        size = random.randint(1, 3)  # Случайный размер звезды
        brightness = random.randint(100, 255)  # Случайная яркость звезды
        color = (brightness, brightness, brightness)  # Случайный цвет звезды
        stars.append([color, (x, y), size, 0, False])
    return stars


# Функция поворачивает точку вокруг центральной точки на заданный угол
def rotate_point(point, angle, center):
    x, y = point
    cx, cy = center
    translated_x = x - cx
    translated_y = y - cy
    radians = math.radians(angle)
    rotated_x = translated_x * math.cos(radians) - translated_y * math.sin(radians)
    rotated_y = translated_x * math.sin(radians) + translated_y * math.cos(radians)
    final_x = rotated_x + cx
    final_y = rotated_y + cy
    return (final_x, final_y)


# Отрисовка нейтронной звезды
def draw_neutron_star(screen, neutron_star):
    pygame.draw.aaline(screen, (225, 193, 237), neutron_star['start'], neutron_star['end'])
    pygame.draw.circle(screen, (225, 193, 237), (
        (neutron_star['start'][0] + neutron_star['end'][0]) // 2,
        (neutron_star['start'][1] + neutron_star['end'][1]) // 2), 10)
