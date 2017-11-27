# manos.py
"""
td - todos diferentes
1p - 1 par
2p - 2 pares
tercia - 3 iguales
full - 1 trio y 1 par
poker - 4 iguales
quintilla - todos iguales
"""
probabilidad = {'td':0.30240, '1p':0.50400, '2p':0.10800, 'tercia':0.07200, 'full':0.00900, 'poker':0.00450, 'quintilla':0.00010}
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
    # Solo si sabemos que había uno
    if onep(numero):
        par = None
        for conteo in guia.items():
            if conteo[1] >= 2:
                par = conteo[0]
                break
        # Quitamos el que había
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