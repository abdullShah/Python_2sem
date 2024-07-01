# Функция для перевода из 10сс в другое сс
def algorithm_decimal_to_binary(get_value, accuracy):
    value = get_value
    sign = ''
    if value[0] in ['-', '+']:
        sign = value[0]
        value = value[1:]
    if '.' in value:
        whole_bin, fraction_bin = map(int, value.split('.'))
        fraction_bin = float(f'0.{fraction_bin}')
    else:
        whole_bin, fraction_bin = int(value), None

    whole_output = ''
    while whole_bin > 0:
        whole_output += str(whole_bin % 2)
        whole_bin //= 2
    whole_output = whole_output[::-1]

    fraction_output = ''
    if fraction_bin is not None:
        fraction_output += '.'
        for _ in range(accuracy):
            fraction_bin *= 2
            bit = int(fraction_bin)
            fraction_output += str(bit)
            fraction_bin -= bit

    return f"{sign}{whole_output + fraction_output}"


# Функция для перевода из одного сс в 10сс
def algorithm_binary_to_decimal(get_value, accuracy):
    value = get_value
    sign = ''
    if value[0] in ['-', '+']:
        sign = value[0]
        value = value[1:]
    if '.' in value:
        whole_bin, fraction_bin = value.split('.')
    else:
        whole_bin, fraction_bin = value, None

    whole_output = 0
    for q, el in enumerate(whole_bin[::-1]):
        whole_output += int(el) * 2 ** q

    fraction_output = 0
    if fraction_bin is not None:
        for q, el in enumerate(fraction_bin):
            fraction_output += int(el) * 2 ** -(q + 1)

    return f"{sign}{whole_output + fraction_output:.{len(str(whole_output)) + accuracy}g}"
