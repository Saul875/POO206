while True:
    try:

        num = int(input("Introduce un número entero positivo: "))
        if num < 0:
            print("No se aceptan números negativos")
            continue

        x = [str(i) for i in range(num, -1, -1)]
        print(", ".join(x))
        break

    except ValueError:
        print("Error: Debes introducir un número entero válido")
