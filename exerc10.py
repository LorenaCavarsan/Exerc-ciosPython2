numero = int(input("Digite um número inteiro para exibir a tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")