from dec_to_fp import to_fp_format
from fp_to_dec import to_decimal


def print_menu():
    while True:
        print("""\nElige una opción:\n
        1 Expresar número decimal en formato de punto flotante\n
        2 Convertir número en formato de punto flotante a decimal\n
        3 Salir\n""")
        choice = int(input("-> "))
        if choice == 1:
            print("Representación de punto flotante: ", to_fp_format(), "\n")
        elif choice == 2:
            print("Número decimal: ", to_decimal(), "\n")
        elif choice == 3:
            print("\n")
            break
        else:
            print("Elige una opción definida.\n")

if __name__ == "__main__":
        print_menu()