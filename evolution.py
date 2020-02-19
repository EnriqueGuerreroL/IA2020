# Generar cadena (población) inicial
def  initial_data(root, iterations):
    pass

# Función que modifica ligeramente la cadena inicial para
# facilitar el manejo de la misma en pasos posteriores
def prepare_string(initial_string):
    new_string = initial_string
    if initial_string[0] == "1":
        new_string = "0" + initial_string
    if initial_string[-1] == "1":
        new_string += "0"
    return new_string

# Verifica si el organismo en cuestión morirá o no
def is_dead(a_slice):
    if (a_slice == "000" or a_slice == "111"):
        new_slice_char = "0"
    else:
        new_slice_char = "1"
    return new_slice_char

# Función que opera para producir la derivación de la cadena de entrada,
# simula la evolución
def evol_process(new_string):
    resulting_string = "1"
    for element in range(0, len(new_string)-2):
        resulting_string += is_dead(new_string[element:element + 3])
    resulting_string += "1"
    return resulting_string



my_string = "1111111" # 7 unos
cool_string = prepare_string(my_string)
print("cool string: " + cool_string)
print(evol_process(cool_string))