# Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o numero de anos que ele fuma, o número de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros)

#Entrada
anos_que_fuma = int(input('Insira o período (em anos) que o fumante fuma: '))
cigarros_por_dia = int(input('Insira quantos cigarros o fumante fumava por dia: '))
preco_carteira = float(input('Insira o valor da carteira que o fumante costuma comprar: '))

#Processamento
unidade_cigarro = preco_carteira / 20
gasto_por_dia = unidade_cigarro * cigarros_por_dia
total_gasto = anos_que_fuma * 365 * gasto_por_dia

#Saída
print(f'O total gasto em cigarro durante esses {anos_que_fuma} anos que fuma foram {total_gasto:.2f}')