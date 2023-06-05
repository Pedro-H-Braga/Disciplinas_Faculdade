'''
Dado um número natural na base binária, transformá-lo para a base decimal. Usar
OBRIGATORIAMENTE laço de repetição.
Exemplo: Dado 10010 a saída será 18, pois 1.24 + 0.23 + 0.22 + 1.21 + 0.20 = 18.


'''
# pegando o binario em formato string e invertendo-o para nao ter divergencia nas contagem das posicoes
binario = str(input('Informe um numero em binario: '))
binario = binario[::-1]

pos           = 0
multiplicador = 0
valor_decimal = 0
tamanho_bin = len(binario)

for pos in range(pos,tamanho_bin):
   # varrendo a string em cada posicao 
    percorre_str = binario[pos::tamanho_bin] 
    percorre_str = percorre_str[::-1]

    if '1' in percorre_str:
        multiplicador = 1
    else:        
        multiplicador = 0
    # formula de binario -> decimal
    valor_decimal +=  multiplicador * (2 ** pos)

    pos += 1

print(f'Valor decimal do binario {binario[::-1]} é:',valor_decimal)