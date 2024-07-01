import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from tools import *

"""
Автор проекта: Абдуллаев Шахмар ИУ7-24Б

Проект представляет собой приложение для вычисления корней функции 
на отрезке [a; b] определенным методом, используя модуль создания оконных 
приложений Tkinter. Для вычисления отрезок [a; b] делится на элементарные 
отрезки с шагом h. Гарантируется, что на каждом элементарном отрезке 
у функции не более одного корня. Для каждого элементарного отрезка, 
на котором есть корень, итерационно вычисляется приближенное значение 
корня с заданной точностью eps. Для обнаружения медленного процесса 
сходимости или расходимости метода количество итераций ограничивается
числом Nmax.
"""

# Создание окна
root = tk.Tk()
# Задание название окну
root.title("Расчет функции")

# Создание стиля окна
style = ttk.Style()

# Создание стиля для поля ввода
style.configure('CustomEntry.TEntry', font=('Arial', 12), foreground='blue', padding=10)

# Создание стиля для метки "Функция"
style.configure('Func.TLabel', foreground='black', font=('Arial', 12, 'italic'))

# Определение стиля для кнопки
style.configure('Custom.TButton', font=('Arial', 11, 'bold'), background='lightgrey')

# Определение стиля для справочника для ввода функции
style.configure('Question.TButton',
                font=('Arial', 8, 'bold'),
                foreground='black',
                background='white',
                borderwidth=0)

# Создание проверки ввода с клавиатуры функции
root_validate_function = root.register(validate_function)

# Создание лейблов и полей ввода функции
label_func = ttk.Label(root, text="Функция", style='Func.TLabel')
label_func.grid(row=0, column=0, padx=10, pady=10)
entry_func = ttk.Entry(root, style='Custom.TEntry')
entry_func.config(validate="key", validatecommand=(root_validate_function, "%P"))
entry_func.grid(row=0, column=1, padx=10, pady=10)
question_button = ttk.Button(root, text="?", width=2, command=lambda: func_info(messagebox), style='Question.TButton')
question_button.grid(row=0, column=0, sticky='ne')
question_button['takefocus'] = 0
button_clear_entry_func = ttk.Button(root, text="X", command=lambda: entry_func.delete(0, 'end'))
button_clear_entry_func.grid(row=0, column=2, sticky='w')
button_clear_entry_func.config(width=2, style='Custom.TButton')
button_clear_entry_func['takefocus'] = 0

# Создание проверки ввода с клавиатуры целых чисел
root_validate_int = root.register(validate_int)

# Создание лейблов и полей ввода начала отрезка
label_a = ttk.Label(root, text="Начало отрезка", style='Func.TLabel')
label_a.grid(row=1, column=0, padx=10, pady=10)
entry_a = ttk.Entry(root)
entry_a.config(validate="key", validatecommand=(root_validate_int, "%P"))
entry_a.grid(row=1, column=1, padx=10, pady=10)
button_clear_entry_a = ttk.Button(root, text="X", command=lambda: entry_a.delete(0, 'end'))
button_clear_entry_a.grid(row=1, column=2, sticky='w')
button_clear_entry_a.config(width=2, style='Custom.TButton')
button_clear_entry_a['takefocus'] = 0

# Создание лейблов и полей ввода конца отрезка
label_b = ttk.Label(root, text="Конец отрезка", style='Func.TLabel')
label_b.grid(row=2, column=0, padx=10, pady=10)
entry_b = ttk.Entry(root)
entry_b.config(validate="key", validatecommand=(root_validate_int, "%P"))
entry_b.grid(row=2, column=1, padx=10, pady=10)
button_clear_entry_b = ttk.Button(root, text="X", command=lambda: entry_b.delete(0, 'end'))
button_clear_entry_b.grid(row=2, column=2, sticky='w')
button_clear_entry_b.config(width=2, style='Custom.TButton')
button_clear_entry_b['takefocus'] = 0

# Создание проверки ввода с клавиатуры целых чисел не меньших единицы
root_validate_division_step = root.register(validate_division_step)

# Создание лейблов и полей ввода шага деления отрезка
label_h = ttk.Label(root, text="Шаг деления отрезка", style='Func.TLabel')
label_h.grid(row=3, column=0, padx=10, pady=10)
entry_h = ttk.Entry(root)
entry_h.config(validate="key", validatecommand=(root_validate_division_step, "%P"))
entry_h.grid(row=3, column=1, padx=10, pady=10)
button_clear_entry_h = ttk.Button(root, text="X", command=lambda: entry_h.delete(0, 'end'))
button_clear_entry_h.grid(row=3, column=2, sticky='w')
button_clear_entry_h.config(width=2, style='Custom.TButton')
button_clear_entry_h['takefocus'] = 0

# Создание проверки ввода с клавиатуры целых чисел не меньших единицы
root_validate_int_gr_one = root.register(validate_int_gr_one)

# Создание лейблов и полей ввода макс. кол. итераций
label_nmax = ttk.Label(root, text="Макс. кол. итераций", style='Func.TLabel')
label_nmax.grid(row=4, column=0, padx=10, pady=10)
entry_nmax = ttk.Entry(root)
entry_nmax.config(validate="key", validatecommand=(root_validate_int_gr_one, "%P"))
entry_nmax.grid(row=4, column=1, padx=10, pady=10)
button_clear_entry_nmax = ttk.Button(root, text="X", command=lambda: entry_nmax.delete(0, 'end'))
button_clear_entry_nmax.grid(row=4, column=2, sticky='w')
button_clear_entry_nmax.config(width=2, style='Custom.TButton')
button_clear_entry_nmax['takefocus'] = 0

# Создание проверки ввода с клавиатуры ЧПТ для точности
root_validate_float_range = root.register(validate_float_range)

# Создание лейблов и полей ввода точности
label_eps = ttk.Label(root, text="Точность", style='Func.TLabel')
label_eps.grid(row=5, column=0, padx=10, pady=10)
entry_eps = ttk.Entry(root)
entry_eps.config(validate="key", validatecommand=(root_validate_float_range, "%P"))
entry_eps.grid(row=5, column=1, padx=10, pady=10)
button_clear_entry_eps = ttk.Button(root, text="X", command=lambda: entry_eps.delete(0, 'end'))
button_clear_entry_eps.grid(row=5, column=2, sticky='w')
button_clear_entry_eps.config(width=2, style='Custom.TButton')
button_clear_entry_eps['takefocus'] = 0

# Создание стиля для ячеек таблицы
style.configure('Custom.Treeview', font=('Arial', 12))

# Создание таблицы
tree = ttk.Treeview(root, columns=('№ корня', '[x(i); x(i+1)]', "x", "f(x)",
                                   'Кол. итераций', 'Код ошибки'),
                    show='headings',
                    style='Custom.Treeview')
# Установки заголовков для столбцов
tree.heading('№ корня', text='№ корня')
tree.column('№ корня', anchor='center')
tree.heading('[x(i); x(i+1)]', text='[x(i); x(i+1)]')
tree.column('[x(i); x(i+1)]', anchor='center')
tree.heading("x", text="x")
tree.column('x', anchor='center')
tree.heading("f(x)", text="f(x)")
tree.column('f(x)', anchor='center')
tree.heading('Кол. итераций', text='Кол. итераций')
tree.column('Кол. итераций', anchor='center')
tree.heading('Код ошибки', text='Код ошибки')
tree.column('Код ошибки', anchor='center')
tree.grid(row=0, column=3, rowspan=7, padx=10, pady=10)

# Создание стиля для кнопки "Рассчитать"
style.configure('Calculate.TButton', foreground='blue',
                font=('Arial', 12, 'bold'))
# Добавление кнопки "Рассчитать"
calc_button = ttk.Button(root, text="Рассчитать", style='Calculate.TButton',
                         command=lambda: get_roots(entry_func, entry_a,
                                                   entry_b, entry_h,
                                                   entry_nmax, entry_eps,
                                                   tree, messagebox, function_graph_button))
calc_button.grid(row=7, column=0, padx=10, pady=10)

# Создание стиля для кнопки "Очистить поля"
style.configure('Clear.TButton', foreground='red', font=('Arial', 12, 'bold'))
# Добавление кнопки "Очистить"
clear_button = ttk.Button(root, text="Очистить поля", style='Clear.TButton',
                          command=lambda: clear_inputs(entry_func,
                                                       entry_a, entry_b, entry_h,
                                                       entry_nmax, entry_eps))
clear_button.grid(row=7, column=1, padx=10, pady=10)

# Создание кнопки "Очистить таблицу"
clear_table_button = ttk.Button(root, text="Очистить таблицу", style='Clear.TButton',
                                command=lambda: clear_table(tree, function_graph_button))
clear_table_button.grid(row=7, column=3, padx=10, pady=10, sticky='e')

# Создание стиля для кнопки "График функции"
style.configure('Graph.TButton', foreground='purple', font=('Arial', 12, 'bold'))

# Создание кнопки "График функции"
function_graph_button = ttk.Button(root, text="График функции", style='Graph.TButton',
                                   command=lambda: create_function_graph(tree, entry_func,
                                                                         entry_a, entry_b, messagebox))
function_graph_button.grid(row=7, column=3, padx=10, pady=10, sticky='w')
function_graph_button.grid_remove()

# Создание меню с разделенными категориями
menubar = tk.Menu(root)

# Меню "Действия"
action_menu = tk.Menu(menubar, tearoff=0)
action_menu.add_command(label="Рассчитать", command=lambda: get_roots(entry_func, entry_a,
                                                                      entry_b, entry_h,
                                                                      entry_nmax, entry_eps,
                                                                      tree, messagebox, function_graph_button))

# Меню "Очистка"
clear_menu = tk.Menu(menubar, tearoff=0)
clear_menu.add_command(label="Очистить поля", command=lambda: clear_inputs(entry_func,
                                                                           entry_a, entry_b, entry_h,
                                                                           entry_nmax, entry_eps))
clear_menu.add_command(label="Очистить таблицу", command=lambda: clear_table(tree, function_graph_button))
clear_menu.add_command(label="Очистить все", command=lambda:
clear_all(tree, entry_func, entry_a, entry_b,
          entry_h, entry_nmax, entry_eps, function_graph_button))

# Меню "Информация"
info_menu = tk.Menu(menubar, tearoff=0)
info_menu.add_command(label="О программе", command=lambda: display_info(messagebox))
info_menu.add_command(label="Коды ошибки", command=lambda: error_info(messagebox))

# Добавление меню в основное меню
menubar.add_cascade(label="Действия", menu=action_menu)
menubar.add_cascade(label="Очистка", menu=clear_menu)
menubar.add_cascade(label="Информация", menu=info_menu)

# Привязка меню к корневому окну
root.config(menu=menubar)

# Запуск окна
root.mainloop()
