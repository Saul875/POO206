while True:
    try:
        f = input("Introduce una frase: ")
        if f.strip() == "":
            raise ValueError("Porfavor introduce algo")

        l = input("Introduce una letra: ")
        if len(l) != 1 or not l.isalpha():
            raise ValueError("Introducec una letra válida")

        cont = f.lower().count(l.lower())
        print(f"La letra '{l}' aparece {cont} vez/veces en la frase")

    except ValueError as e:
        print("Error:", e)
