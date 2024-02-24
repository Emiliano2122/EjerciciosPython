contador_while = 0

while contador_while < 3:
    print(f"Inicio de la interacion {contador_while + 1} del ciclo while")

    for i in range(5):
        print(f"Interacion {i + 1} del ciclo for, dentro de la interacion  {contador_while + 1} del ciclo while.")

        contador_while += 1
        print(f"Fin de la interacion {contador_while} del ciclo while. \n")