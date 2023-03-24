def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    # pasar todo a minusculas y sacarle los espacios
    return palabra == palabra[::-1]
    # comparamos la version invert de la palabra

palabra = input("Ingrese una palabra: ")
print(es_palindromo(palabra))