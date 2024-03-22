lis = [[1, 2, 3, 4], 'rojo', 'verde', [True, False, False], ['uno', 'dos', 'tres']]
total_elementos = 0
elemento = len([elemento for elemento in lis if type(elemento) == list])
print(elemento)