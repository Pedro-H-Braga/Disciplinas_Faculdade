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
tamanho_entrada = len(entrada) 
# faz cortar do ultimo ao primeiro, enves do inverso
entrada = entrada[::-1]

contador_inverso = tamanho_entrada

tamanho_percorre_entrada = 0
# para o tamanho de percorre_entrada chegar até o tamanho da entrada, pare
for tamanho_percorre_entrada in range(tamanho_percorre_entrada,tamanho_entrada):
    # contador inverso recebe menos 1 até chegar em 0
    contador_inverso -= 1
    # percorre entrada recebe a string entrada nas posicoes contador_inverso e tamanho entrada (30,30);(29,30)...
    # ou seja exibe a string caracter por caracter  
    percorre_entrada = entrada[contador_inverso:tamanho_entrada]
    # pega o tamanho da string adicionada  como parametro comparativo
    tamanho_percorre_entrada = len(percorre_entrada)
    # exibe a string ao contrário do que foi armazenado(de forma certa)
    print(percorre_entrada[::-1])
    
