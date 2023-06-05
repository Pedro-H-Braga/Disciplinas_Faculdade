'''
Faça um programa que receba um valor qualquer e informe se esse valor digitado é um palíndromo
(utilizar laço de repetição WHILE).
Lembrando que palíndromo é uma cadeia de caracteres que quando lida da esquerda para a direita é
igual a quando se lê da direita para esquerda.
Exemplos: ARARA, 15051, ...

pegar a string que verifica, quando a string(pos(1,2,3,4)) for igua a ela quando invertida (pos(-1,-2,-3,-4))

inverter string:
entrada = 'entrada'
entrada_invertida = x[::-1]
'''

entrada = str(input('informe uma palavra: '))
entrada = entrada.lower()
entrada_invertida = entrada[::-1]

if entrada == entrada_invertida:
    print(f"As palavras '{entrada}' e '{entrada_invertida}' são palíndromos")
else: print(f"'{entrada}' não é palindromo de '{entrada_invertida}'")