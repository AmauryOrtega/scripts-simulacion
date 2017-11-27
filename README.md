# Códigos en simulación

## Prueba poker

## Volados

Esta juego esta explicado de la siguiente forma:

![Volados](Volados_1.png)

Un ejemplo de la simulación es el siguiente:

![Volados_ejemplo](Volados_2.png)

En este caso una corrida acaba cuando el saldo llega a 50 o 0. Una corrida esta dada por lo siguiente:
```python
import random
# INICIO Corrida
saldo = 30
apuesta = 10
print("[#] Si  A  R  = Sf")
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
```
Esto puede dar como salida:
```shell
[#] Si A  R  = Sf
[1] 30 10 G  = 40
[2] 40 10 P  = 30
[3] 30 20 P  = 10
[4] 10 10 P  = 0
Perdió
```
o
```shell
[#] Si A  R  = Sf
[1] 30 10 P  = 20
[2] 20 20 G  = 40
[3] 40 10 G  = 50
Ganó
```
- `[#]` Numero del lanzamiento.
- `Si` Saldo inicial.
- `A` Valor de la apuesta.
- `R` Si ganó `G` o perdió `P`.
- `Sf` Saldo final.

Haciendo lo anterior `n_corridas` y llevando la cuenta de cuantas veces ganó y perdió.
```python
n_corridas = 150
gana = 0 # Cuantas veces ganó
pierde = 0 # Cuantas veces perdió
for corrida in range(n_corridas):
    print("\nJuego #" + str(corrida + 1))
    # INICIO Corrida
    saldo # Tendra un valor de 0 ó >=50
    # FIN Corrida
    if saldo == 0:
        print("Perdio")
        pierde += 1
    else:
        print("Gano")
        gana += 1
print("\n% de Ganar",str("%.2f" % round(gana*100/(gana+pierde), 2)) + "%")
print("% de Perder",str("%.2f" % round(pierde*100/(gana+pierde), 2)) + "%")
```
Se obtiene una salida como esta (`n_corridas = 10`):
```shell
Juego #1
[#] Si A  R  = Sf
[1] 30 10 P  = 20
[2] 20 20 P  = 0
Perdió

Juego #2
[#] Si A  R  = Sf
[1] 30 10 P  = 20
[2] 20 20 P  = 0
Perdió

Juego #3
[#] Si A  R  = Sf
[1] 30 10 G  = 40
[2] 40 10 G  = 50
Ganó

Juego #4
[#] Si A  R  = Sf
[1] 30 10 G  = 40
[2] 40 10 P  = 30
[3] 30 20 G  = 50
Ganó

Juego #5
[#] Si A  R  = Sf
[1] 30 10 P  = 20
[2] 20 20 G  = 40
[3] 40 10 G  = 50
Ganó

Juego #6
[#] Si A  R  = Sf
[1] 30 10 P  = 20
[2] 20 20 G  = 40
[3] 40 10 G  = 50
Ganó

Juego #7
[#] Si A  R  = Sf
[1] 30 10 P  = 20
[2] 20 20 G  = 40
[3] 40 10 G  = 50
Ganó

Juego #8
[#] Si A  R  = Sf
[1] 30 10 G  = 40
[2] 40 10 G  = 50
Ganó

Juego #9
[#] Si A  R  = Sf
[1] 30 10 G  = 40
[2] 40 10 G  = 50
Ganó

Juego #10
[#] Si A  R  = Sf
[1] 30 10 G  = 40
[2] 40 10 G  = 50
Ganó

% de Ganar 80.00%
% de Perder 20.00%
```

## Procedimientos especiales (Dist Normal)

El procedimiento especial para generar una variable aleatoria `x`, con distribución normal con una media y desviación estándar en particular, es expresado con la siguiente ecuación:

![Normal_1](Normal_1.png)

Sin embargo, la bibliografía nos dice que esta demostrado para `n = 12` así que la ecuación queda así:

![Normal_2](Normal_2.png)

[Explicacion del libro](Normal.png).

### Lluvia

![Lluvia](Normal_Lluvia.png)

Del enunciado sabemos que la `MEDIA = 18.7` y que `DESV_ESTANDAR = 5`. Para generar una variable aleatoria `x` usamos el siguiente método:
```python
import random
def var_aleatoria():
    MEDIA = 18.7
    DESV_ESTANDAR = 5.0
    sumatoria = 0.0
    for i in range(12):
        sumatoria += random.uniform(0, 1)
    return MEDIA + DESV_ESTANDAR*(sumatoria - 6.0)
```
En este caso, se ejecutaran `n_corridas` donde cada una estará dada por 30 variables aleatorias debido a que cada variable representa un día del mes. Un solo mes, lo mismo que una corrida, se ejecuta así:
```python
# resultado = Cuantas veces la temperatura estuvo > 21°C en 1 mes
resultado = 0
for dia in range(30):
    if(var_aleatoria() > 21.0):
        resultado += 1
```
De esta forma la probabilidad que la temperatura sea > de 21°C en ese mes es `resultado/30.0`. Esto ejecutado `n_corridas` seria:
```python
n_corridas = 5
resultado_final = 0 # Promedio de probabilidades que la temperatura > 21°C después de n_corridas
for corrida in range(n_corridas):
    # INICIO Corrida
    # resultado = Cuantas veces la temperatura estuvo > 21°C en 1 mes
    resultado # Tendrá un valor después de la corrida
    # FIN Corrida
    print("[" + str(corrida + 1) + "] Prob de T > 21°: "
        + str("%.2f" % round(resultado/30.0, 2)) + " en 30 días")
    resultado_final += resultado/30.0
    print("P(T>21°C): " + str("%.2f" % round(resultado_final/n_corridas, 2)))
```
Esto da como salida:
```shell
[1] Prob de T > 21°: 0.33 en 30 días
[2] Prob de T > 21°: 0.37 en 30 días
[3] Prob de T > 21°: 0.40 en 30 días
[4] Prob de T > 21°: 0.50 en 30 días
[5] Prob de T > 21°: 0.43 en 30 días
P(T>21°C): 0.41
```
Para ver el código completo, [click aqui](Normal_Lluvia.py).

## Procedimientos especiales (Dist binomial)

El procedimiento especial para generar una variable aleatoria con distribución binomial puede ser expresado en una serie de pasos:
- Generar `n` números pseudo-aleatorios llamados `R`.
- Contar cuantos de estos `R` son menores que una probabilidad `P`
- La cantidad contada en el paso anterior es la variable aleatoria

[Explicacion del libro](Binomial.png).

### Alternadores

![Alternadores](Binomial_Alternadores.png)

En este caso, se ejecutaran `n_corridas` donde cada una estará dada por `n = 10` alternadores debido a que se consultan 10. Mi probabilidad de que un alternador este defectuoso es de `P = 0.2`. Con esto, 1 corrida sera lo siguiente:
```python
import random
n_alternadores = 10
P = 0.2
n_defectuosos = 0
for alternador in range(n_alternadores):
    if random.uniform(0, 1) < P:
        n_defectuosos += 1
```
De esta forma `n_defectuosos` seria mi variable aleatoria. Haciendo el código anterior múltiples veces y sacando las probabilidades para las preguntas seria así:
```python
n_corridas = 50
"""
resultado_0 = Pregunta a. Cuantas veces no hubieron defectuosos
resultado_1 = Pregunta b. Cuantas veces solo uno salio defectuoso
resultado_2 = Pregunta c. Cuantas veces salieron al menos 2 defectuosos
resultado_3 = Pregunta d. Cuantas veces salieron mas de 3 defectuosos
resultado_4 = Pregunta e. Cuantas veces no mas de 3 salieron defectuosos
"""
resultado_0 = 0
resultado_1 = 0
resultado_2 = 0
resultado_3 = 0
resultado_4 = 0

for corrida in range(n_corridas):
    # CORRIDA Código anterior
    n_defectuosos # Tendrá un valor después de la corrida
    # Conteo para probabilidades
    if n_defectuosos == 0: resultado_0 += 1
    if n_defectuosos == 1: resultado_1 += 1
    if n_defectuosos >= 2: resultado_2 += 1
    if n_defectuosos > 3: resultado_3 += 1
    if n_defectuosos <= 3: resultado_4 += 1
print("P(X=0):", resultado_0/n_corridas)
print("P(X=1):", resultado_1/n_corridas)
print("P(X>=2):", resultado_2/n_corridas)
print("P(X>3):", resultado_3/n_corridas)
print("P(X<=3):", resultado_4/n_corridas)
```
Esto da como salida:
```shell
P(X=0): 0.18
P(X=1): 0.3
P(X>=2): 0.52
P(X>3): 0.2
P(X<=3): 0.8
```
Para ver el código completo, [click aqui](Binomial_Alternadores.py).

### Dados

__¿Cual es la probabilidad de obtener 20 veces el numero 3 al lanzar 51 veces un dado?__

En este caso `n = 51` debido a que una corrida corresponderá a 51 lanzamientos. La probabilidad de sacar 3 en un dado es `P = 1/6`. Una corrida esta expresada de la siguiente forma:
```python
import random
n_lanzamientos = 51
P = 1.0/6.0
numero_3es = 0
for lanzamiento in range(n_lanzamientos):
    R = random.uniform(0, 1)
    if R < P:
        numero_3es += 1.0
print("51 Lanzamientos con", numero_3es, "3es")
```
De esta forma `numero_3es` sera mi variable aleatoria. Haciendo el código anterior múltiples veces y sacando la probabilidad para responder la pregunta seria así:
```python
n_corridas = 50
respuesta = 0.0 # Cuantas veces se obtuvieron 20 veces el numero 3 luego de n_lanzamientos 
for corrida in range(n_corridas):
    # INICIO Corrida
    numero_3es # Tendrá un valor después de la corrida
    # FIN Corrida
    # Conteo para probabilidad
    if numero_3es == 20: respuesta += 1.0
print("P(X=20):", respuesta/n_corridas)
```
Esto da como salida:
```shell
51 Lanzamientos con 7.0 3es
51 Lanzamientos con 11.0 3es
51 Lanzamientos con 9.0 3es
51 Lanzamientos con 5.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 6.0 3es
51 Lanzamientos con 7.0 3es
51 Lanzamientos con 6.0 3es
51 Lanzamientos con 9.0 3es
51 Lanzamientos con 6.0 3es
51 Lanzamientos con 7.0 3es
51 Lanzamientos con 9.0 3es
51 Lanzamientos con 11.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 12.0 3es
51 Lanzamientos con 4.0 3es
51 Lanzamientos con 11.0 3es
51 Lanzamientos con 10.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 3.0 3es
51 Lanzamientos con 6.0 3es
51 Lanzamientos con 9.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 7.0 3es
51 Lanzamientos con 11.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 9.0 3es
51 Lanzamientos con 12.0 3es
51 Lanzamientos con 5.0 3es
51 Lanzamientos con 5.0 3es
51 Lanzamientos con 11.0 3es
51 Lanzamientos con 7.0 3es
51 Lanzamientos con 6.0 3es
51 Lanzamientos con 9.0 3es
51 Lanzamientos con 12.0 3es
51 Lanzamientos con 10.0 3es
51 Lanzamientos con 4.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 12.0 3es
51 Lanzamientos con 7.0 3es
51 Lanzamientos con 14.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 13.0 3es
51 Lanzamientos con 7.0 3es
51 Lanzamientos con 4.0 3es
51 Lanzamientos con 11.0 3es
51 Lanzamientos con 8.0 3es
51 Lanzamientos con 10.0 3es
51 Lanzamientos con 13.0 3es
P(X=20): 0.0
```
Para ver el cogido completo, [click aqui](Binomial_Dados.py).