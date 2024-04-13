def convertir_temperatura(valor, medida_origen, medida_destino):
    print(valor, medida_origen, medida_destino)
    if medida_origen == "Celsius":
        if medida_destino == "Farenheit":
            print((valor * 9 / 3) + 32)
            return
        elif medida_destino == "Kelvin":
            print(valor + 273.15)
            return
    elif medida_origen == "Farenheit":
        if medida_destino == "Celsius":
            print((valor -32) * 5 / 9)
            return
        elif medida_destino == "Kelvin":
            print((valor - 32) * 5 / 9 + 273.15)
            return
    elif medida_origen == "Kelvin":
        if medida_destino == "Celsius":
            print(valor - 273.15)
            return
        elif medida_destino == "Farenheit":
            print((valor - 273.15) * 9 / 5 + 32)
            return
seleccion_menu_principal = 0
menu = True

text_menu = """
            Que temperatura quieres ver
            De que tempereraturar quieres convertir
            1.- Convertir de Celsius a Farenheit
            2.- convertir de Celsius a Kelvin
            3.- Convertir de Kelvin a Celsius
            4.- Convertir de Kelvin a Farenheit
            5.- Convertir de Farenheit a Celsius
            6.- Convertir de Ferenheit a Kelvin
            """
while(menu):
    print(text_menu)
    try:
        seleccion_menu_principal = int(input("Tu opcion que escogiste va aqui:"))
        if(seleccion_menu_principal == 1):
            medida_origen = "Celsius"
            medida_destino = "Farenheit"
            valor = float(input("Escribe el valor que desas convertir: y el resultado es"))
            convertir_temperatura(valor, medida_origen, medida_destino)
        if(seleccion_menu_principal == 2):
            medida_origen = "Celsius"
            medida_destino = "Kelvin"
            valor = float(input("Escribe el valor que desas convertir: y el resultado es"))
            convertir_temperatura(valor, medida_origen, medida_destino)
        if(seleccion_menu_principal == 3):
            medida_origen = "Kelvin"
            medida_destino = "Celsius"
            valor = float(input("Escribe el valor que desas convertir: y el resultado es"))
            convertir_temperatura(valor, medida_origen, medida_destino)
        if(seleccion_menu_principal == 4):
            medida_origen = "Kelvin"
            medida_destino = "Farenheit"
            valor = float(input("Escribe el valor que desas convertir: y el resultado es"))
            convertir_temperatura(valor, medida_origen, medida_destino)
        if(seleccion_menu_principal == 5):
            medida_origen = "Farenheit"
            medida_destino = "Celsius"
            valor = float(input("Escribe el valor que desas convertir: y el resultado es"))
            convertir_temperatura(valor, medida_origen, medida_destino)
        if(seleccion_menu_principal == 6):
            medida_origen = "Farenheit"
            medida_destino = "Kelvin"
            valor = float(input("Escribe el valor que desas convertir: y el resultado es"))
            convertir_temperatura(valor, medida_origen, medida_destino)
        menu == False
    except ValueError:
        print("La opcion que escogiste no es correcta")