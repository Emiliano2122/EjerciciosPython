mi_tupla = (1, 2, 3, 4, 1, 1, 5, 6, 1)
mi_lista = [1, 2, 3, 4, 1, 1, 5, 6, 1]

print(mi_tupla, mi_lista)
print("Que numero quieres checar")
elemento_tupla = int(input())
elemento_lista = int(input())

cantidad_en_tupla = mi_tupla.count(elemento_tupla)

print(f"El elemento {elemento_tupla} aparece {cantidad_en_tupla} veces en la tupla.")

cantidad_en_lista = mi_lista.count(elemento_lista)

print(f"El elemento {elemento_lista} aparece {cantidad_en_lista} veces en la lista.")