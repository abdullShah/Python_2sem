"""
Абдуллаев Шахмар ИУ7-24Б
Реализована с использованием библиотеки pygame циклическая анимация с сюжетом.
"""
import pygame

from data import *
from tools import *

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космос звезд")
clock = pygame.time.Clock()

# Инициализация солнца
sun_surf = pygame.Surface((SUN_RADIUS * 2, SUN_RADIUS * 2), pygame.SRCALPHA)  # Создание поверхности
sun_surf.fill((0, 0, 0, 0))  # Установление прозрачного фона
pygame.draw.circle(sun_surf, YELLOW, (SUN_RADIUS, SUN_RADIUS), SUN_RADIUS)  # Создание окружности
pygame.draw.circle(sun_surf, ORANGE, (SUN_RADIUS, SUN_RADIUS), SUN_RADIUS * 0.7)  # Создание окружности
pygame.draw.circle(sun_surf, RED, (SUN_RADIUS, SUN_RADIUS), SUN_RADIUS * 0.3)  # Создание окружности

# Создание звезд
stars = get_stars()
cur_star_time = STAR_TIME

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие экрана
            exit()

    screen.fill((0, 0, 0))  # Очистка экрана

    draw_neutron_star(screen, neutron_star)  # Отрисовка нейтронной звезды
    neutron_star['start'] = rotate_point(neutron_star['start'], DEGREE_ROTATE, ORIGIN)  # Движение нейтронной звезды
    neutron_star['end'] = rotate_point(neutron_star['end'], DEGREE_ROTATE, ORIGIN)  # Движение нейтронной звезды

    # Отрисовка звездного фона
    for i in range(len(stars)):
        color, (x, y), size, cur_size, is_proc_smaller = stars[i]  # Получение звезды
        pygame.draw.circle(screen, color, (x, y), cur_size)  # Отрисовка звезды
        if not (is_proc_smaller) and cur_size < size:  # Масштабирование звезды вверх
            stars[i][3] += STAR_SPEED
        else:
            stars[i][4] = True  # Звезда достигла максимального размера
        if is_proc_smaller and 0 < cur_size:  # Масштабирование звезды вниз
            stars[i][3] -= STAR_SPEED

    screen.blit(sun_surf, (CENTER_X - SUN_RADIUS, CENTER_Y - SUN_RADIUS))  # Отрисовка солнца

    for planet in planets:
        pygame.draw.circle(screen, GRAY, (CENTER_X, CENTER_Y), planet['length_orbit'], 1)  # Отрисовка орбиты планеты
        planet_x = CENTER_X + math.cos(math.radians(planet['angle_orb'])) * planet[
            'length_orbit']  # Вычисление позиции планеты
        planet_y = CENTER_Y + math.sin(math.radians(planet['angle_orb'])) * planet[
            'length_orbit']  # Вычисление позиции планеты

        planet_rect = planet['image'].get_rect(
            center=(planet_x, planet_y))  # Возвращает координаты планеты, создает объект Rect
        rotated_planet = pygame.transform.rotate(planet['image'],
                                                 planet['angle_self'])  # Поворачиваем планеты на угол вращения

        screen.blit(rotated_planet, planet_rect)  # Отображение планеты на экране
        planet['angle_orb'] += planet['speed_orb']  # Вращение планеты по окружности
        if planet['angle_orb'] >= 360:
            planet['angle_orb'] = 0
        planet['angle_self'] += planet['speed_self']  # Вращение планеты вокруг своей оси
        if planet['angle_self'] >= 360:
            planet['angle_self'] = 0

    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Задержка, чтобы контролировать скорость анимации

    # Обновление звезд
    if cur_star_time == STAR_TIME:
        stars = get_stars()
        cur_star_time = 0
    cur_star_time += 1
