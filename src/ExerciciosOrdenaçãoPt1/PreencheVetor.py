import random

def preenche_vetor(vetor):
    for i in range(len(vetor)):
        vetor[i] = random.randint(1, 100)