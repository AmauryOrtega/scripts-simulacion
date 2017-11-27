import random
n_corridas = 10
gana = 0 # Cuantas veces ganó
pierde = 0 # Cuantas veces perdió
for corrida in range(n_corridas):
    print("\nJuego #" + str(corrida + 1))
    # INICIO Corrida
    saldo = 30
    apuesta = 10
    print("[#] Si A  R  = Sf")
    n_lanzamiento = 1
    while saldo > 0 and saldo != 50:
        print("[" + str(n_lanzamiento) + "]", saldo, apuesta, end="")
        if random.uniform(0, 1) < 0.5:
            # Gana
            print(" G ", end="")
            saldo += apuesta
            apuesta = 10
        else:
            # Pierde
            print(" P ", end="")
            saldo -= apuesta
            apuesta *= 2 # Apuesta el doble cuando pierde
            if apuesta >= saldo: apuesta = saldo
        print(" = " + str(saldo))
        n_lanzamiento += 1
    # FIN Corrida
    if saldo == 0:
        print("Perdió")
        pierde += 1
    else:
        print("Ganó")
        gana += 1
print("\n% de Ganar",str("%.2f" % round(gana*100/(gana+pierde), 2)) + "%")
print("% de Perder",str("%.2f" % round(pierde*100/(gana+pierde), 2)) + "%")