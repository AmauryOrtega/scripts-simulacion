import random
n_corridas = 5

def var_aleatoria():
    MEDIA = 18.7
    DESV_ESTANDAR = 5.0
    sumatoria = 0.0
    for i in range(12):
        sumatoria += random.uniform(0, 1)
    return MEDIA + DESV_ESTANDAR*(sumatoria - 6.0)

resultado_final = 0 # Promedio de probabilidades que la temperatura > 21°C despues de n_corridas
for corrida in range(n_corridas):
    # INICIO Corrida
    # resultado = Cuantas veces la temperatura estuvo > 21°C en 1 mes
    resultado = 0
    for dia in range(30):
        if(var_aleatoria() > 21.0):
            resultado += 1
    # FIN Corrida
    print("[" + str(corrida + 1) + "] Prob de T > 21°: "
        + str("%.2f" % round(resultado/30.0, 2)) + " en 30 dias")
    resultado_final += resultado/30.0
print("P(T>21°C): " + str("%.2f" % round(resultado_final/n_corridas, 2)))