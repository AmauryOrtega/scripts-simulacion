import random
gana = 0
pierde = 0

for i in range(150):
  saldo = 30
  apuesta = 10
  print("\n#" + str(i+1))
  n_lanzamientos = 1
  # Apuesta el doble cuando pierde
  while saldo > 0 and saldo != 50:
    print("[" + str(n_lanzamientos) + "]", saldo, apuesta, end="")
    if random.uniform(0, 1) < 0.5:
      # Gana
      print(" V ", end="")
      saldo += apuesta
      apuesta = 10
    else:
      # Pierde
      print(" F ", end="")
      saldo -= apuesta
      apuesta *= 2
      if apuesta >= saldo:
        apuesta = saldo
    n_lanzamientos+=1
    print(" = " + str(saldo))
  if saldo == 0:
    print("Perdio")
    pierde += 1
  else:
    print("Gano")
    gana += 1
print("\n% de Ganar",str(gana*100/(gana+pierde)) + "%")
print("% de perder",str(pierde*100/(gana+pierde)) + "%")
