def verificar(conjunto, candidato, k):
    ordenado = sorted(conjunto)
    return ordenado.index(candidato) == k


def fuerza_bruta(conjunto, k):
    for candidato in conjunto:
        if verificar(conjunto, candidato, k):
            return candidato
    return None            
