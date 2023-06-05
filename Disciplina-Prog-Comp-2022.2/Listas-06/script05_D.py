'''
Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser
solicitado ao usuário e ser positivo), com os elementos na faixa dos números inteiros entre 0 e 99
(inclusive), gerados aleatoriamente. Determinar (usar laço de repetição – NÃO USAR a biblioteca
statistics.py):

d) O desvio-padrão populacional dos valores dos elementos da lista

'''
from random import choice
print('<<Informar a baixo numeros inteiros e positivos>>')
dimensao = int(input('Informe a dimensao da lista: '))

valores_randomicos = range(1,100)
desvio_padrao      = 0
v_desvio           = 0
somatorio_media    = 0
somatorio_variancia= 0
posicao_mediana    = 0

numero_randomicos  = []
lista_ordenada     = []
lista_desvios      = []

# condição para ser positivo e estar entre 0 a 9
if dimensao > 0:
    # laço que popula a lista com valores aleatorios floats
    for i in range(dimensao):
        numero_randomicos.append(choice(valores_randomicos))
 
    for i in numero_randomicos:     
        ''' MEDIA '''
        # Somatorio dos numeros divido pela quantidade de elementos
        somatorio_media += i
    media = somatorio_media/dimensao
    
    for j in numero_randomicos:     
        ''' DESVIOS '''
        # cada elemento menos a media, gerará uma lista de numeros
        lista_desvios.append(j-media)
    for k in lista_desvios:     
        ''' VARIANCIA '''
        # o somatório de cada desvio elevado ao quadrado e dividido pela quantidade de elementos
        somatorio_variancia += (k ** 2)
    
    variancia = somatorio_variancia / dimensao    

    desvio_padrao = variancia ** (1/2)

    print(f'LISTA ORIGINAL: <{numero_randomicos}>')
    print(f'O desvio_padrao dos valores sao: <{desvio_padrao}>')
else: 
    print('<<VALOR INFORMADO É INVÁLIDO>>')