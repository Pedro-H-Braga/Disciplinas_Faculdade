'''
Refaça a questão 3, dessa vez usando o método de ordenação de lista (SORT() ou SORTED()), sendo
que a ordenação agora deverá ser decrescente.

'''
from random import choice

print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,100)
repeticoes         = 0
numero_randomicos  = []
lista_ordenada     = []
# condição para ser positivo e estar entre 0 a 9
if dimensao > 0:
    # laço que popula a lista com valores aleatorios
    for i in range(dimensao):
        numero_randomicos.append(choice(valores_randomicos))
    print(f'LISTA ORIGINAL: <{numero_randomicos}>')
    # ordenando de forma crescente
    numero_randomicos.sort()
    # ordenando de forma decrescente
    numero_randomicos = numero_randomicos[::-1]
    print(f'LISTA DECRESCENTE: <{numero_randomicos}>')

else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')