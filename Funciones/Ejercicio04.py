def convertir_temperatura(valor, medida_origen, medida_destino):
    if medida_origen == "Celsius":
        if medida_destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif medida_destino == "Kelvin":
            return valor + 273.15
        else:
            return valor  # Si la medida de origen y destino son iguales, devolver el mismo valor
    elif medida_origen == "Fahrenheit":
        if medida_destino == "Celsius":
            return (valor - 32) * 5/9
        elif medida_destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
        else:
            return valor
    elif medida_origen == "Kelvin":
        if medida_destino == "Celsius":
            return valor - 273.15
        elif medida_destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32
        else:
            return valor
    else:
        return valor  # Si la medida de origen no es válida, devolver el mismo valor

# Ejemplo de uso:
valor = 25
medida_origen = "Celsius"
medida_destino = "Fahrenheit"

resultado = convertir_temperatura(valor, medida_origen, medida_destino)
print(f"{valor} grados {medida_origen} son {resultado} grados {medida_destino}")