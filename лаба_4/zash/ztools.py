from zarithmetic import *

def add_input(canvas, points, event):
    x, y = event.x, event.y
    points.append((x, y))
    canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")

def clear(canvas, points):
    canvas.delete("all")
    points.clear()

def draw_triangle(canvas, p1, p2, p3):
    canvas.delete("triangle")
    canvas.create_polygon(p1, p2, p3, fill='', outline='black', tags="triangle")

def solve(canvas, points):
    res = min_triangle_bis(points)
    #canvas.delete("all")
    #for x, y in points:
    #    canvas.create_oval(x-3, y-3, x+3, y+3, fill="black")
    draw_triangle(canvas, *res)
    print(res)
