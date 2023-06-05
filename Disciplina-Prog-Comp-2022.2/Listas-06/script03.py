'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99
(inclusive), gerados aleatoriamente. Imprimir a lista original gerada, em seguida, ordená-la de forma
crescente (usar laço de repetição) e imprimi-la. LEMBRANDO: NÃO USAR SORT() NEM SORTED()


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
    for numero in numero_randomicos:
        for chave, valor in enumerate(lista_ordenada):
            if numero < valor:
                lista_ordenada.insert(chave, numero)
                break
        else:
            lista_ordenada.append(numero)

    print(f'LISTA ORIGINAL: <{numero_randomicos}>')
    print(f'LISTA ORDENADA: <{lista_ordenada}>')

else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')
