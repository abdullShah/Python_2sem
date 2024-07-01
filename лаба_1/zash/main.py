"""
Абдуллаев Шахмар ИУ7-24Б
"""
import tkinter as tk
from act import *

root = tk.Tk()
root.geometry("520x600")
root.resizable(False, False)
root.title("Защита")

entry = tk.Entry(root, font=("Arial", 14), bd=2, relief=tk.SOLID)
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

from_pram_to_obrat_button = tk.Button(button_frame, text="Перевести",
                                     bg="lightblue", fg="black",
                                     font=("Arial", 12, "bold"),
                                     borderwidth=1, border=4,
                                     relief=tk.RAISED,
                                     command=lambda: perevesti(entry, result_obrat_label, result_dop_label))
from_pram_to_obrat_button.grid(row=0, column=0, padx=5, pady=5)


result_obrat_label = tk.Label(root, text="Результат обратного кода: ",
                        font=("Helvetica", 16, "bold"),
                        bg="light green", fg="navy",
                        relief=tk.RIDGE,
                        padx=10, pady=10)
result_obrat_label.pack(pady=10, padx=10)


result_dop_label = tk.Label(root, text="Результат дополнительного кода: ",
                        font=("Helvetica", 16, "bold"),
                        bg="light green", fg="navy",
                        relief=tk.RIDGE,
                        padx=10, pady=10)
result_dop_label.pack(pady=10, padx=10)

root.mainloop()