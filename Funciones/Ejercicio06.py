def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp
seleccion_de_menu_principal = 0
menu = True

text_menu = """
            Progama para calcular un factorial
            1- Calcular el factorial
            9- Salir del calculo del factorial
            """
while(menu):
    print(text_menu)
    try:
        seleccion_de_menu_principal = int(input("Elije la opcion: "))
        if(seleccion_de_menu_principal == 1):
            tmp = int(input("Escribe otro numero en este factorial"))
            print(factorial(tmp))
        if(seleccion_de_menu_principal == 9):
            menu = False
    except ValueError:
        print("No es un numero")
