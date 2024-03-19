import random

def preenche_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = random.randint(1, 100)

def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        key = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > key:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = key


def encontra_menor(vetor):
    if len(vetor) > 0:
        return vetor[0]
    else:
        return None

vetor = [0] * 1000
preenche_vetor(vetor)
insertion_sort(vetor)

menor = encontra_menor(vetor)
print("O menor número do vetor é:", menor)

#Usado o código do arquivo ExInsertionSort.py