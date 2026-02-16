# Ler 3 números inteiros e positivos (A, B, C) e calcular a seguinte expressão: D = (R+S)/2, onde R = (A+B)²; S = (B+C)²

#Entrada
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

#Processamento
R = (a + b) ** 2
S = (b + c) ** 2
D = (R + S) / 2

#Saída
print(f'Com R = {R} e S = {S}, o valor da expressão é {D}')