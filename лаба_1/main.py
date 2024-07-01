"""
Абдуллаев Шахмар ИУ7-24Б
Приложение разработано для перевода вещественного числа из 10-й счисления в 2-ю и обратно.
"""
from action import *

# Создание главного окна
root = tk.Tk()
root.geometry("520x600")  # Задание размера окна
root.resizable(False, False)  # Запрет изменение размера окна
root.title("Конвертер чисел")  # Заголовок окна

# Создание заголовка
label = tk.Label(root, text="Введите число:", font=("Arial", 16))  # Создание виджета
label.pack(pady=10)  # Отображение виджета

# Создание поля для ввода
validation_input = root.register(check_float)  # Регистрируем функцию в качестве функции проверки
entry = tk.Entry(root, font=("Arial", 14), bd=2, relief=tk.SOLID,
                 validate="key",  # Режим валидации при каждом вводе символов
                 # Связывает функцию validation с полем ввода, %P представляет введенную строку перед её валидацией
                 validatecommand=(validation_input, '%P'))
entry.pack(pady=10)  # Отображение виджета

# Создание клавиатуры
keyboard_frame = tk.Frame(root)  # Создание виджета
keyboard_frame.pack(pady=10)  # Отображение виджета

# Создание кнопок для цифр
array_of_buttons = ["0", "1", "2", "+", "3", "4", "5", "-", "6", "7", "8", ".", "9", "\u2190", "C", "i"]
for i in range(len(array_of_buttons)):
    button = tk.Button(keyboard_frame,
                       text=array_of_buttons[i],
                       fg="black",
                       font=("Arial", 12, "bold"),
                       width=5, height=2,
                       borderwidth=1, border=4,
                       relief=tk.RAISED,
                       command=lambda q=i: add_to_entry(entry, array_of_buttons[q]))
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

# Создание кнопок перевода
button_frame = tk.Frame(root)  # Создание фрейма для размещения кнопок
button_frame.pack()  # Отображение фрейма

# Создание кнопки для перевода из 10сс во 2сс
decimal_to_binary_button = tk.Button(button_frame, text="10 \u2192 2",
                                     bg="lightblue", fg="black",
                                     font=("Arial", 12, "bold"),
                                     borderwidth=1, border=4,
                                     relief=tk.RAISED,
                                     command=lambda: decimal_to_binary(entry, accuracy_entry, result_label))
decimal_to_binary_button.grid(row=0, column=0, padx=5, pady=5)

# Создание кнопки для перевода из 2сс в 10сс
binary_to_decimal_button = tk.Button(button_frame, text="2 \u2192 10",
                                     bg="lightblue", fg="black",
                                     font=("Arial", 12, "bold"),
                                     borderwidth=1, border=4,
                                     relief=tk.RAISED,
                                     command=lambda: binary_to_decimal(entry, accuracy_entry, result_label))
binary_to_decimal_button.grid(row=0, column=1, padx=5, pady=5)

# Создание фрейма для размещения метки и поля ввода в одном ряду
accuracy_frame = tk.Frame(root)
accuracy_frame.pack(pady=10)

# Создание метки для поля ввода точности
accuracy_label = tk.Label(accuracy_frame, text="Точность вывода:", font=("Arial", 12))
accuracy_label.grid(row=0, column=0, padx=5)

# Создание кнопки для уменьшения точности вывода
reduced_accuracy_button = tk.Button(accuracy_frame, text="-", font=("Arial", 16), border=0,
                                    command=lambda: reduced_accuracy(accuracy_entry))
reduced_accuracy_button.grid(row=0, column=1, padx=5)

# Создание поля для ввода точности
validation_accuracy = root.register(check_accuracy)  # Регистрируем функцию в качестве функции проверки
accuracy_entry = tk.Entry(accuracy_frame, font=("Arial", 12), width=5,
                          validate="key",  # Режим валидации при каждом вводе символов
                          # Связывает функцию с полем ввода, %P представляет введенную строку перед её валидацией
                          validatecommand=(validation_accuracy, '%P'))
accuracy_entry.grid(row=0, column=2, padx=5)
accuracy_entry.insert(0, "5")  # Значение по умолчанию

# Создание кнопки для увеличения точности вывода
improved_accuracy_button = tk.Button(accuracy_frame, text="+", font=("Arial", 16), border=0,
                                     command=lambda: improved_accuracy(accuracy_entry))
improved_accuracy_button.grid(row=0, column=3, padx=5)

# Создание места для вывода
result_label = tk.Label(root, text="Результат:",
                        font=("Helvetica", 16, "bold"),
                        bg="light green", fg="navy",
                        relief=tk.RIDGE,
                        padx=10, pady=10)
result_label.pack(pady=10, padx=10)

# Создание кнопки очистки
clear_result_button = tk.Button(root, text="Очистить результат",
                                bg="light coral", fg="white",
                                font=("Arial", 12, "bold"),
                                borderwidth=1, border=4,
                                relief=tk.RAISED,
                                command=lambda: clear_result(result_label))
clear_result_button.pack()

# Создание меню с разделенными категориями
menubar = tk.Menu(root)

# Меню "Действия"
action_menu = tk.Menu(menubar, tearoff=0)
action_menu.add_command(label="10 \u2192 2", command=lambda: decimal_to_binary(entry, accuracy_entry, result_label))
action_menu.add_command(label="2 \u2192 10", command=lambda: binary_to_decimal(entry, accuracy_entry, result_label))

# Меню "Очистка"
clear_menu = tk.Menu(menubar, tearoff=0)
clear_menu.add_command(label="Очистить поле", command=lambda: clear_input(entry))
clear_menu.add_command(label="Очистить результат", command=lambda: clear_result(result_label))
clear_menu.add_command(label="Очистить точность", command=lambda: clear_accuracy(accuracy_entry))
clear_menu.add_command(label="Очистить все", command=lambda: clear_all(entry, result_label, accuracy_entry))

# Меню "Информация"
info_menu = tk.Menu(menubar, tearoff=0)
info_menu.add_command(label="О программе", command=display_info)

# Добавление меню в основное меню
menubar.add_cascade(label="Действия", menu=action_menu)
menubar.add_cascade(label="Очистка", menu=clear_menu)
menubar.add_cascade(label="Информация", menu=info_menu)

# Привязка меню к корневому окну
root.config(menu=menubar)

# Запуск главного цикла событий
root.mainloop()
