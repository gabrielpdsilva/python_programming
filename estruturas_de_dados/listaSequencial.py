#busca em uma lista ordenada

def busca(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
        
    return None     #retorna None se não encontrou o elemento


#exemplo de uso:
list = [1, 64, 41, 5, "teste", 20]
indice = busca(list, 5)

if indice is not None:
    print("O índice é " + str(indice)) #3
else:
    print("Valor não foi encontrado.")
input()