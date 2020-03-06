# Inteligenia Artificial
# Alumnos:
#   Fuentes Mora Oscar Fernando
#   Granados Gómez Nanci Noelia
#   Guerrero López Enrique
#   Pólito Seba Víctor Hugo

 # Programa que recibe como entrada un número en base diez
 # y produce como salida el número en representación de punto flotante
 # de 32 bits.

# Función que toma el dato de entrada
def get_input():
    a_input = float(input("Ingresa el número: "))
    return a_input


# Función que determina el signo del número que recibe
def det_sign(number):
    sign = []
    if number < 0:
        sign.append(1)
    else:
        sign.append(0)
    return sign


# Implementación del algoritmo revisado en clase
# para expresar un número decimal en otra base
def dec_to_base(number, base):
    output_vector = []
    while number != 0:
        output_vector.append(number % base)
        number = int(number/base)
    output_vector.reverse()
    return output_vector


# Esta función se encarga de obtener la parte fraccionaria
# de la mantisa. Recibe como dato la parte fraccionaria del 
# número a convertir (lo que va después del punto decimal).
def fractional_part(number):
    int_pt = []
    while number != 0:
        new_number = (number * 2)
        number = new_number % 1
        int_pt.append(int(new_number))
    return int_pt


# fix_vector se utiliza para adecuar la lista de entrada
# para que tenga la longitud de 23 caracteres, entonces
# puede truncar una entrada con longitud mayor o puede
# agregar ceros a la lista
def fix_vector(vector):
    if(len(vector) > 23):
        vector = vector[:23]
    else:
        while len(vector) < 23:
            vector.append(0)
    return vector


# Función que pasa el contenido de una lista a una cadena,
# se utiliza para imprimir en pantalla el resultado de formato de 
# punto flotante
def list_as_string(some_list):
    a_string = ""
    for char in some_list:
        a_string += str(char)
    return a_string


 # Aquí se lleva el flujo de las operaciones para determinar
 # la salida. La función devuelve el resultado final
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
