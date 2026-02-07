# imc é calculado dividindo o peso pela altura ao quadrado

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura **2)
print(f'O seu IMC é: {imc}')
