"""
Абдуллаев Шахмар ИУ7-24Б

"""

import tkinter as tk

from action import *


root = tk.Tk()
root.title("Стеганография")
root.geometry("555x275")
root.resizable(False, False)


image_path = tk.StringVar()
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Путь изображения:").pack(side=tk.LEFT)
input_entry = tk.Entry(input_frame, textvariable=image_path, width=30)
input_entry.pack(side=tk.LEFT)
tk.Button(input_frame, text="Обзор", command=lambda: browse_image(image_path)).pack(side=tk.LEFT)


converted_image_path = tk.StringVar()
converted_image_frame = tk.Frame(root)
converted_image_frame.pack(pady=10)

tk.Label(converted_image_frame, text="Путь преобразованного изображения:").pack(side=tk.LEFT)
converted_image_entry = tk.Entry(converted_image_frame, textvariable=converted_image_path, width=30)
converted_image_entry.pack(side=tk.LEFT)
converted_image_entry_button = tk.Button(converted_image_frame, text="Обзор",
                                         command=lambda: save_as(converted_image_path))
converted_image_entry_button.pack(side=tk.LEFT)


message_var = tk.StringVar()

message_frame = tk.Frame(root)
message_frame.pack(pady=5)
tk.Label(message_frame, text="Порог:").pack(side=tk.LEFT)
message_entry = tk.Entry(message_frame, textvariable=message_var, width=30)
message_entry.pack(side=tk.LEFT)


action_frame = tk.Frame(root)
action_frame.pack(pady=10)
tk.Button(action_frame, text="Выполнить",
          command=lambda: process(image_path, converted_image_path, message_var, output_label)).pack()


output_label = tk.Label(root)
output_label.pack(pady=10)

root.mainloop()
