def get_input():
    a_input = float(input("Ingresa el número: "))
    return a_input


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


def fix_vector(vector):
    if(len(vector) > 23):
        vector = vector[:23]
    else:
        while len(vector) < 23:
            vector.append(0)
    return vector


def list_as_string(some_list):
    a_string = ""
    for char in some_list:
        a_string += str(char)
    return a_string


def to_fp_format():
    input_num = get_input()
    int_input_num = int(input_num)
    fract_input_num = input_num - int_input_num
    epsilon = 127

    fp_sign = det_sign(input_num)
    fp_int_part = dec_to_base(int_input_num, 2)[1:]
    fp_fract_part = fractional_part(fract_input_num)
    fp_mantissa = fix_vector(fp_int_part + fp_fract_part)
    fp_exponent = dec_to_base(epsilon + len(fp_int_part), 2)
    return list_as_string(fp_sign + fp_exponent + fp_mantissa)
