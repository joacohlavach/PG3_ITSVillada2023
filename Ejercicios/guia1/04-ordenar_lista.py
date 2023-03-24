def ordenar(lista):
    return sorted(lista, reverse=True)

lista = []  

while True:
    valor = input("Ingrese un valor para agregar a la lista o 'stop' para terminar: ")
    if valor == 'stop':
        break  
    lista.append(int(valor))  
print(f"La lista ingresada es: {lista}")

lista_ordenada = ordenar(lista)
print(f"La lista ordenada es: {lista_ordenada}")