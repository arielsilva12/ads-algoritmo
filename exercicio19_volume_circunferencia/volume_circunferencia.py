#Ler o valor do raio de uma esfera, calcular e escrever o valor do volume da esfera. O valor do raio será digitado pelo usuário. O volume da esfera é calculado pela fórmula: V = 4/3 * π * r³, onde r é o raio da esfera e π é a constante pi (aproximadamente 3.14159).

raio = float(input('Digite o valor do raio da esfera: '))
volume = (4/3) * 3.14 * (raio ** 3)
print('O volume da esfera é', volume)


