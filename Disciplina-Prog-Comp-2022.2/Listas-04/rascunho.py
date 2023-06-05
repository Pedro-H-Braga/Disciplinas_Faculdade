contador_vogais = 0                             # contador vogal 
vogais = 'aáãâeéêiíîoóõôuúû'                    # vogais que irão ser encontradas na string
percorre_vogais = ''
tamanho_vogais = len(vogais)                    # pega o tamanho da string

contador_string = 0                             # contador string
entrada = 'opa digai meu bom, quão á de ser'    # tem 14 vogais
percorre_string = ''
tamanho_string = len(entrada)                   # pega o tamanho da string           
               
entrada = entrada.lower()                       # transformar as entradas em minusculo para não ter divergencia na contagem

while contador_string < tamanho_string: 
    percorre_string = entrada[contador_string::tamanho_string]
    contador_string += 1
    percorre_vogais = vogais[contador_vogais::tamanho_vogais]
    contador_vogais += 1
    if percorre_vogais in percorre_string:
                contador_vogais += 1
    elif percorre_vogais not in percorre_string:
                contador_string += 1
print(f"Tem {contador_vogais} vogais na palavra: {entrada}")
