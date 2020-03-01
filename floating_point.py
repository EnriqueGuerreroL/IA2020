def det_sign(number):
    sign = []
    if number < 0:
        sign.append(1)
    else:
        sign.append(0)
    return sign


def dec_to_base(number, base):
    output_vector = []
    while number != 0:
        output_vector.append(number % base)
        number = int(number/base)
    output_vector.reverse()
    return output_vector


def fractional_part(number):
    int_pt = []
    while number != 0:
        new_number = (number * 2)
        number = new_number % 1
        int_pt.append(int(new_number))
    return int_pt


def complete_vector(vector):
    while len(vector) < 23:
        vector.append(0)
    return vector


if __name__ == "__main__":
    input_num = float(input("Ingresa el número: "))
    int_input_num = int(input_num)
    fract_input_num = input_num - int_input_num
    epsilon = 127

    fp_sign = det_sign(input_num)
    fp_integer_part = dec_to_base(int_input_num, 2)[1:]
    fp_fractional_part = fractional_part(fract_input_num)
    fp_mantissa = complete_vector(fp_integer_part + fp_fractional_part)
    fp_exponent = dec_to_base(epsilon + len(fp_integer_part), 2)
    fp_total = fp_sign + fp_exponent + fp_mantissa
