'''
Faça um programa que receba uma palavras e imprima essa palavra na vertical (em escada).
Exemplo: Ao ser informada a palavra NATAL, o programa imprime conforme poder ser visto abaixo:
N
NA
NAT
NATA
NATAL

fazer laço que exibe posição por posição até chegar na posição final
'''
entrada = input('informe uma palavra: ')
contador = 0
guarda_palavra_anterior = ''
tamanho_entrada = len(entrada) 
entrada = entrada[::-1]

contador = tamanho_entrada
while contador >= 0:
    percorre_entrada = entrada[contador:tamanho_entrada]
    print(percorre_entrada[::-1])
    contador -= 1