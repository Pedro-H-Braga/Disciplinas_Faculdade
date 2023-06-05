'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99
(inclusive), gerados aleatoriamente. Determinar (usar laço de repetição – NÃO USAR a biblioteca
statistics.py):

d) O desvio-padrão populacional dos valores dos elementos da lista

'''
from random import choice
from statistics import stdev

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,100)
numero_randomicos  = []
desvio_padrao      = 0

# condição para ser positivo e estar entre 0 a 9
if dimensao > 0:
    # laço que popula a lista com valores aleatorios floats
    for i in range(dimensao):
        numero_randomicos.append(choice(valores_randomicos))
 
    desvio_padrao = stdev(numero_randomicos)

    print(f'LISTA ORIGINAL: <{numero_randomicos}>')
    print(f'O desvio_padrao dos valores sao: <{desvio_padrao}>')
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')