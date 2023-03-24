def contar_vocales(frase):
    frase = frase.lower()
    # minusuclas
    vocales = ['a', 'e', 'i', 'o', 'u']
    # lista_vocales

    contador = 0
    for caracter in frase:
        if caracter in vocales:
            contador += 1
    return contador

f = input("Ingrese una frase o palabra: ")
print(f"Hay {contar_vocales(f)} vocales en la frase o palabra")