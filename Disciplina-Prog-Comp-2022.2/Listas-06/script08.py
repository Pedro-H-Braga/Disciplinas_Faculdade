'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), cada elemento da lista será uma lista de n elementos. com os
elementos na faixa dos números inteiros entre 0 e 9 (inclusive), gerados aleatoriamente. Imprimir a lista
e calcular e imprimir o determinante dessa “matriz” 

https://pt.stackoverflow.com/questions/367434/como-calculo-determinante-de-uma-matriz-quadrada-em-python

'''

from random import choices

import numpy

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,100)
numero_randomicos  = []
desvio_padrao      = 0

# condição para ser positivo e estar entre 0 a 9
if dimensao > 0:
    # laço que popula a lista com listas do tamanho de 'dimensao' com valores aleatorios 
    for i in range(dimensao):
        numero_randomicos.append(choices(valores_randomicos, k=dimensao))
    
    print(numero_randomicos, end='\n')
    determinante_matriz = numpy.linalg.det(numero_randomicos)
    print(determinante_matriz)
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')
