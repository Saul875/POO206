while True:
    try:
        n = int(input("Introduce un número entero positivo mayor que 10: "))
        if n <= 10:
            raise ValueError("El número es menor o igual a 10, es necesario que el numero sea mnayor a 10")
        break
    except ValueError as e:
        print(f"Error: {e}. Intenta de nuevo.")

impares = []
for i in range(3, n+1, 2):
    impares.append(str(i))

resultado = ",".join(impares)
print("Números impares desde 2 hasta", n, ":")
print(resultado)
