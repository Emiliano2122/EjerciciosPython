ciudades = ["Alemania", "Tokio", "Londres", "Paris", "Roma", "Moscu", "España", "Sideny", "Berlin"]

diccionario_ciudades = {"Ciudad": ciudades}

diccionario_ciudades["Pais"] = ["Alemania", "Japon", "Inglaterra", "Francia", "Italia", "Rusia", "España", "Australia", "Alemania"]
diccionario_ciudades["Continentes"] = ["Europa", "Asia", "Europa", "Europa", "Oceania", "Europa"]

print("Dicctionario de ciudades:")
print(diccionario_ciudades)

print("Clave del diccinario:")
print(diccionario_ciudades.keys())

print("Ciudades")
print(diccionario_ciudades["Ciudad"])