lis = [[1, 2, 3, 4], 1, 'verde', [True, False, False], ['uno', 'dos', 'tres']]

nueva_lista = [elemento if isinstance(elemento, list) else [elemento] for elemento in lis]
print(nueva_lista)