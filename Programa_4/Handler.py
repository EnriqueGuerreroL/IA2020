:
import os
import DCodificar

def caratula():
    unam = "Universidad Nacional Autónoma de México"
    fi = "Facultad de ingeniería"
    ia = "Inteligencia artificial"
    pg = "Programa 4"
    alum = "Integrantes:"
    fumo = "Fuentes Mora Oscar Fernando"
    gagn = "Granados Gómez Nanci Noelia"
    gle = "Guerrero López Enrique"
    psvh = "Pólito Seba Víctor Hugo"
    sem = "Semestre 2020-2"
    prof = "Profesor: Eduardo Espinosa Ávila"
    print ( "\n",unam.center(100, " "), "\n",fi.center(100," "), "\n\n",ia.center(100, " "), "\n",pg.center(100, " ") )
    print ("\n",alum.center(100," "), "\n",fumo.center(100, " "), "\n", gagn.center(100, " "), "\n",gle.center(100, " "))
    print (psvh.center(102," "),"\n\n",sem.center(100, " "), "\n\n",prof.center(100, " "))
    input("\n\n\nPresione una tecla para continuar...")

def codificar():
    os.system("Clear")
    print("Codificar una cadena")
    cadena = input ("\n Introduce la cadena a codificar: ")
    coder = DCodificar.programa04(cadena)
    clave = input(" \nIntroduzca la clave: ")
    clav = DCodificar.programa04(clave)
    print("\n La cadena introducida es: ", cadena)
    print("\n La cadena codificada es: ", coder.encode(clave))
    input("\n Presione una tecla para continuar")


def decodificar():
    print("Decodificar")

def main():
    
    while True:
        try:
            os.system("clear")
            print (" 1. Codificar \n 2. Decodificar \n 3. Salir")
            opcion = int (input ("\n Elija una opción: "))
            if (opcion == 1):
                codificar()
                continue
            elif(opcion == 2):
                decodificar()
                continue
            elif(opcion == 3):
                print("¡Hasta pronto!")
                break
            else:
                input (" Opción inválida, inténtelo de nuevo.\n Presione una tecla para continuar... ")
                main()
            break
        except ValueError:
            input (" Caracter inválido.\n Presione una tecla para continuar... ")
            continue

caratula()
main()
