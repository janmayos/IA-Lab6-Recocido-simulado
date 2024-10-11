from valoresminimos import run_minimos


def menu():
    print("*** MENU ***")
    print("1.-Valores mínimos de la función")
    print("2.-Salir")
    while True:
        opcion = int(input("Ingresa la opción deseada entre 1-2:"))
        if opcion >= 1 and opcion <= 2:
            break
        else:
            print("Valor incorrecto")
    return opcion


if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == 1:
            run_minimos()
        else:
            print("Gracias por jugar")
            exit(0)
