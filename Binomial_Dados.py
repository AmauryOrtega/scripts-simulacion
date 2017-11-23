import random
n_corridas = 50
n_lanzamientos = 51
P = 1.0/6.0
respuesta = 0.0 # Cuantas veces se obtuvieron 20 veces el numero 3 luego de n_lanzamientos 
for corrida in range(n_corridas):
	# INICIO Corrida
	numero_3es = 0
	for lanzamiento in range(n_lanzamientos):
		R = random.random.uniform(0, 1)
		if R < P:
			numero_3es += 1.0
	print("51 Lanzamientos con", numero_3es, "3es")
	# FIN Corrida
	# Conteo para probabilidad
	if numero_3es == 20: respuesta += 1.0
print("P(X=20):", respuesta/n_corridas)