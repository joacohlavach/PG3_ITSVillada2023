try:
    with open('archivo.txt', 'w') as archivo:
        strings = ['Hola', 'Pepe', 'cómo', 'te', 'sentis']
        for s in strings:
            archivo.write(s + '\n')
            
        archivo.write(555)
        
except TypeError:
    print('Error: No se puede escribir un entero en el archivo de texto.')