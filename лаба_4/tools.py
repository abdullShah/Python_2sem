import tkinter as tk
from tkinter import messagebox

from arithmetic import *


def add_line_from_input(start_x_entry, start_y_entry, end_x_entry, end_y_entry, table, canvas, canvas_width,
                        canvas_height, lines):
    start_x = start_x_entry.get()
    start_y = start_y_entry.get()
    end_x = end_x_entry.get()
    end_y = end_y_entry.get()

    # Проверяем, что все поля заполнены
    if start_x and start_y and end_x and end_y:
        start_x = int(start_x_entry.get())
        start_y = int(start_y_entry.get())
        end_x = int(end_x_entry.get())
        end_y = int(end_y_entry.get())

        # Проверяем, что значения координат находятся в пределах от 0 до ширины и высоты холста
        if 0 <= int(start_x) <= canvas_width and 0 <= int(start_y) <= canvas_height and 0 <= int(
                end_x) <= canvas_width and 0 <= int(end_y) <= canvas_height:
            if (start_x, start_y) != (end_x, end_y):
                if [(start_x, start_y), (end_x, end_y)] not in lines:
                    table.insert("", "end", values=(f"{len(lines) + 1}", start_x, start_y, end_x, end_y))
                    start_x_entry.delete(0, tk.END)
                    start_y_entry.delete(0, tk.END)
                    end_x_entry.delete(0, tk.END)
                    end_y_entry.delete(0, tk.END)

                    lines.append([(start_x, start_y), (end_x, end_y)])
                    canvas.create_oval(start_x - 2, start_y - 2, start_x + 2, start_y + 2, fill="red")
                    canvas.create_oval(end_x - 2, end_y - 2, end_x + 2, end_y + 2, fill="red")
                    canvas.create_line((start_x, start_y), (end_x, end_y), fill="blue")
                else:
                    # Если прямая уже введена ранее, выводим сообщение об ошибке
                    messagebox.showerror("Ошибка", "Эта прямая уже была введена ранее")
            else:
                # Если начальная и конечная точки совпадают, выводим сообщение об ошибке
                messagebox.showerror("Ошибка", "Начальная и конечная точки совпадают, это не прямая")
        else:
            # Если значения выходят за пределы, вы можете вывести сообщение об ошибке
            messagebox.showerror("Ошибка",
                                 f"Координаты должны быть в пределах от 0 до ширины и высоты холста ({canvas_width}x{canvas_height})")
    else:
        # Если не все поля заполнены, вы можете вывести предупреждение
        messagebox.showwarning("Предупреждение", "Пожалуйста, заполните все поля")


# Функция для добавление прямой
def add_line(canvas, table, lines, event):
    # Получение координат щелчка мыши
    x, y = event.x, event.y
    # Отображение точки на холсте
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red")

    if len(lines) == 0 or len(lines[-1]) == 2:
        lines.append([(x, y)])
    else:
        lines[-1].append((x, y))

    if len(lines[-1]) == 2:
        if (lines[-1][0][0] == lines[-1][1][0]) and (lines[-1][0][1] == lines[-1][1][1]):
            del lines[-1]
            canvas.delete("all")
            for i in range(len(lines)):
                start_x, start_y, end_x, end_y = lines[i][0][0], lines[i][0][1], lines[i][1][0], lines[i][1][1]
                canvas.create_oval(start_x - 2, start_y - 2, start_x + 2, start_y + 2, fill="red")
                canvas.create_oval(end_x - 2, end_y - 2, end_x + 2, end_y + 2, fill="red")
                canvas.create_line((start_x, start_y), (end_x, end_y), fill="blue")
            messagebox.showerror("Ошибка", "Начальная и конечная точки совпадают, это не прямая")
        else:
            # Добавление линии между точками на холсте
            canvas.create_line(lines[-1][0], lines[-1][1], fill="blue")
            # Добавление прямой в таблицу
            table.insert("", "end",
                         values=(f"{len(lines)}", lines[-1][0][0], lines[-1][0][1], lines[-1][1][0], lines[-1][1][1]))


# Функция для постройки минимального треугольника
def draw_triangle(canvas, points, line_width=3):
    lines = []
    for i in range(len(points)):  # Рисуем линии между всеми парами точек (замыкаем треугольник)
        line = canvas.create_line(points[i][0], points[i][1], points[(i + 1) % len(points)][0],
                                  points[(i + 1) % len(points)][1], width=line_width)
        lines.append(line)
    return lines


# Функция для удаления минимального треугольника
def delete_triangle(canvas, lines):
    for line in lines:
        canvas.delete(line)


# Функция для очистки результата
def clear_result(res_lines, canvas, result_label):
    delete_triangle(canvas, res_lines)
    result_label.config(text="Площадь: Номера прямых: ")


# Функция для очистки всех полей
def clear_all(result_label, res_lines, canvas, table, lines):
    lines.clear()
    canvas.delete("all")
    table.delete(*table.get_children())
    clear_result(res_lines, canvas, result_label)


# Кнопка для поиска минимальной площади треугольника
def calculate_result(lines, res_lines, result_label, canvas):
    if len(lines) != 0 and len(lines[-1]) != 2:
        messagebox.showerror("Ошибка", "Поставьте вторую точку, чтобы достроить прямую")
        return

    min_area, ind_min_triangle, min_intersections = min_triangle_area(lines)
    if not ind_min_triangle:
        messagebox.showerror("Ошибка", "Нет прямых, образующие треугольник")
        return

    if res_lines:
        delete_triangle(canvas, res_lines)
        res_lines.clear()

    res_lines += draw_triangle(canvas, min_intersections)
    result_label.config(
        text=f"Площадь: {min_area:<15.6g}" + f"Номера прямых: {', '.join([str(i) for i in ind_min_triangle]):<15}")


# Функция для валидации ввода чисел
def validate_positive_integer(input):
    if input.isdigit():
        return True
    if input == "":
        return True
    return False
