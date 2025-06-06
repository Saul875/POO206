#Si es par se divide entre 2
#Si es impar se multiplica por 3 y se suma 1
while True:
    try:
        x: int = print(input("Introduzca un número "))
        if x%2 == 0:
            np: int = x / 2 
            print(np)

        else:
            if x % 2 != 0:
                ni: int = x * 3 + 1
                print(ni)

    except (ValueError) as e:
        print("Ocurrió el siguiente error:", e)

