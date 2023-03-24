def buscar_num(lista, num):
    if num in lista:
        return lista.index(num)
    else:
        return -1
mi_lista = [10,20,30,40,50]
elemento_buscado = int(input("Ingrese el número que desee buscar: "))
posicion = buscar_num(mi_lista, elemento_buscado)
if posicion != -1:
    print(f"El número {elemento_buscado} se encuentra en la posición: {posicion}")
else:
    print(f"El número {elemento_buscado} no se encuentra en la lista")