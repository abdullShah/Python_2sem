from arithmetic import *
from graphics import *
from math import *

# Функция для вывода информации о проекте
def display_info(messagebox):
    messagebox.showinfo("О программе",
                        "Проект представляет собой приложение для вычисления корней функции "
                        "на отрезке [a; b] определенным методом, используя модуль создания оконных "
                        "приложений Tkinter.\n\nДля вычисления отрезок [a; b] делится на элементарные "
                        "отрезки с шагом h. Гарантируется, что на каждом элементарном отрезке "
                        "у функции не более одного корня. Для каждого элементарного отрезка, "
                        "на котором есть корень, итерационно вычисляется приближенное значение "
                        "корня с заданной точностью eps. Для обнаружения медленного процесса "
                        "сходимости или расходимости метода количество итераций ограничивается"
                        "числом Nmax.\n\n"
                        "Автор проекта: Абдуллаев Шахмар ИУ7-24Б")


# Функция для вывода информации о кодах ошибках
def error_info(messagebox):
    messagebox.showinfo("Коды ошибки",
                        "-1 - нет корня на данном интервале\n\n"
                        "0 – корень вычислен успешно\n\n"
                        "1 – превышено максимальное число итераций\n\n"
                        "2 - произошло деление на 0\n\n"
                        "3 – найденный корень лежит за пределами отрезка\n\n")


# Функция-справочник для пользователя о вводе функции
def func_info(messagebox):
    messagebox.showinfo("Ввод функции",
                        "При работе с математическими функциями, важно учитывать "
                        "особенности написания и использования выражений. Для "
                        "того, чтобы успешно использовать математические функции, "
                        "следуйте указанным ниже правилам, чтобы язык Python смог их "
                        "обработать:\n\n"
                        "Арифметические операции: Python поддерживает основные "
                        "математические операции, такие как сложение (+), вычитание "
                        "(-), умножение (*), деление (/) и возведение в степень (**). "
                        "Например: 2 + 3, 5 - 1, 2 * 4, 8 / 2, 3 ** 2.\n\n"
                        "Модуль math: Для более сложных математических операций в "
                        "Python можно использовать встроенный модуль math, который "
                        "предоставляет доступ к дополнительным математическим функциям. "
                        "Например: sin, cos и т.д.\n\n"
                        "Приоритет операций: При написании выражений в Python важно "
                        "помнить о приоритете операций. Умножение и деление имеют более "
                        "высокий приоритет, чем сложение и вычитание. Если необходимо "
                        "изменить порядок операций, используйте скобки. Например: 2 * "
                        "(3 + 4).\n\n"
                        "Переменные: Если вы хотите использовать переменные в выражении, "
                        "убедитесь, что они определены в виде x. Вводите сразу функцию, без y.\n\n"
                        "При невыполнений правил использования интерфейса не гарантируется корректная "
                        "работа приложения!"
                        )


# Валидатор для ввода целых чисел
def validate_int(enter):
    if enter != enter.strip():
        return False
    elif enter in ["+00", "00", "-00"]:
        return False

    if len(enter) >= 2 and "." in enter and enter.count(".") == 1:
        try:
            float(enter)
            return True
        except ValueError:
            return False
    
    elif (len(enter) > 2 and ("+0" == enter[:2] or "-0" == enter[:2])) or \
            (len(enter) > 1 and ("0" == enter[0])):
        return False
    elif enter.isdigit():
        return True
    elif len(enter) == 1 and (enter.startswith("-") and enter.count("-") == 1 \
                              or enter.startswith("+") and enter.count("+") == 1):
        return True
    elif enter == "" or (enter.startswith("-") and enter[1:].isdigit()) \
            or (enter.startswith("+") and enter[1:].isdigit()):
        return True

    '''if len(enter) >= 2 and enter[-1] == "e" and enter.count("e") == 1:
        return True
    
    if len(enter) >= 3 and enter[-2] == "e" and (enter[-1] == "-" or enter[-1] == "+") and enter.count("e") == 1:
        return True

    if len(enter) > 4 and enter[-3] == "e" and (enter[-2] == "-" or enter[-2] == "+") and enter.count("e") == 1:
        if not enter[enter.find("+")+enter.find("-")+1:].isdigit():
            return False

        if enter[-1:] == "00":
            return False

        return True'''


    return False


# Валидатор для ввода шага деления отрезка
def validate_division_step(enter):
    if enter != enter.strip():
        return False
    if enter == "":
        return True

    if enter[0] == "-" or enter[0] == "+":
        return False

    try:
        float(enter)
        return True
    except ValueError:
        return False


# Валидатор для ввода целых чисел не меньших единицы
def validate_int_gr_one(enter):
    if enter != enter.strip():
        return False
    if enter == "":
        return True

    try:
        number = int(enter)
        return number >= 1
    except ValueError:
        return False


# Валидатор для ввода точности
def validate_float_range(enter):
    if enter != enter.strip():
        return False
    if enter == "":
        return True

    if enter == "1":
        return True

    if len(enter) == 2 and enter[1] == "e":
        return True

    if len(enter) == 3 and enter[1] == "e" and enter[2] == "-":
        return True

    if len(enter) > 3 and enter[1] == "e" and enter[2] == "-":
        if not enter[3:].isdigit():
            return False

        if enter[3:5] == "00":
            return False

        return True

    if len(enter) >= 2 and enter[:2] == "0." and enter.count(".") == 1:
        try:
            float(enter)
            return True
        except ValueError:
            return False

    if enter == "0":
        return True

    return False


# Валидатор для ввода функции
def validate_function(enter):
    if enter != enter.strip():
        return False
    if enter == "":
        return True
    return True


# Функция для проверки мат. функции
def check_func(func):
    if len(func) == 0:
        return False
    try:
        test = lambda x: eval(func)

        test(1)
        return True
    except Exception:
        return False


# Функция для создания мат. функции
def create_function(func):
    def function(x):
        return eval(func)

    return function


# Функция для проверки начала отрезка
def check_a(a):
    if len(a) == 0:
        return False
    try:
        a = float(a)
        return True
    except ValueError:
        return False


# Функция для проверки конца отрезка
def check_b(b, a):
    if len(b) == 0 or len(str(a)) == 0:
        return False
    try:
        b = float(b)
    except ValueError:
        return False

    if b <= a:
        return False
    return True


# Функция для проверки шага деления отрезка
def check_h(h):
    if len(h) == 0:
        return False
    try:
        h = float(h)
        return True
    except ValueError:
        return False


# Функция для проверки макс. кол. итераций
def check_nmax(nmax):
    if len(nmax) == 0:
        return False
    try:
        nmax = int(nmax)
    except ValueError:
        return False

    if nmax < 1:
        return False
    return True


# Функция для проверки точности
def check_eps(eps):
    if len(eps) == 0:
        return False
    try:
        eps = float(eps)
    except ValueError:
        return False

    if not (0 < eps <= 1):
        return False
    return True


# Функция для добавления данных в таблицу
def add_table(tree, data):
    for item in data:
        values = (item['number'], item['section'], item['x'], item['f(x)'], item['iteration'], item['status'])
        tree.insert('', 'end', values=values)


# Функция для очистки таболицы
def clear_table(tree, function_graph_button):
    for item in tree.get_children():
        tree.delete(item)
    function_graph_button.grid_remove()


# Функция для полей ввода
def clear_inputs(entry_func, entry_a, entry_b, entry_h, entry_nmax, entry_eps):
    entry_func.delete(0, 'end')
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
    entry_h.delete(0, 'end')
    entry_nmax.delete(0, 'end')
    entry_eps.delete(0, 'end')


# Функция для очистки всех полей
def clear_all(tree, entry_func, entry_a, entry_b,
              entry_h, entry_nmax, entry_eps,
              function_graph_button):
    clear_table(tree, function_graph_button)
    clear_inputs(entry_func, entry_a, entry_b, entry_h, entry_nmax, entry_eps)


# Функция для получения данных о корней мат. функции на отрезке
def get_roots(entry_func, entry_a, entry_b, entry_h, entry_nmax, entry_eps, tree, messagebox, function_graph_button):
    func = entry_func.get()
    if not check_func(func):
        messagebox.showerror("Ошибка", "Введена некорректная функция")
        return
    func = create_function(func)

    a = entry_a.get()
    if not check_a(a):
        messagebox.showerror("Ошибка", "Введено некорректное начало отрезка")
        return
    a = float(a)

    b = entry_b.get()
    if not check_b(b, a):
        messagebox.showerror("Ошибка", "Введен некорректный конец отрезка")
        return
    b = float(b)

    h = entry_h.get()
    if not check_h(h):
        messagebox.showerror("Ошибка", "Введен некорректный шаг деления отрезка")
        return
    h = float(h)

    nmax = entry_nmax.get()
    if not check_nmax(nmax):
        messagebox.showerror("Ошибка", "Введено некорректное максимальное количество итераций")
        return
    nmax = int(nmax)

    eps = entry_eps.get()
    if not check_eps(eps):
        messagebox.showerror("Ошибка", "Введена некорректная точность")
        return
    eps = float(eps)

    # Далее выполняется расчет с заданными входными параметрами
    arr_new_values, text = preparation_find_roots(func, a, b, h, nmax, eps)

    if len(text) != 0:
        messagebox.showerror("Ошибка", f"{text}")
        return

    if len(arr_new_values) == 0:
        messagebox.showerror("Ошибка", "На этом отрезке нет корней для веденной функции")
        return

    # Обновление таблицы
    clear_table(tree, function_graph_button)
    add_table(tree, arr_new_values)
    function_graph_button.grid()


# Функция для получения данных из таблицы
def get_data(tree):
    x_values = []
    y_values = []
    for row in tree.get_children():
        data = tree.item(row)['values']
        if data[2] != '-' and data[3] != '-':
            x_values.append(float(data[2]))
            y_values.append(float(data[3]))
    return x_values, y_values


# Функция для создания графика мат. функции
def create_function_graph(tree, entry_func, entry_a, entry_b, messagebox):
    if not tree.get_children():
        messagebox.showerror("Ошибка", "Таблица корней пуста")
        return

    func = entry_func.get()
    if not check_func(func):
        messagebox.showerror("Ошибка", "Введена некорректная функция")
        return
    func = create_function(func)

    a = entry_a.get()
    if not check_a(a):
        messagebox.showerror("Ошибка", "Введено некорректное начало отрезка")
        return
    a = float(a)

    b = entry_b.get()
    if not check_b(b, a):
        messagebox.showerror("Ошибка", "Введен некорректный конец отрезка")
        return
    b = float(b)

    x_values, y_values = get_data(tree)

    plotting(func, entry_func.get(), a, b, x_values, y_values)
