

def get_number():
    number = float(input("Ingresa el número: "))
    return number

def int_number(number):
    return int(number)

def dec_to_base(data, base):
    output_vector = []
    while data != 0:
        output_vector.append(data%base)
        data = int(data/base)
    output_vector.reverse()
    return output_vector

def fractional_part(number):
    # fract_pt = []
    int_pt = []
    while number != 0:
        new_number = (number * 2)
        number = new_number % 1
        # fract_pt.append(number)
        int_pt.append(int(new_number))
    return int_pt

if __name__ == "__main__":
    input_num = get_number()
    int_input_num = int_number(input_num)
    fract_input_num = input_num - int_input_num
    fp_integer_part = dec_to_base(int_input_num, 2)
    fp_fractional_part = fractional_part(fract_input_num)
    
    