import random

def preenche_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = random.randint(1, 100)

def selection_sort(vetor):
    for i in range(len(vetor)):
        min_index = i
        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[min_index]:
                min_index = j
        vetor[i], vetor[min_index] = vetor[min_index], vetor[i]

vetor = [1000 - i for i in range(1000)]  # Vetor reversamente ordenado de 1000 elementos
selection_sort(vetor)
print(vetor)