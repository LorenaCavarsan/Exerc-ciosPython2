N = int(input("Digite um número inteiro positivo: "))

soma = 0
contador = 1

while contador <= N:
    soma += contador
    contador += 1

print(f"A soma dos números de 1 até {N} é {soma}.")