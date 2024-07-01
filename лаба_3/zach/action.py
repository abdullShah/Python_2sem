from tkinter import filedialog, messagebox

from sten import *


def browse_image(image_path):
    filename = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if filename:
        image_path.set(filename)


def save_as(converted_image_path):
    filename = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("Bitmap files", "*.bmp")])
    if filename:
        converted_image_path.set(filename)


def process(image_path, converted_image_path, message_var, output_label):
    image_path_val = image_path.get()
    converted_image_path_val = converted_image_path.get()

    if image_path_val == "":
        messagebox.showerror("Error", "Отсутствующий путь. Укажите путь изображения")
        return

    output_label.config(text="...")

    message = int(message_var.get())
    rc, status = binar(image_path_val, converted_image_path_val, message)
    output_label.config(text=f"{status}")
