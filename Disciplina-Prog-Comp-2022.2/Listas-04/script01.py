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
percorre_vogais = ''
tamanho_vogais = len(vogais)                    # pega o tamanho da string

contador_string = 0                             # contador string
entrada = input('digite algo: ')    # tem 14 vogais
percorre_string = ''
tamanho_string = len(entrada)                   # pega o tamanho da string           
               
entrada = entrada.lower()                       # transformar as entradas em minusculo para não ter divergencia na contagem

while contador_string < tamanho_string:         # percorre a string até o contador chegar ao tamanho máximo dela
    percorre_string = entrada[contador_string::tamanho_string]
    contador_string += 1
    percorre_vogais = vogais[contador_vogais::tamanho_vogais]
    contador_vogais += 1
    if percorre_vogais in percorre_string:
        contador_vogais += 1
    elif percorre_vogais not in percorre_string:
        contador_string += 1

print(f"Tem {contador_vogais} vogais na palavra: {entrada}")
