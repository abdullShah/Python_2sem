from PIL import Image

def binar(image_path_val, converted_image_path_val, lim):
    try:
        img = Image.open(image_path_val)

        for y in range(img.height):
            for x in range(img.width):
                pixel = list(img.getpixel((x, y)))
                for i in range(3):
                    if pixel[i] < lim:
                        pixel[i] = 0
                    else:
                        pixel[i] = 255

                img.putpixel((x, y), tuple(pixel))

        img.show()
        img.save(converted_image_path_val)

        return 0, "Информация успешно сокрыта в изображении"
    except Exception as e:
        return 1, f"{str(e)}"