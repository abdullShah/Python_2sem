from arif import *


def calculate_root(entry_a, entry_b, entry_eps, result_label):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        eps = float(entry_eps.get())

        if a >= b:
            messagebox.showerror("Ошибка", "Значение a должно быть меньше b")
            return

        root = newton_method(f, derivative_f, a, b, eps)

        result_label.config(text=f"Корень функции: {root:.6f}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные значения")
