N = int(input("Digite um número inteiro positivo: "))

contador = 0

for soma in range(1, N + 1):
    contador += soma


print(f"A soma dos números de 1 até {N} é {contador}.")