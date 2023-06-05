'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99
(inclusive), gerados aleatoriamente.

b) A mediana dos valores dos elementos da lista
ordenar a lista de forma crescente -> dividir a dimensao da lista em 2 -> pegar o numero na posicao da divisao

'''
from random import choice
from statistics import median

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,100)
numero_randomicos  = []
mediana            = 0

# condição para ser positivo e estar entre 0 a 9
if dimensao > 0:
    # laço que popula a lista com valores aleatorios
    for i in range(dimensao):
        numero_randomicos.append(choice(valores_randomicos))

    mediana = median(numero_randomicos)
    print(f'LISTA ORIGINAL: <{numero_randomicos}>')
    print(f'A mediana dos valores sao: <{mediana}>')
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')