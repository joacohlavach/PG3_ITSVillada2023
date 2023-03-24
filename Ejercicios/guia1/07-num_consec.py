def es_step(numero):
    numero_str = str(numero)
    # convertimos el número a una cadena de caracteres

    for i in range(len(numero_str) - 1):
        # recorremos cada dígito
        diferencia = abs(int(numero_str[i]) - int(numero_str[i+1]))
        # calculamos la diferencia entre el dígito actual y el siguiente
        
        if diferencia != 1:
            return False
            
    return True

num = input("Ingrese un numero para saber si es step o no: ")
if es_step(num) == True:
    print("Es step")
else:
    print("No es step")
