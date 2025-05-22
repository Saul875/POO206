try:
    #Pedimos al usuario que introduzca un número
    numero = int(input("Introduce un número: "))
    # Intentamos dividir 10 entre el número introducido
    resultado = 10 / numero
    # Mostramos el resultado si no hay error
    print("El resultado es:", resultado)

 #Capturamos dos tipos de errores en una línea: división por cero o valor no entero
except (ZeroDivisionError, ValueError) as e:
    # Imprimimos el mensaje de error capturado
    print("Ocurrió el siguiente el error:", e)