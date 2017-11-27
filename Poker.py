import manos

# Nivel de verbose
entrada = input("Desea ver todos los detalles?(Y/N) >")
IMPRIMIR = (entrada == 'Y' or entrada == 'y')

# Leyendo numeros
numeros = []
ruta = "numeros-poker.txt"
# ruta = "numeros-poker-2.txt"
with open(ruta, "r") as archivo:
    for linea in archivo:
        numeros.append(linea[2:7])
    archivo.close()

# Mostrando numeros
if IMPRIMIR:
  print(numeros)

# Frecuencia observada
fo = {'td':0, '1p':0, '2p':0, 'tercia':0, 'full':0, 'poker':0, 'quintilla':0}
# Frecuencia esperada
fe = {'td':0, '1p':0, '2p':0, 'tercia':0, 'full':0, 'poker':0, 'quintilla':0}
# Calculando frecuencia esperada
for tipo_mano in fe.keys():
    fe[tipo_mano] = len(numeros) * manos.probabilidad[tipo_mano]

# Contando la frecuencia observada
for numero in numeros:
    fo[manos.tipo(numero)] += 1
    if IMPRIMIR:
        print("#", numero)
        print("quintilla:", manos.quintilla(numero))
        print("poker:", manos.poker(numero))
        print("full:", manos.full(numero))
        print("tercia:", manos.tercia(numero))
        print("2p:", manos.twop(numero))
        print("1p:", manos.onep(numero))
        print("td:", manos.td(numero))
        print("-"*5)

# Mostrar la frecuencia esperada y observada obtenida
if IMPRIMIR:
    print("#"*5, "Frecuencias", "#"*5)
    print(fe, "=", sum(fe.values()))
    print(fo, "=", sum(fo.values()))

# Calculando X^2
sum = 0.0
for tipo_mano in fe.keys():
    sum += ((fo[tipo_mano]-fe[tipo_mano])**2)/fe[tipo_mano]

# Resultado
print(sum, "< 7.81")
if sum < 7.81:
  print("No se rechaza que los numeros siguen una distribucion uniforme")
else:
  print("Se rechaza que los numeros siguen una distribucion uniforme")