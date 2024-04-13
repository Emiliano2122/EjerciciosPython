def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp
tmp = input("Escribe otro numero en este factorial")
print(factorial(5))
print(factorial(34))