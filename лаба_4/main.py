"""
Абдуллаев Шахмар ИУ7-24Б
Разработано приложение с графическим интерфейсом для решения задачи по индивидуальному варианту.
Задание: На плоскости задано множество прямых. Найти три прямые, образующие треугольник 
минимальной площади.
"""

from functools import partial
from tkinter import ttk

from tools import *

root = tk.Tk()
root.title("Треугольник минимальной площади")

# Создание холста для прямых
canvas = tk.Canvas(root, width=300, height=250, bg="white")
canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Создание таблицы для точек
table_frame = ttk.Frame(root)
table_frame.grid(row=0, column=1, columnspan=5, padx=10, pady=10, sticky="nsew")

table = ttk.Treeview(table_frame, columns=("number", "start1", "end1", "start2", "end2"), show="headings")
table.heading("number", text="№")
table.heading("start1", text="Начало X")
table.heading("end1", text="Начало Y")
table.heading("start2", text="Конец X")
table.heading("end2", text="Конец Y")
table.grid(row=0, column=1, columnspan=5, padx=10, pady=10, sticky="nsew")

table_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=table_scroll.set)
table_scroll.grid(row=0, column=6, sticky="ns")

# Список для хранения созданных прямых
lines = []

# Список для хранения прямых, образующий треугольник с минимальной площадью
res_lines = []

# Привязка события щелчка мыши на холсте
canvas.bind("<Button-1>", partial(add_line, canvas, table, lines))

# Валидация полей ввода
positive_int_validator = root.register(validate_positive_integer)

# Инпуты для ввода координат точек
start_x_label = ttk.Label(root, text="Начало X:")
start_x_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
start_x_entry = ttk.Entry(root, validate="key", validatecommand=(positive_int_validator, "%P"))
start_x_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

start_y_label = ttk.Label(root, text="Начало Y:")
start_y_label.grid(row=2, column=2, padx=10, pady=5, sticky="w")
start_y_entry = ttk.Entry(root, validate="key", validatecommand=(positive_int_validator, "%P"))
start_y_entry.grid(row=3, column=2, padx=10, pady=5, sticky="w")

end_x_label = ttk.Label(root, text="Конец X:")
end_x_label.grid(row=2, column=3, padx=10, pady=5, sticky="w")
end_x_entry = ttk.Entry(root, validate="key", validatecommand=(positive_int_validator, "%P"))
end_x_entry.grid(row=3, column=3, padx=10, pady=5, sticky="w")

end_y_label = ttk.Label(root, text="Конец Y:")
end_y_label.grid(row=2, column=4, padx=10, pady=5, sticky="w")
end_y_entry = ttk.Entry(root, validate="key", validatecommand=(positive_int_validator, "%P"))
end_y_entry.grid(row=3, column=4, padx=10, pady=5, sticky="w")

# Кнопка для добавления прямой с клавиатуры
add_line_button = ttk.Button(root, text="Добавить прямую",
                             command=lambda: add_line_from_input(start_x_entry, start_y_entry, end_x_entry, end_y_entry,
                                                                 table, canvas, canvas.winfo_width(),
                                                                 canvas.winfo_height(), lines))
add_line_button.grid(row=3, column=5, padx=10, pady=5, sticky="w")

# Кнопка для очистки результата
clear_result_button = ttk.Button(root, text="Очистить результат",
                                 command=lambda: clear_result(res_lines, canvas, result_label))
clear_result_button.grid(row=4, column=0, padx=(10, 5), pady=10, sticky="e")

# Лейбл для отображения результата
result_label = ttk.Label(root, text="Площадь: Номера прямых: ")
result_label.grid(row=4, column=1, columnspan=5, padx=10, pady=10, sticky="nsew")

# Кнопка для расчета результата
calculate_button = ttk.Button(root, text="Рассчитать",
                              command=lambda: calculate_result(lines, res_lines, result_label, canvas))
calculate_button.grid(row=4, column=2, padx=10, pady=10, sticky="e")

# Кнопка для очистки данных
clear_all_button = ttk.Button(root, text="Очистить все",
                              command=lambda: clear_all(result_label, res_lines, canvas, table, lines))
clear_all_button.grid(row=4, column=5, padx=(5, 10), pady=10, sticky="e")

root.mainloop()
