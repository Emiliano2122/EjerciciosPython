ciudades = ["Alemania", "Tokio", "Londres", "Paris", "Roma", "Moscu", "España", "Sideny", "Berlin"]

diccionario_ciudades = {"Ciudad": ciudades}

diccionario_ciudades["Pais"] = "Varios"
diccionario_ciudades["Continentes"] = "Varios"

print("Dicctionario de ciudades:")
print(diccionario_ciudades)

print("Clave del diccinario:")
print(diccionario_ciudades.keys())

print("Ciudades")
print(diccionario_ciudades["Ciudad"])