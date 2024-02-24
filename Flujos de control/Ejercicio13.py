def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def buscar_primo():
    while True:
        numero = int(input("Ingresa un numero para sabaer si es primo o pon 0 para terminar:"))

        if numero == 0:
            print("salir del programa.")
            break
        if es_primo(numero):
            print("Es un numero primo")
        else:
            print("No es un numero primo")
buscar_primo()