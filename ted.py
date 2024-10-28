# Inicializando o vetor VET e preenchendo com os 10 números fornecidos pelo usuário
VET = []

print("Digite 10 números:")

# Lendo os 10 números
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    VET.append(numero)

# Dicionário para armazenar posições dos números
posicoes = {}

# Verificando números repetidos e suas posições
for i in range(len(VET)):
    num = VET[i]
    # Se o número já estiver no dicionário, adicionar a nova posição
    if num in posicoes:
        posicoes[num].append(i)
    else:
        posicoes[num] = [i]

# Exibindo números repetidos e suas posições
repetidos = False
for num, indices in posicoes.items():
    if len(indices) > 1:
        repetidos = True
        print(f"O número {num} está repetido nas posições: {indices}")

if not repetidos:
    print("Não há números repetidos no vetor.")
