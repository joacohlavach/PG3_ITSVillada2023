meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

try:
    num_mes = int(input('Ingrese el número de mes (1-12): '))
    
    if num_mes >= 1 and num_mes <= 12:
        nombre_mes = meses[num_mes - 1]
        print(f'El nombre del mes {num_mes} es {nombre_mes}.')
    else:
        raise IndexError
except ValueError:
    print('Error: Debe ingresar un número entero.')
except IndexError:
    print('Error: El número de mes ingresado está fuera de rango.')