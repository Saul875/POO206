while True:
    def Numeros(x):
        if x.isdigit():
            raise ValueError("Error: se introdujeron números")
        return x
    
    try:
        print("Pulsa ""F"" para salir")
        x = input("Introduce una frase para verificar si es un palíndromo: ").lower()
        Numeros(x)
        if x == "f":
            print("Programa finalizado")
            break

        else:
            if x == x[::-1] :
                print("La frase sí es un palíndromo")
            else:
                print("La frase ingresada no es un palíndromo")

    except (ValueError) as Error:
        print("Ocurrió un error :", Error)