import tkinter as tk
from functools import partial
from ztools import *

window = tk.Tk()
window.title("Приложение")

points = []

canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.bind("<Button-1>", partial(add_input, canvas, points))
canvas.pack()

solve_button = tk.Button(window, text="Найти решение", command=lambda: solve(canvas, points))
solve_button.pack()

clear_button = tk.Button(window, text="Очистить холст", command=lambda: clear(canvas, points))
clear_button.pack()

window.mainloop()
