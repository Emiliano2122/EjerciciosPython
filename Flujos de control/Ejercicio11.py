import time

def encontrar_primos_original(limite):
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

def encontrar_primos_optimizado(limite):
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

inicio_original = time.time()
encontrar_primos_original(10000)
fin_original = time.time()
tiempo_original = fin_original - inicio_original

inicio_optimizado = time.time()
encontrar_primos_optimizado(10000)
fin_optimizado = time.time()
tiempo_optimizado = fin_optimizado - inicio_optimizado

print("Tiempo de ejecucion de la implementacion original: ", tiempo_original)
print("Tiempo de ejecucion de la implementacion optimizada: ", tiempo_optimizado)