numero = int(input("Digite um número inteiro para exibir a tabuada: "))

for tabuada in range(1, 11):
    resultado = numero * tabuada
    print(f"{numero} x {tabuada} = {resultado}")