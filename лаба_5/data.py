import pygame

from const import FPS
from tools import calc_speed_orb

mercury = {  # Меркурий
    'length_orbit': 40,  # Радиус орбиты от центра солнца до центра планеты
    'angle_orb': 0,  # Угол для вращения планеты по орбите
    'angle_self': 0,  # Угол для вращения планеты вокруг своей оси
    'speed_orb': calc_speed_orb(2.5, FPS),
    # Увеличение угла для вращения по орбите, изменяется количество секунд на один оборот по орбите
    'speed_self': 1,  # Увеличиваем угол для вращения вокруг своей оси
    'image': pygame.image.load("./images/mercury.png")  # Загрузка фотографии
}
venera = {  # Венера
    'length_orbit': 65,
    'angle_orb': 0,
    'angle_self': 0,
    'speed_orb': calc_speed_orb(6, FPS),
    'speed_self': 1,
    'image': pygame.image.load("./images/venera.png")
}
earth = {  # Земля
    'length_orbit': 95,
    'angle_orb': 0,
    'angle_self': 0,
    'speed_orb': calc_speed_orb(10, FPS),
    'speed_self': 1,
    'image': pygame.image.load("./images/earth.png")
}
mars = {  # Марс
    'length_orbit': 125,
    'angle_orb': 0,
    'angle_self': 0,
    'speed_orb': calc_speed_orb(20, FPS),
    'speed_self': 1,
    'image': pygame.image.load("./images/mars.png")
}
jupiter = {  # Юпитер
    'length_orbit': 160,
    'angle_orb': 0,
    'angle_self': 0,
    'speed_orb': calc_speed_orb(40, FPS),
    'speed_self': 0.3,
    'image': pygame.image.load("./images/jupiter.png")
}
saturn = {  # Сатурн
    'length_orbit': 210,
    'angle_orb': 0,
    'angle_self': 0,
    'speed_orb': calc_speed_orb(80, FPS),
    'speed_self': 0.05,
    'image': pygame.image.load("./images/saturn.png")
}

# Инициализация планет солнечной системы
planets = [
    mercury, 
    venera, 
    earth, 
    mars, 
    jupiter, 
    saturn
]

"""sun = { # Солнце
    'length_orbit': 0,
    'angle_orb': 0,
    'angle_self': 0,
    'speed_orb': 0,
    'speed_self': 1,
    'image': pygame.image.load("./images/sun.png")
    },"""

# Инициализация нейтронной звезды
neutron_star = {
    'start': (35, 35),
    'end': (65, 65),
    'color': (225, 193, 237)
}
