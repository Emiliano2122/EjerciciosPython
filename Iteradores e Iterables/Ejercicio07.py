n_terminos = 30

n0 = 0
n1 = 1

fibonacci = [n0, n1]

for _ in range(2, n_terminos):
    siguiente = n0 + n1
    fibonacci.append(siguiente)
    n0, n1 = n1, siguiente

print("Secuencia de Fibonacci:")
print(fibonacci)