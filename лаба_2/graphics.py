import matplotlib.pyplot as plt


def find_extrema(f, a, b):
    step = 0.01

    x_extrema = []
    y_extrema = []

    x_values = []
    y_values = []

    # Вычисляем значения функции на заданном отрезке с заданным шагом
    x = a
    while x <= b:  # x < b + step / 2
        x_values.append(x)
        y_values.append(f(x))
        x += step

    # Проверяем каждую точку на наличие локального экстремума
    for i in range(1, len(x_values) - 1):
        if y_values[i] > y_values[i - 1] and y_values[i] > y_values[i + 1]:  # Максимум
            x_extrema.append(x_values[i])
            y_extrema.append(y_values[i])
        elif y_values[i] < y_values[i - 1] and y_values[i] < y_values[i + 1]:  # Минимум
            x_extrema.append(x_values[i])
            y_extrema.append(y_values[i])

    return x_extrema, y_extrema


def plotting(entry_func, text_func, entry_a, entry_b, x_values, y_values):
    # Определение функции
    f = entry_func

    # Определение отрезка [a; b]
    a = entry_a
    b = entry_b

    # Значения функции на отрезке [a; b]
    x = list(range(int(a * 10), int(b * 10) + 1))  # Преобразование в int для range
    y = [f(i / 10) for i in x]

    # Нарисовать график функции
    plt.plot([i / 10 for i in x], y, label=f'f(x) = {text_func}')

    # Нарисовать корни на графике
    plt.scatter(x_values, y_values, color='blue', label='Вычисленные корни')

    # Добавление локальных экстремумов
    x_extrema, y_extrema = find_extrema(f, a, b)

    # Нарисовать точки на графике
    plt.scatter(x_extrema, y_extrema, color='red', label='Локальные экстремумы')

    # Добавление подписей осей и заголовка
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'График функции {text_func} на отрезке [{a}, {b}]')

    # Отображение графика
    plt.grid(True)
    plt.legend()
    plt.show()
