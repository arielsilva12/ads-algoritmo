#Ler duas frações (numerador e denominador), calcular e escrever a soma dessas frações, escrevendo o resultado em forma de fração

#Entrada
numerador1 = int(input('Insira o valor do numerador da primeira fração: '))
denominador1 = int(input('Insira o valor do denominador da primeira fração: '))
numerador2 = int(input('Insira o valor do numerador da segunda fração: '))
denominador2 = int(input('Insira o valor do denominador da segunda fração: '))

#Processamento
numerador_final = (numerador1 * denominador2) + (numerador2 * denominador1)
denominador_final = denominador1 * denominador2

#Saída
print(f'O resultado da soma da fração {numerador1}/{denominador1} e {numerador2}/{denominador2} é igual a {numerador_final}/{denominador_final}')

