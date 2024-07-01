import tkinter as tk
from tkinter import messagebox
from tools import *


root = tk.Tk()
root.title("Поиск корня")

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

calculate_button = tk.Button(root, text="Вычислить", command=lambda: calculate_root(entry_a, entry_b, entry_eps, result_label))
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
