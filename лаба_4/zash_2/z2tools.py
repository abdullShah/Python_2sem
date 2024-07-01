from z2arithmetic import *

def add_input(canvas, triangles, event):
    x, y = event.x, event.y
    if len(triangles) == 0 or len(triangles[-1]) == 3:
        triangles.append([])

    if len(triangles[-1]) != 3:
        triangles[-1].append((x, y))
    print(triangles)
    
    if len(triangles[-1]) == 3:
        draw_triangle(canvas, *triangles[-1])

    canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")

def clear(canvas, triangles):
    canvas.delete("all")
    triangles.clear()

def draw_triangle(canvas, p1, p2, p3, result=False):
    #canvas.delete("triangle")
    if result:
        canvas.create_polygon(p1, p2, p3, fill='', outline='black', tags="triangle", width=3)
    else:
        canvas.create_polygon(p1, p2, p3, fill='', outline='black', tags="triangle")

def solve(canvas, triangles):
    #canvas.delete("all")
    triangle1, triangle2 = min_raz_triangles_area(triangles)
    print(triangle1, triangle2)
    draw_triangle(canvas, *triangle1, result=True)
    draw_triangle(canvas, *triangle2, result=True)
