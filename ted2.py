import random

# Inicializando a matriz A com valores randômicos inteiros entre 1 e 100
A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

# a. Calculando a soma de todos os valores da matriz A
soma_total = sum(sum(linha) for linha in A)

# b. Criando a matriz B, onde cada elemento é o valor correspondente de A multiplicado por 3
B = [[elemento * 3 for elemento in linha] for linha in A]

# Exibindo a matriz A, a soma dos elementos e a matriz B
print("Matriz A:")
for linha in A:
    print(linha)

print("\nSoma de todos os valores da matriz A:", soma_total)

print("\nMatriz B (A * 3):")
for linha in B:
    print(linha)
