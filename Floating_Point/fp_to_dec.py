def get_input():
    a_input = input("Ingresa el número: ")
    return a_input


def bin_to_base(bit_string, base):
    res = 0
    bit_string = bit_string[::-1]
    for pos in range(len(bit_string)):
        res += int(bit_string[pos]) * (base ** pos)
    return res


def det_first_term(input_bits):
    sign = input_bits[0]
    first_term = (-1) ** int(sign)
    return first_term


def det_second_term(input_bits):
    epsilon = 127
    exponent = bin_to_base(input_bits[1:9], 2)
    second_term = 2 ** (exponent - epsilon)
    return second_term


def det_third_term(input_bits):
    third_term = 0
    mantissa = "1" + input_bits[9:]
    for num in range(len(mantissa)):
        third_term += int(mantissa[num]) / (2 ** num)
    return third_term


def to_decimal():
    input_num = get_input()
    dec_first_term = det_first_term(input_num)
    dec_second_term = det_second_term(input_num)
    dec_third_term = det_third_term(input_num)
    dec_number = dec_first_term * dec_second_term * dec_third_term
    return dec_number
