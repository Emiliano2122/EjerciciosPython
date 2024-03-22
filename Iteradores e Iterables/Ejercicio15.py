lis = [[1, 2, 3, 4], 1, 'verde', [True, False, False], ['uno', 'dos', 'tres']]

def contar_elementos(lista):
    total_elementos = 0
    for elemento in lista:
        if type(elemento) == list:
            total_elementos += contar_elementos(elemento)
        else:
            total_elementos += 1
    return total_elementos

cantidad_total_elementos = contar_elementos(lis)
print(type(cantidad_total_elementos))

print("La cantidad total de elementos en la lista es:", cantidad_total_elementos)