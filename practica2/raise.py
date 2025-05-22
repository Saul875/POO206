def verificar_edad(edad):
    if edad < 18:
        raise Exception("No eres mayor de edad")
    print("Eres mayor de edad")

try:
    verificar_edad(16)
except Exception as e:
    print("Error:", e)
