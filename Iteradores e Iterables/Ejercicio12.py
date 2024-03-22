cadena = 'Hola Mundo. Esto es una practico del lenguaje de programacion Python'
contador = 0
lista_cadena = list(cadena)
lista_cadena = iter(lista_cadena)

#for caracter in lista_cadena:
while contador < len(cadena):
    print(next(lista_cadena))
    contador += 1
print(len(cadena))
#print(type(cadena))
#print(type(lista_cadena))