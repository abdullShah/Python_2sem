def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def triangle_area(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p3, p1)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def min_raz_triangles_area(triangles):
    min_area = float('inf')
    min_triangles = None
    
    for i in range(len(triangles)):
        for j in range(i + 1, len(triangles)):
            triangle1 = triangles[i]
            triangle2 = triangles[j]
            raz = abs(triangle_area(*triangle1) - triangle_area(*triangle2))
            if min_area > raz:
                min_area = raz
                min_triangles = [triangle1, triangle2]
    
    return min_triangles
