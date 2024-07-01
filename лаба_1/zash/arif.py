def alg_from_pram_to_obrat(code):
    sign = code[0]
    new_code = code[1:]
    if sign == "0":
        return code

    return_code = ''
    for i in new_code:
        if i == "0":
            return_code += '1'
        else:
            return_code += '0'

    return sign + return_code


# print(int(from_pram_to_dop("1010")))
# print(bin(10))
# print(bin(10 | 1))

def alg_from_pram_to_dop(code):
    sign = code[0]
    new_code = code[1:]
    if sign == "0":
        return code

    # print(alg_from_pram_to_obrat(code))
    # print(int(alg_from_pram_to_obrat(code), 2))
    # print(bin(int(alg_from_pram_to_obrat(code), 2) + 1))
    return bin(int(alg_from_pram_to_obrat(code), 2) + 1)[2::]

# print(int(from_pram_to_dop("1010")))
# print(bin(10))
# print(bin(10 | 1))





