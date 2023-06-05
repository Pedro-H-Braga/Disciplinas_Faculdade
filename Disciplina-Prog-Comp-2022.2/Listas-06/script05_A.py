'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99
(inclusive), gerados aleatoriamente. Determinar (usar laço de repetição – NÃO USAR a biblioteca
statistics.py):

a) A média dos valores dos elementos da lista
soma dos elementos / dimensao da lista

'''
from random import choice

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,100)
somatorio          = float(0)
media              = float(0)
repeticoes         = 0

numero_randomicos  = []
lista_ordenada     = []

# condição para ser positivo e estar entre 0 a 9
if dimensao > 0:
    # laço que popula a lista com valores aleatorios
    for i in range(dimensao):
        numero_randomicos.append(choice(valores_randomicos))

    for i in numero_randomicos:
        somatorio += i
    
    media = somatorio/dimensao
    
    print(f'LISTA ORIGINAL: <{numero_randomicos}>')
    print(f'A media dos valores sao: <{media}>')
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')