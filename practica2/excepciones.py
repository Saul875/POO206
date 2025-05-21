#numero = int(input("Introduce un número"))
#resultado = 10/numero

#print("Resultado:", resultado)

try:
    numero = int(input("Introduce un número: "))
    resultado = 10/numero
    print("Resultado:")

except ValueError:
    print("Error: se ingresó un valor no numérico")
except ZeroDivisionError:
    print("Error: estás intentando dividir entre 0 y eso no es posible")
    