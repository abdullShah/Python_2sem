from PIL import Image


# Функция для сокрытия строки в изображении
def hide_text(image_path, converted_image_path, text):
    try:
        img = Image.open(image_path)
        binary_text = ''.join(format(ord(char), '08b') for char in text)

        if len(binary_text) * 3 >= img.width * img.height:
            return 2, "Длина строки слишком большая для данного изображения"

        binary_text += '11111111'

        data_index = 0
        last_pix = 0
        for y in range(img.height):
            for x in range(img.width):
                pixel = list(img.getpixel((x, y)))

                last_pix += 1
                n = 2 if last_pix % 3 == 0 else 3

                for i in range(n):
                    if data_index < len(binary_text):
                        pixel[i] = pixel[i] & 0b11111110 | int(binary_text[data_index])
                        data_index += 1

                img.putpixel((x, y), tuple(pixel))

        img.save(converted_image_path)

        return 0, "Информация успешно сокрыта в изображении"
    except Exception as e:
        return 1, "Ошибка считывания изображения. Укажите корректный путь"


# Функция для извлечения строки из изображения
def extract_text(image_path):
    try:
        img = Image.open(image_path)
        binary_text = ''
        data = ''

        last_pix = 0
        for y in range(img.height):
            for x in range(img.width):
                pixel = img.getpixel((x, y))

                last_pix += 1
                n = 2 if last_pix % 3 == 0 else 3

                for i in range(n):
                    binary_text += str(pixel[i] & 1)
                    if len(binary_text) % 8 == 0:
                        byte = binary_text[-8:]
                        if byte == '11111111':
                            return 0, data
                        data += chr(int(byte, 2))

        return 0, data
    except Exception as e:
        return 1, "Ошибка считывания изображения. Укажите корректный путь"
