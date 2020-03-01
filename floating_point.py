

def get_number():
    number = input("Ingresa el número: ")
    return number

def dec_to_base(data, base):
    output_vector = []
    while data != 0:
        output_vector.append(data%base)
        data = int(data/base)
    output_vector.reverse()
    return output_vector

def fractional_part():
    pass

if __name__ == "__main__":
    initial_number = get_number()
    integer_part = dec_to_base(initial_number, 2)
    