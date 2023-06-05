'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99
(inclusive), gerados aleatoriamente. Determinar (usar laço de repetição - NÃO USAR a biblioteca
statistics.py):

b) A mediana dos valores dos elementos da lista
ordenar a lista de forma crescente -> dividir a dimensao da lista em 2 -> pegar o numero na posicao da divisao

'''
from random import choice

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,100)
repeticoes         = 0
mediana            = 0
posicao_mediana    = 0
numero_randomicos  = []
lista_ordenada     = []

# condição para ser positivo e estar entre 0 a 9
if dimensao > 0:
    # laço que popula a lista com valores aleatorios
    for i in range(dimensao):
        numero_randomicos.append(choice(valores_randomicos))

    for numero in numero_randomicos:
        for chave, valor in enumerate(lista_ordenada):
            if numero < valor:
                lista_ordenada.insert(chave, numero)
                break
        else:
            lista_ordenada.append(numero)
    
    posicao_mediana = int(dimensao/2)
    mediana = lista_ordenada[posicao_mediana]
    print(f'LISTA ORIGINAL: <{lista_ordenada}>')
    print(f'A mediana dos valores sao: <{mediana}>')
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')