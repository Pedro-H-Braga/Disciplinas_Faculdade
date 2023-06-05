'''
Dado o código a seguir, implemente um programa que faça o mesmo utilizando APENAS um laço
WHILE:

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

'''

variavel                  = '1234567890'
tamanho_variavel          = (len(variavel))+1

contador                  = 0
contador_invertido        = tamanho_variavel

tamanho_inicial           = 0
tamanho_percorre_variavel = 0

'''2 laços, um crescente e outro decrecente, quando um termina começa o outro'''
for contador in range(contador,tamanho_variavel):
    # exiba a input do início até o tamanho do contador
    print(variavel[:contador])
    contador += 1 
    # contador_invertido já recebe menos 1 para não repetir o estado final da palavra
    contador_invertido -= 1

for tamanho_percorre_variavel in range(tamanho_percorre_variavel, tamanho_variavel):
    contador_invertido -= 1
    print(variavel[:contador_invertido])
    tamanho_percorre_variavel = len(variavel[:contador_invertido])