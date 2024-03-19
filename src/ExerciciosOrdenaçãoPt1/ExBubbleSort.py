import random

def preenche_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = random.randint(1, 100)

def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n):
        # Últimos i elementos já estão no lugar
        for j in range(0, n-i-1):
            # Percorre o vetor da esquerda para a direita
            if vetor[j] > vetor[j+1]:
                # Se o elemento atual for maior que o próximo, troca
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

# Criar vetor com 1000 posições
vetor = [0] * 1000

# Preencher vetor usando a função preenche_vetor
preenche_vetor(vetor)

# Ordenar vetor usando Bubble Sort
bubble_sort(vetor)

# Imprimir o vetor ordenado
print("Vetor ordenado:")
print(vetor)