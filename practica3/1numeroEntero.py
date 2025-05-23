while True:
    try:
        x = int(input("Escribe un número entero, sin decimales: "))
        if x % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
    except ValueError:
        print("El número que ingresaste no es válido")