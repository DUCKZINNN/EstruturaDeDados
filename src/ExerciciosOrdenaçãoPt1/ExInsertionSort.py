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

vetor = [0] * 1000
preenche_vetor(vetor)
insertion_sort(vetor)

print(vetor)