n_terminos = 30

n_0 = 0
n_1 = 1

fibonacci = [n_0, n_1]

for _ in range(2, n_terminos):
    siguiente = n_0 + n_1
    fibonacci.append(siguiente)
    n_0, n_1 = n_1, siguiente

print("Secuencia de Fibonacci:")
print(fibonacci)