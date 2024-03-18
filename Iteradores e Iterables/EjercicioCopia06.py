lista_incompleta = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]
lista_faltante =[numero_faltante for numero_faltante in range(1,20) if numero_faltante not in lista_incompleta]
lista_completa = lista_incompleta + lista_faltante
lista_completa.sort()
print(lista_completa)