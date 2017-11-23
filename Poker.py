"""
td - todos diferentes
1p - 1 par
2p - 2 pares
tercia - 3 iguales
full - 1 trio y 1 par
poker - 4 iguales
quintilla - todos iguales
"""

IMPRIMIR = True
prob = {'td':0.30240, '1p':0.50400, '2p':0.10800, 'tercia':0.07200, 'full':0.00900, 'poker':0.00450, 'quintilla':0.00010}
numeros = ["0.00000", "0.18750", "0.12500", "0.81250", "0.25000", "0.43750", "0.37500", "0.06250", "0.50000", "0.68750", "0.62500", "0.31250", "0.75000", "0.93750", "0.87500", "0.56250"]

# Limpieza de numeros
numeros_limpios = []
for numero in numeros:
  numeros_limpios.append(numero[2:])

# Que tengo
if IMPRIMIR:
  print(numeros_limpios)

def quintilla(numero):
    digito1 = numero[0]
    for digito in numero:
      if digito != digito1:
        return False
    return True
def full(numero):
  # Conteo
  guia = dict.fromkeys(numero, 0)
  for digito in numero:
    guia[digito]+=1
  if(2 in guia.values() and 3 in guia.values()):
    return True
  return False
def poker(numero):
  if(tercia(numero)):
    # Conteo
    guia = dict.fromkeys(numero, 0)
    for digito in numero:
      guia[digito]+=1
    for conteo in guia.values():
      if conteo >= 4:
        return True
    return False
  else:
    return False
def tercia(numero):
  # Conteo
  guia = dict.fromkeys(numero, 0)
  for digito in numero:
    guia[digito]+=1
  # Impar
  for conteo in guia.values():
    if conteo >= 3:
      return True
  return False
def onep(numero):
  # Conteo
  guia = dict.fromkeys(numero, 0)
  for digito in numero:
    guia[digito]+=1
  # Par
  for conteo in guia.values():
    if conteo >= 2:
      return True
  return False
def twop(numero):
  # Conteo
  guia = dict.fromkeys(numero, 0)
  for digito in numero:
    guia[digito]+=1
  # Primer par
  # Solo si sabemos que habia uno
  if onep(numero):
    par = None
    for conteo in guia.items():
      if conteo[1] >= 2:
        par = conteo[0]
        break
    # Quitamos el que habia
    del guia[par]
    # Segundo par
    for conteo in guia.values():
      if conteo >= 2:
        return True
    return False
  else:
    return False
def td(numero):
  return not (len(numero) != len(set(numero)))
def tipo(numero):
  if quintilla(numero):
    return 'quintilla'
  elif poker(numero):
    return 'poker'
  elif full(numero):
    return 'full'
  elif tercia(numero):
    return 'tercia'
  elif twop(numero):
    return '2p'
  elif onep(numero):
    return '1p'
  else:
    return 'td'

fo = {'td':0, '1p':0, '2p':0, 'tercia':0, 'full':0, 'poker':0, 'quintilla':0}

fe = {'td':0, '1p':0, '2p':0, 'tercia':0, 'full':0, 'poker':0, 'quintilla':0}
for indice in fe.keys():
    fe[indice]=len(numeros_limpios)*prob[indice]

for numero in numeros_limpios:
  if IMPRIMIR:
    print("#", numero)
    print("quintilla:", quintilla(numero))
    print("poker:", poker(numero))
    print("full:", full(numero))
    print("tercia:", tercia(numero))
    print("2p:", twop(numero))
    print("1p:", onep(numero))
    print("td:", td(numero))
    print("-"*5)
  fo[tipo(numero)]+=1

if IMPRIMIR:
  print("#"*5, "Frecuencias", "#"*5)
  print(fe, "=", sum(fe.values()))
  print(fo, "=", sum(fo.values()))

sum = 0.0
for indice in fe.keys():
    sum+=((fo[indice]-fe[indice])**2)/fe[indice]
print("sum", sum)
if sum < 7.81:
  print("No se rechaza que los numeros siguen una distribucion uniforme")
else:
  print("Se rechaza que los numeros siguen una distribucion uniforme")