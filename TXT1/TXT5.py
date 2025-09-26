with open("nicolas.txt", "r") as f:
    texto = f.read()
    palabras = texto.split()
    print("Cantidad", len(palabras))
