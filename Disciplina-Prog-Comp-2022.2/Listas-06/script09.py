'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 1.000
(inclusive). Em seguida o programa deverá solicitar ao usuário um valor x compreendido entre 0 e 1.000
e:
a) Informar se o valor existe ou não lista;
b) Se existir, informar qual a posição do elemento na lista.
'''
from random import choice

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))
if dimensao > 0:
    num_input = int(input('Informe um numero que queira ver a posicação na lista: '))
    contador = 0
    
    valores_randomicos = range(0,1001)
    lista = []
    repeticoes = 0
# condição para ser positivo e estar entre 0 a 9
    # laço que popula a lista com valores aleatorios
    for i in range(dimensao):
        lista.append(choice(valores_randomicos))
    # laço que verifica quantas vezes 0 a 9 apareceram na lista
    for j in lista:
        if j == num_input:             
            print(f'O numero: <{num_input}> está na posição: <{contador}>')
        else:
            contador += 1
    else: 
        print('<<VALOR INFORMADO NÃO FOI ENCONTRADO>>', end='\nCONFIRA A LISTA ABAIXO:\n')
    print(f'<{lista}>')
else:
    print('<<VALOR INFORMADO NÃO EXISTE>>')