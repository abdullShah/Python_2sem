from math import sin, cos


def f(x):
    return sin(x)


def derivative_f(x):
    return cos(x)

def derivative_derivative_f(x):
    return -sin(x)

def newton_method(func, func_derivative, a, b, eps, max_iter=1000):
    test_1 = a - func(a) / func_derivative(a)
    test_2 = b - func(b) / func_derivative(b)
    c = (a+b)/2
    test_3 = c - func(c) / func_derivative(c)

    if test_1 >= a and test_1 <= b:
        x_prev = a
    
    elif test_2 >= a and test_2 <= b:
        x_prev = b

    else:
        x_prev = c

    """if f(a) * derivative_derivative_f(a) > 0:
        x_prev = a
    else:
        x_prev = b"""

    
    for _ in range(max_iter):
        x_next = x_prev - func(x_prev) / func_derivative(x_prev)
        if abs(f(x_next)) <= eps:
            return x_next
        x_prev = x_next

    return x_prev
