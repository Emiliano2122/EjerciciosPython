def encontrar_primos(limite):
    compuestos = [False] * (limite + 1)
    primos = []

    for num in range(2, limite + 1):
        if not compuestos[num]:
            primos.append(num)

            for i in range(num * num, limite + 1, num):
                compuestos[i] = True
            if num * num > limite:
                break
    
    return primos

print("Numeros primis entre 0 y 30")
print(encontrar_primos(500))