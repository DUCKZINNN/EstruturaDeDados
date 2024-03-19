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

def calcular_media(vetor):
    if len(vetor) == 0:
        return 0
    soma = sum(vetor)
    media = soma / len(vetor)
    return media

vetor = [0] * 1000
preenche_vetor(vetor)
insertion_sort(vetor)

media = calcular_media(vetor)
print("A média do vetor é:", media)

#Usado o código do arquivo ExInsertionSort.py
