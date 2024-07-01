from math import sin, cos


def f(x):
    return sin(x)


def derivative_f(x):
    return cos(x)


def newton_method(func, func_derivative, a, b, eps, max_iter=1000):
    x_prev = (a + b) / 2
    for _ in range(max_iter):
        x_next = x_prev - func(x_prev) / func_derivative(x_prev)
        if abs(x_next - x_prev) < eps:
            return x_next
        x_prev = x_next
    return x_prev


def simplified_newton_method(func, func_derivative, a, b, eps, max_iter=1000):
    x_prev = (a + b) / 2
    q = func_derivative(x_prev)
    for _ in range(max_iter):
        x_next = x_prev - func(x_prev) / q
        if abs(x_next - x_prev) < eps:
            return x_next
        x_prev = x_next
    return x_prev


def simple_iter_method(func, func_derivative, a, b, eps, max_iter=1000):
    x = (a + b) / 2
    for _ in range(max_iter):
        x_next = x - func(x) / func_derivative(x)
        if abs(x_next - x) < eps:
            return x_next
        x = x_next
    return x


def bisection_method(func, a, b, eps):
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if abs(func(c)) < 1e-8:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# def bisection_method(func, a, b, eps, max_iter=1000):
#     for _ in range(max_iter):
#         c = (a + b) / 2
#         if abs(b - a) / 2 <= eps or abs(func(c)) < 1e-8:
#             return c
#         elif func(c) * func(a) < 0:
#             b = c
#         else:
#             a = c
#     return (a + b) / 2


def secant_method(func, a, b, eps):
    x0, x1 = a, b
    while abs(x1 - x0) >= eps:
        x_next = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        x0, x1 = x1, x_next
    return x1


# def secant_method(func, a, b, eps, max_iter=1000):
#     x0, x1 = a, b
#     for _ in range(max_iter):
#         x_next = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
#         if abs(x_next - x1) < eps:
#             return x_next
#         x0, x1 = x1, x_next
#     return x1


def chord_method(func, a, b, eps):
    while abs(b - a) > eps:
        c = a - func(a) / (func(b) - func(a)) * (b - a)
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# def chord_method(func, a, b, eps, max_iter=1000):
#     for _ in range(max_iter):
#         c = a - func(a) / (func(b) - func(a)) * (b - a)
#         if abs(b - a) <= eps or func(c) == 0:
#             return c
#         elif func(c) * func(a) < 0:
#             b = c
#         else:
#             a = c
#     return (a + b) / 2


def stefenson_method(func, a, b, eps, max_iter=1000):
    x0 = (a + b) / 2
    iter_count = 0
    while True:
        x_next = x0 - (func(x0) ** 2) / (func(x0 + func(x0)) - func(x0))
        iter_count += 1
        if abs(x_next - x0) < eps or iter_count >= max_iter:
            return x_next
        x0 = x_next
