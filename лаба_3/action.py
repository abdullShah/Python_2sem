from tkinter import filedialog, messagebox

from steganography import *


# Функция для вывода информации о проекте
def display_info():
    messagebox.showinfo("О программе",
                        "Проект заключается в создании программы с графическим интерфейсом для сокрытия "
                        "и извлечения информации из изображений в формате BMP с использованием метода "
                        "наименее значащих битов (LSB).\n\n"
                        "Программа имеет два режима работы: "
                        "1) Режим сокрытия строки: пользователь вводит строку символов, выбирает изображение  "
                        "BMP, в которое хочет спрятать эту строку, и сохраняет полученное измененное изображение. "
                        "2) Режим извлечения строки: пользователь выбирает изображение BMP, из которого хочет  "
                        "извлечь скрытую строку, и программа отображает скрытую строку.\n\n"
                        "Если длина входной строки превышает максимально возможное количество символов, которые "
                        "можно спрятать в выбранном изображении, программа должна выдавать сообщение об ошибке.\n\n"
                        "Автор проекта: Абдуллаев Шахмар ИУ7-24Б")


# Функция для обзора bmp файлов
def browse_image(image_path):
    filename = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if filename:
        image_path.set(filename)


# Функция "Сохранить как"
def save_as(converted_image_path):
    filename = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("Bitmap files", "*.bmp")])
    if filename:
        converted_image_path.set(filename)


# Функция для выполнения действий в зависимости от режима
def process(mode_var, image_path, converted_image_path, message_var, output_label):
    mode = mode_var.get()
    image_path_val = image_path.get()
    converted_image_path_val = converted_image_path.get()

    if image_path_val == "":
        messagebox.showerror("Error", "Отсутствующий путь. Укажите путь изображения")
        return

    output_label.config(text="...")

    if mode == "hide":
        message = message_var.get()
        rc, status = hide_text(image_path_val, converted_image_path_val, message)
        output_label.config(text=f"{status}")
    elif mode == "extract":
        rc, status = extract_text(image_path_val)
        if not rc:
            output_label.config(text=f"Извлеченная строка: {status}")
        else:
            output_label.config(text=f"{status}")


# Функция для переключения состояния ввода в зависимости от режима
def toggle_message_entry(mode_var, converted_image_entry, converted_image_entry_button, message_entry, tk):
    if mode_var.get() == "extract":
        message_entry.config(state=tk.DISABLED)
        converted_image_entry.config(state=tk.DISABLED)
        converted_image_entry_button.config(state=tk.DISABLED)
    else:
        message_entry.config(state=tk.NORMAL)
        converted_image_entry.config(state=tk.NORMAL)
        converted_image_entry_button.config(state=tk.NORMAL)
