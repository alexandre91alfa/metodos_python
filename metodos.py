def ordenar(arr):
    '''Retorna uma lista ordenada'''
    ordenado = [];
    for item in arr:
        if len(ordenado) == 0 or item > ordenado[-1]:
            ordenado.append(item);
        else:
            pos = 0;
            while pos < len(arr):
                if item <= ordenado[pos]:
                    ordenado.insert(pos,item)
                    break;
                pos += 1;
    return ordenado