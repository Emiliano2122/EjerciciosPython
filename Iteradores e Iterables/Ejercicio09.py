d = [0,1]

d += [(d := [d[1], d[0] + d[1]]) and d[1] for k in range(1, 6)]
print(d)

cocientes = []
for i in range(1, 6):
    cociente = d[-i - 1] / d[-i]
    cocientes.append(cociente)

print("Cocientes de los ultimos 5 pares de numeros contiguos en la secuencia de Fibonacci:")
for i, cociente in enumerate(cocientes, start=1):
    print(f"n{i-1} / n{i}: {cociente}")