'''
ASSUNTO DE STRINGS:

resolução:
- fazer a string ocorrer um 'split' que separe as palavras e seja possível contar as vogais
- fazer laço que identifique as vogais nas strings 
- fazer um contador para contar as aparições no laço

ANDAR PELA STRING:
var = '0123456789'
x = var[0:3:2] 0 a 3 pulando de dois em dois
RESPOSTA: X=012

Fazer um laço que ande do inicio ao fim da

LÓGICA 2 COM WHILE:
- pegar o tamanho da palavra com len() e 
- fazer while que seja verdadeiro até contador_string (que vai percorrer a string até ser menor que o tamanho da palavra)
- condição para percorrer a string 0 -> tamanho final, e ao percorrer, se achar uma vogal contador_vogais recebe +1 
'''

contador_vogais = 0                             # contador vogal 
vogais = 'aáãâeéêiíîoóõôuúû'                    # vogais que irão ser encontradas na string
vogais = vogais[::-1]
tamanho_vogais = len(vogais)                    # pega o tamanho da string
contador_vogais = tamanho_vogais
tamanho_percorre_vogais = 0
quantidade_vogais = 0

entrada = input('digite algo: ')    # tem 14 vogais
entrada = entrada.lower() # transformar as entradas em minusculo para não ter divergencia na contagem
entrada = entrada[::-1]
tamanho_string = len(entrada) # pega o tamanho da string           
contador_string = tamanho_string # contador inverso
tamanho_percorre_string = 0
               
for tamanho_percorre_string in range(tamanho_percorre_string, tamanho_string):
    ''' Posso fazer um laço que para cada posicao de percorre 
    string, verifique toda a string vogais vendo se alguma 
    vogal tem naquela posição da string'''
    # STRING
    contador_string -= 1
    percorre_string = entrada[contador_string::tamanho_string]
    tamanho_percorre_string = len(percorre_string)
    
    # VOGAIS
    for contador_vogais in range(tamanho_vogais):
        contador_vogais -= 1
        percorre_vogais = vogais[contador_vogais::tamanho_vogais]
        if percorre_vogais in percorre_string:
         quantidade_vogais += 1
'''Para cada percorre_string varra toda string vogais comparando com percorre_string'''
'''Verificando, if letra de percorre_string igual a letra de percorre vogais, quantidade_vogais += 1'''
    	 

print(f"Tem {quantidade_vogais} vogais na palavra: {entrada}")


