fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]

cocientes = []
for i in range(1, 6):
    cociente = fibonacci[-i - 1] / fibonacci[-i]
    cocientes.append(cociente)

print("Cocientes de los ultimos 5 pares de numeros contiguos en la secuencia de Fibonacci:")
for i, cociente in enumerate(cocientes, start=1):
    print(f"n{i-1} / n{i}: {cociente}")