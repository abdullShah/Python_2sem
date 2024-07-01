# Функция для нахождения точки пересечения двух прямых
def line_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None  # Прямые параллельны или совпадают

    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator

    return x, y


# Функция для вычисления площади треугольника по трем точкам
def triangle_area(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)


# Функция для поиска минимальной площади треугольника
def min_triangle_area(lines_set):
    min_area = float('inf')
    min_line_indices = None
    min_intersections = None

    # Перебор всех комбинаций троек прямых
    for i in range(len(lines_set)):
        for j in range(i + 1, len(lines_set)):
            for k in range(j + 1, len(lines_set)):
                line1, line2, line3 = lines_set[i], lines_set[j], lines_set[k]
                intersection1 = line_intersection(line1, line2)
                intersection2 = line_intersection(line1, line3)
                intersection3 = line_intersection(line2, line3)
                if intersection1 and intersection2 and intersection3:
                    intersections = [intersection1, intersection2, intersection3]
                    area = triangle_area(intersections)
                    if area < min_area and area != 0:
                        min_area = area
                        min_intersections = intersections
                        min_line_indices = [i + 1, j + 1, k + 1]

    return min_area, min_line_indices, min_intersections
