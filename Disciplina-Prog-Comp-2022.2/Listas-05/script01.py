'''
Fazer um programa que solicite ao usuário um valor inteiro positivo e gere o seu valor em binário
--ATENÇÃO--: Deverá ser utilizada divisões inteiras para a solução

O QUE TENHO QUE FAZER? 
- minha saída tem que ser o binário daquele número 
- fatorar o numero e pegar a quantidade de vezes que ele será dividido para pegar o resto
- a fatoração em binario ocorre no range de números até 2
- pegar o resto do numero...
'''
entrada         = int(input("informe um valor: "))
contador        = 0
binario         = 0
entrada_inicial = entrada
str_binario     = ''

for contador in range(contador, entrada_inicial):
    if entrada >= 2:
        binario = entrada % 2
        entrada = entrada // 2
        contador = entrada
        str_binario = str(binario) + str_binario
    else:
        break
str_binario = str(1) + str_binario
print(str_binario)