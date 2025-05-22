try:
    print("Inicio del bloque try")
    resultado = 10 / 0  # Esto provoca un error de división por cero
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
finally:
    print("Esto siempre se ejecuta, sin importar si hubo error o no.")
