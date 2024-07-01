import tkinter as tk
from tkinter import messagebox

from arithmetic import *


# Функция для очистки поля ввода
def clear_input(entry):
    entry.delete(0, 'end')  # Удаляет с 0 до конца


# Функция для очистки результата
def clear_result(result_label):
    result_label.config(text="Результат:")  # Устанавливает текстовое содержимое для виджета


# Функция для точности
def clear_accuracy(accuracy_entry):
    accuracy_entry.delete(0, 'end')  # Удаляет с 0 до конца


# Функция для очистки всех полей
def clear_all(entry, result_label, accuracy_entry):
    clear_input(entry)
    clear_result(result_label)
    clear_accuracy(accuracy_entry)


# Функция для вывода информации
def display_info():
    messagebox.showinfo("О программе",
                        "Проект представляет собой приложение, созданное с использованием модуля "
                        "Tkinter разработки оконных приложений, и предназначенное для "
                        "конвертации вещественных чисел из десятичной системы счисления "
                        "в двоичную и обратно. Интерфейс приложения обеспечивает возможность "
                        "ввода данных, включая числа и знаки операций, как с использованием "
                        "клавиатуры, так и с помощью кнопок приложения.\n\nВ приложении также "
                        "создано меню, в котором содержатся пункты, дублирующие действия указанных "
                        "кнопок, а также пункт для отображения всплывающего окна с информацией о "
                        "программе и авторе.\n\n"
                        "Автор проекта: Абдуллаев Шахмар ИУ7-24Б")


"""def check_float(input_val):
    print(input_val)
    if (input_val == '-' or input_val == '+'):
        print('1!!')
        return True
    elif input_val.replace('-', '', 1).replace(".", "", 1).isdigit() or \
            input_val.replace('+', '', 1).replace(".", "", 1).isdigit():
        print('2!!')
        return True
    elif input_val == "":
        print('3!!')
        return True
    return False"""


# Функция для проверки ввода вещественного числа со знаком
def check_float(input_val):
    if input_val == "00" or input_val != input_val.strip():
        return False
    if input_val in {'-', '+'} or input_val == '':
        return True
    try:
        float(input_val)
        return True
    except ValueError:
        return False


# Функция для добавления символов в поле ввода
def add_to_entry(entry, value):
    if value == "i":
        display_info()
    elif value == "\u2190":
        entry.delete(len(entry.get()) - 1)  # Удаляет символ в позиции len(entry.get()) - 1
    elif value == "C":
        entry.delete(0, 'end')  # Удаляет с 0 до конца
    else:
        entry.insert(entry.index(tk.INSERT), value)  # Вставка текста справа от курсора


# Проверка правильности заполнения точности вывода
def check_accuracy_emptiness(accuracy_entry):
    accuracy = accuracy_entry.get()
    if accuracy == "":
        messagebox.showerror("Ошибка", "Введите корректное точность ввода")
        return None
    return int(accuracy)


# Функция для перевода из 10сс во 2сс
def decimal_to_binary(entry, accuracy_entry, result_label):
    accuracy = check_accuracy_emptiness(accuracy_entry)
    if accuracy is None:
        return
    if entry.get() == '':
        messagebox.showerror("Ошибка", "Введите корректное вещественное число")
        return
    try:
        user_text = f"Результат: {algorithm_decimal_to_binary(entry.get(), accuracy)}"
        result_label.config(text=user_text)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное вещественное число")


# Функция для перевода из 2сс в 10сс
def binary_to_decimal(entry, accuracy_entry, result_label):
    accuracy = check_accuracy_emptiness(accuracy_entry)
    if accuracy is None:
        return
    if not all(map(lambda x: x in '01.+-', list(entry.get()))) or entry.get() == '' or entry.get()[-1] == ".":
        messagebox.showerror("Ошибка", "Введите корректное двоичное число")
        return
    try:
        user_text = f"Результат: {algorithm_binary_to_decimal(entry.get(), accuracy)}"
        result_label.config(text=user_text)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное двоичное число")


def check_accuracy(accuracy_val):
    if accuracy_val == "":  # Разрешаем пустой ввод
        return True
    try:
        value = int(accuracy_val)  # Преобразуем введенное значение в целое число
        return 1 <= value <= 10  # Ограничиваем значение от 0 до 10
    except ValueError:
        return False


# Функция для уменьшения точности вывода
def reduced_accuracy(accuracy_entry):
    if accuracy_entry.get() == '':
        accuracy_entry.insert(0, 10)
        return
    new_value = int(accuracy_entry.get()) - 1
    if not new_value < 1:
        accuracy_entry.delete(0, "end")  # Удаляем текущее значение
        accuracy_entry.insert(0, new_value)  # Вставляем новое значение


# Функция для увелечения точности вывода
def improved_accuracy(accuracy_entry):
    if accuracy_entry.get() == '':
        accuracy_entry.insert(0, 1)
        return
    new_value = int(accuracy_entry.get()) + 1
    if not new_value > 10:
        accuracy_entry.delete(0, "end")  # Удаляем текущее значение
        accuracy_entry.insert(0, new_value)  # Вставляем новое значение
