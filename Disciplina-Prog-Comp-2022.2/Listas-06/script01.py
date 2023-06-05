'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 9
(inclusive), gerados aleatoriamente. Determinar as quantidades para cada número que foi gerado.

# utilizar a RANDOM.PY
'''
from random import choice

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(0,10)
lista = []
repeticoes = 0
# condição para ser positivo e estar entre 0 a 9
if dimensao in range(0,10):
    # laço que popula a lista com valores aleatorios
    for i in range(dimensao):
        lista.append(choice(valores_randomicos))
    # laço que verifica quantas vezes 0 a 9 apareceram na lista
    for j in range(0,10):
        repeticoes = lista.count(j)
        if repeticoes == 0: 
            continue
        else:
            print(f'O numero: <{j}> apareceu <{repeticoes}> vezes')
    
    print(f'<{lista}>')
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')