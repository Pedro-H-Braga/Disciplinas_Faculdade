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

exibir a verredura da string 
do começo pro final até chegar no tamanho_variavel, quando chegar no final
exiba do final ao começo dela, quando chegar no começo, comece a exibir a string 
ou seja:
enquanto contador < tamanho_variavel and contador invertido > tamanho_inicial

'''

variavel           = '1234567890'
tamanho_variavel   = len(variavel)
contador           = 0
contador_invertido = tamanho_variavel
tamanho_inicial    = 0

while True:  
    if contador < tamanho_variavel: 
        print(variavel[:contador])
        contador += 1 
    elif contador_invertido >= tamanho_inicial:
        print(variavel[:contador_invertido])
        contador_invertido -= 1
    else: break

