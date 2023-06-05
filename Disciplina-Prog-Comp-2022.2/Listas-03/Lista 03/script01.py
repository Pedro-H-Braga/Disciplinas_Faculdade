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
binario_inverso = 0
binario         = 0

while entrada > 0:   
    binario_inverso   = binario_inverso * 10 + entrada % 2
    entrada //= 2
while binario_inverso > 0:
    binario = binario * 10 + binario_inverso % 10
    binario_inverso //= 10
print(binario)
# vou precisar fazer um laço que calcule o resto desse numero até ele ser maior que 2
# vou precisar de um (operador auxiliar que guardará os restos das divisões de forma que vá os resto 
# diretamente) e um (operador que guardará a fatoração do numero até ele ser maior que 2)
