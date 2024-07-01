import math


# Функция для подготовки данных к выгрузке в таблицу
def preparation(data):
    for item in data:
        if 'x' in item:
            if item["x"] != '-':
                item["x"] = f"{item['x']:.6g}"
        if 'f(x)' in item:
            if item["f(x)"] != '-':
                item["f(x)"] = f"{item['f(x)']:.1e}"
    return data


# Функция вычисляет производную в точке x
def derivative(f, x):
    h = 0.0001
    return (f(x + h) - f(x)) / h


# Функция вычисляет вторую производную в точке x
def second_derivative(f, x):
    h = 0.0001
    return (f(x + 2*h) - 2*f(x + h) + f(x)) / (h**2)



# Функция для проверки, есть ли корень на отрезке
def is_root(f, a, b):
    return f(a) * f(b) <= 0


# Функция для проверки определенности функции в каждой точке своего отрезка
def is_function_defined_on_interval(f, a, b):
    num_points = 1_000
    interval = [a + i * (b - a) / num_points for i in range(num_points + 1)]
    for point in interval:
        try:
            f(point)
        except Exception:
            return False, point
    return True, -1


# Функция для нахождения всех корней
def find_roots(f, a, b, h, nmax, eps):
    succ, point = is_function_defined_on_interval(f, a, b)
    if not succ:
        return [], f"Функция прерывна на исходном отрезке в точке {point}"

    arr_roots = []
    len_iter = math.ceil((b - a) / h)
    num_root = 1
    for cnt in range(len_iter):
        statistics = {"number": num_root}
        start = a + h * cnt
        end = a + h * (cnt + 1)
        statistics["section"] = f"[{start:.2g}; {end:.2g}]"
        root, iteration, status = find_root_on_elementary_segment(f, start, end, nmax, eps)
        statistics["status"] = status
        if status == 0:  # Успешное нахождение корня
            if len(arr_roots) != 0 and arr_roots[-1]["x"] != "-" and abs(root - arr_roots[-1]["x"]) < eps:
                continue
            statistics["x"] = root
            statistics["f(x)"] = f(root)
            statistics["iteration"] = iteration
        else:
            statistics["x"] = '-'
            statistics["f(x)"] = '-'
            statistics["iteration"] = '-'
        # if status != -1:  # Все другие ошибки, кроме "корня нет"
        arr_roots.append(statistics)
        num_root += 1

    return arr_roots, ''

def preparation_find_roots(f, a, b, h, nmax, eps):
    arr_roots, status = find_roots(f, a, b, h, nmax, eps)
    return preparation(arr_roots), status


# Функция для нахождения корня на элементарном отрезке
# комбинированным методом (хорд и касательных)
def find_root_on_elementary_segment(f, a, b, nmax, eps):
    # Проверка на существования корня на данном отрезке
    if not is_root(f, a, b):
        return None, None, -1

    # Устанавливаем начальные значения
    x0, x1 = a, b  

    for n in range(1, nmax + 1):
        # Проверяем знаки функции на концах отрезка
        if f(x0) * f(x1) < 0:
            # Вычисляем новую аппроксимацию методом хорд
            x2 = x0 - f(x0) / (f(x1) - f(x0)) * (x1 - x0) 
        else:
            # Пытаемся вычислить новую аппроксимацию методом касательных
            try:
                x2 = x1 - f(x1) / derivative(f, x1)  
            except:
                return None, None, 2

        # Проверка сходимости с помощью точности
        if abs(x2 - x1) < eps:
            if a <= x2 <= b:
                return x2, n, 0
            return None, None, 3
            
        
        # Вычисление следующих точек итерации
        if f(x0) * f(x1) < 0:
            x0, x1 = x0, x2
        else:
            x0, x1 = x1, x2

    # Корень не найден
    return None, None, 1
