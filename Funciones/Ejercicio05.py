def convertir_temperatura(valor, medida_origen, medida_destino):
    if medida_origen == "Celsius":
        if medida_destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif medida_destino == "Kelvin":
            return valor + 273.15
    elif medida_origen == "Fahrenheit":
        if medida_destino == "Celsius":
            return (valor - 32) * 5/9
        elif medida_destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
    elif medida_origen == "Kelvin":
        if medida_destino == "Celsius":
            return valor - 273.15
        elif medida_destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32

# Lista de temperaturas
temperaturas = [25, 32, 0]

# Medidas de temperatura posibles
medidas = ["Celsius", "Fahrenheit", "Kelvin"]

# Iterar sobre cada temperatura y cada medida
for temperatura in temperaturas:
    for medida_origen in medidas:
        for medida_destino in medidas:
            if medida_origen != medida_destino:
                resultado = convertir_temperatura(temperatura, medida_origen, medida_destino)
                print(f"{temperatura} grados {medida_origen} son {resultado:.2f} grados {medida_destino}")