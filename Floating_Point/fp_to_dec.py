# Inteligenia Artificial
# Alumnos:
#   Fuentes Mora Oscar Fernando
#   Granados Gómez Nanci Noelia
#   Guerrero López Enrique
#   Pólito Seba Víctor Hugo

# Programa que recibe un número en formato de punto
# flotante para expresarlo como decimal

# Función para recibir el dato de entrada
def get_input():
    a_input = input("Ingresa el número: ")
    return a_input


# Función que nos permite calcular el valor de una 
# cadena de bits según la base que se le indica
# considerando el concepto del sistema numérico 
# posicional
def bin_to_base(bit_string, base):
    res = 0
    bit_string = bit_string[::-1]
    for pos in range(len(bit_string)):
        res += int(bit_string[pos]) * (base ** pos)
    return res


# det_first_term se encarga del manejo del bit de signo,
# recibe la cadena completa de 32 bits y devuelve el valor decimal
def det_first_term(input_bits):
    sign = input_bits[0]
    first_term = (-1) ** int(sign)
    return first_term


# Esta función se encarga del manejo de la parte
# de la cadena de bits que representa el exponente, devolviendo 
# el valor decimal
def det_second_term(input_bits):
    epsilon = 127
    exponent = bin_to_base(input_bits[1:9], 2)
    second_term = 2 ** (exponent - epsilon)
    return second_term


# Esta función trabaja con la mantisa, de igual manera,
# recibe la cadena de 32 bits y devuelve el valor numérico
# de la mantisa
def det_third_term(input_bits):
    third_term = 0
    mantissa = "1" + input_bits[9:]
    for num in range(len(mantissa)):
        third_term += int(mantissa[num]) / (2 ** num)
    return third_term


# Función que controla el flujo de los datos para entregar
# el resultado final. Al final suman las
# distintas partes que conforman el número en formato de
# punto flotante para determinar su valor decimal
def to_decimal():
    input_num = get_input()
    dec_first_term = det_first_term(input_num)
    dec_second_term = det_second_term(input_num)
    dec_third_term = det_third_term(input_num)
    dec_number = dec_first_term * dec_second_term * dec_third_term
    return dec_number
