import numpy as n
# Simulación del tiempo de espera aproximado de la llegada del Va-y-Ven
#El autobús pasa cada 15 minutos
Tiempo_espera = 15 #tiempo de espera
Tiempo_ultimo = round(n.random.uniform(0,15),2) #Número aleatorio entre 0 y 15 minutos
print (f'El autobús se fue hace {Tiempo_ultimo} minutos')
print(f'Debes esperar {round(Tiempo_espera - Tiempo_ultimo,2)} minutos')

