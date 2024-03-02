ciudades = ["Alemania", "Tokio", "Londres", "Paris", "Roma", "Moscu", "España", "Sideny", "Berlin"]

if 'Paris' not in ciudades:
    ciudades.append('Paris')
    mensaje = "'Paris' no esta en la lista y se ha agragado."
else:
    mensaje = "'Paris' ya no esta en la lista."

print(mensaje)
