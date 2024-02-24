def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print("Numeros primos entre 0 y 30:")
for num in range(30):
    if es_primo(num):
        print(num)