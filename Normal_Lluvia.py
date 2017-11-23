import random

MEDIA = 18.7
DESV_ESTANDAR = 5

def var_aleatoria():
  resultado = 0.0
  for i in range(12):
    resultado += random.uniform(0, 1)
  resultado = resultado
  resultado -= 6
  return MEDIA+DESV_ESTANDAR*resultado

promedio = 0.0

for j in range(5):
  numeros_mes = []
  for i in range(30):
    numeros_mes.append(var_aleatoria())
    sum = 0
  for x in numeros_mes:
    if(x>21.0):
      sum+=1
  #print("Var aleatorias:", numeros_mes)
  promedio += sum*100/30
  print("[" + str(j) + "]Prob de T > 21°: " + str(sum*100/30) + "% en " + str(len(numeros_mes)) + " dias")
print("Promedio " + str(promedio/5) + "%")