import math

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def triangle_area(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def bissetrice_length(p1, p2, p3):
    a = distance(p2, p3)
    b = distance(p1, p3)
    c = distance(p1, p2)
    
    s = (a + b + c) / 2
    h = (2 / a) * (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    l = (b * c * (1 - (a / (b + c))**2)) ** 0.5
    
    return l


def vector_length(v):
    return (v[0]**2 + v[1]**2)**0.5

def dot_product(v1, v2):
    # Функция для вычисления скалярного произведения двух векторов
    return v1[0] * v2[0] + v1[1] * v2[1]

def angle_between_segments(start1, end1, start2, end2):
    vector1 = (end1[0] - start1[0], end1[1] - start1[1])
    vector2 = (end2[0] - start2[0], end2[1] - start2[1])
    
    # Вычисляем скалярные произведения векторов и их длины
    dot_product_value = dot_product(vector1, vector2)
    length_product = vector_length(vector1) * vector_length(vector2)
    
    # Проверяем, находится ли значение в пределах допустимого диапазона
    dot_product_value = max(-1, min(dot_product_value, 1))
    
    # Вычисляем угол между векторами
    angle_rad = math.acos(dot_product_value / length_product)
    
    # Конвертируем радианы в градусы
    angle_deg = math.degrees(angle_rad)
    
    return angle_deg


def min_triangle_bis(points):
    min_area = float('inf')
    min_triangle = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                p1, p2, p3 = points[i], points[j], points[k]
                ab = distance(p2, p1)
                bc = distance(p1, p3)
                bisec = bissetrice_length(p1, p2, p3)
                angle = angle_between_segments(p2, p1, p1, p2)
                area1 = 0.5 * ab * bisec * math.sin(angle/2)
                area2 = 0.5 * bc * bisec * math.sin(angle/2)
                area_diff = abs(area1 - area2)
                if area_diff < min_area:
                    min_area = area_diff
                    min_triangle = (p1, p2, p3)
    
    return min_triangle

#////////////////////////////
def point_in_triangle(p, p1, p2, p3):
    # Вычисляем барицентрические координаты точки p относительно вершин треугольника
    alpha = ((p2[1] - p3[1]) * (p[0] - p3[0]) + (p3[0] - p2[0]) * (p[1] - p3[1])) / \
            ((p2[1] - p3[1]) * (p1[0] - p3[0]) + (p3[0] - p2[0]) * (p1[1] - p3[1]))
    beta = ((p3[1] - p1[1]) * (p[0] - p3[0]) + (p1[0] - p3[0]) * (p[1] - p3[1])) / \
           ((p2[1] - p3[1]) * (p1[0] - p3[0]) + (p3[0] - p2[0]) * (p1[1] - p3[1]))
    gamma = 1.0 - alpha - beta
    
    # Проверяем, находится ли точка внутри треугольника
    return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1

def area(p1, p2, p3):
    # Вычисляем площадь треугольника по формуле Герона
    return 0.5 * abs(p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))

def point_in_triangle(p, p1, p2, p3):
    # Вычисляем площадь всего треугольника
    triangle_area = area(p1, p2, p3)
    
    # Вычисляем площади подтреугольников
    sub_triangle1_area = area(p, p1, p2)
    sub_triangle2_area = area(p, p2, p3)
    sub_triangle3_area = area(p, p3, p1)
    
    # Проверяем, находится ли точка внутри треугольника
    return abs(triangle_area - (sub_triangle1_area + sub_triangle2_area + sub_triangle3_area)) < 1e-6




#////////////////////////////
def line_equation(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    # Находим коэффициенты уравнения прямой
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    
    return A, B, C

def point_side_of_line(point, line):
    x, y = point
    A, B, C = line
    
    # Вычисляем значение уравнения прямой в точке
    value = A * x + B * y + C
    
    # Проверяем значение
    if value > 0:
        return "С правой стороны"
    elif value < 0:
        return "С левой стороны"
    else:
        return "На прямой"