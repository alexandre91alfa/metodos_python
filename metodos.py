def ordenar(arr):
    '''Retorna uma lista ordenada'''
    ordenado = []
    for item in arr:
        if len(ordenado) == 0 or item > ordenado[-1]:
            ordenado.append(item)
        else:
            pos = 0
            while pos < len(arr):
                if item <= ordenado[pos]:
                    ordenado.insert(pos, item)
                    break
                pos += 1
    return ordenado


# forma simplificada fatorial
def fat(num): return 1 if num == 0 else num * fat(num - 1)


def fatorial(num):
    ''' Fatorial de um numero'''
    if num == 0:
        return 1

    return num * fatorial(num - 1)


'''retorna quantida de cada palavra da lista'''
def contador(lista): return [len(x) for x in lista]
