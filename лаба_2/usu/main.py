import tkinter as tk
from tkinter import messagebox
from tools import *

def calculate_root():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        eps = float(entry_eps.get())

        if a >= b:
            messagebox.showerror("Ошибка", "Значение a должно быть меньше b")
            return

        root = stefenson_method(f, a, b, eps)

        result_label.config(text=f"Корень функции: {root:.6f}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные значения")

# Создание главного окна
root = tk.Tk()
root.title("Поиск корня")

# Создание элементов управления
label_a = tk.Label(root, text="a")
label_a.grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=5)

label_b = tk.Label(root, text="b")
label_b.grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=5)

label_eps = tk.Label(root, text="Точность")
label_eps.grid(row=2, column=0, padx=5, pady=5)
entry_eps = tk.Entry(root)
entry_eps.grid(row=2, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Вычислить", command=calculate_root)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
