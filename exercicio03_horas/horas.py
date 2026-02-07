#Ler um valor em minutos, calcular e escrever o equivalente em horas e minutos.

#Entrada
total_minutos = int(input("Digite o valor total de minutos: "))

#Processamento
horas = total_minutos // 60
minutos = total_minutos % 60

#Saída
print(f'O equivalente é: {horas} horas e {minutos} minutos.')
