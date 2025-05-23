while True:
    try:
        x=int(input("introduce un año: "))
        if (x % 4 == 0):
            print("el año es bisiesto")
        else:
            print("El año no es bisiesto")
    except ValueError:
        print("No introdujiste un valor válido")