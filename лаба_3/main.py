"""
Абдуллаев Шахмар ИУ7-24Б

Реализован метод наименее значащих битов (Least Significant Bit, LSB) для сокрытия информации в изображении. 
"""

import tkinter as tk

from action import *

# Создание окна
root = tk.Tk()
root.title("Стеганография")
root.geometry("555x275")
root.resizable(False, False)

# Выбор режима
mode_var = tk.StringVar(value="hide")
mode_frame = tk.Frame(root)
mode_frame.pack(pady=10)
tk.Label(mode_frame, text="Режим:").pack(side=tk.LEFT)
tk.Radiobutton(mode_frame, text="Сокрытие", variable=mode_var, value="hide").pack(side=tk.LEFT)
tk.Radiobutton(mode_frame, text="Извлечение", variable=mode_var, value="extract").pack(side=tk.LEFT)

# Ввод пути изображения
image_path = tk.StringVar()
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Путь изображения:").pack(side=tk.LEFT)
input_entry = tk.Entry(input_frame, textvariable=image_path, width=30)
input_entry.pack(side=tk.LEFT)
tk.Button(input_frame, text="Обзор", command=lambda: browse_image(image_path)).pack(side=tk.LEFT)

# Ввод пути преобразованного изображения
converted_image_path = tk.StringVar()
converted_image_frame = tk.Frame(root)
converted_image_frame.pack(pady=10)

tk.Label(converted_image_frame, text="Путь преобразованного изображения:").pack(side=tk.LEFT)
converted_image_entry = tk.Entry(converted_image_frame, textvariable=converted_image_path, width=30)
converted_image_entry.pack(side=tk.LEFT)
converted_image_entry_button = tk.Button(converted_image_frame, text="Обзор",
                                         command=lambda: save_as(converted_image_path))
converted_image_entry_button.pack(side=tk.LEFT)

# Ввод сообщения
message_var = tk.StringVar()

message_frame = tk.Frame(root)
message_frame.pack(pady=5)
tk.Label(message_frame, text="Сообщение:").pack(side=tk.LEFT)
message_entry = tk.Entry(message_frame, textvariable=message_var, width=30)
message_entry.pack(side=tk.LEFT)

# Кнопка выполнения
action_frame = tk.Frame(root)
action_frame.pack(pady=10)
tk.Button(action_frame, text="Выполнить",
          command=lambda: process(mode_var, image_path, converted_image_path, message_var, output_label)).pack()

# Вывод результата
output_label = tk.Label(root)
output_label.pack(pady=10)

# Вызов переключателя, чтобы установить начальное состояние
toggle_message_entry(mode_var, converted_image_entry, converted_image_entry_button, message_entry, tk)

# Привязка переключателя и радиокнопок
mode_var.trace_add("write",
                   lambda *args: toggle_message_entry(mode_var, converted_image_entry, converted_image_entry_button,
                                                      message_entry, tk))

# Создание меню с разделенными категориями
menubar = tk.Menu(root)

# Меню "Информация"
info_menu = tk.Menu(menubar, tearoff=0)
info_menu.add_command(label="О программе", command=lambda: display_info())

# Добавление меню в основное меню
menubar.add_cascade(label="Инфо", menu=info_menu)

# Привязка меню к корневому окну
root.config(menu=menubar)

root.mainloop()
