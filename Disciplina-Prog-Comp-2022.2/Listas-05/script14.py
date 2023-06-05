'''
Dados n e dois números inteiros positivos i e j diferentes de 0, imprimir em ordem crescente os n
primeiros naturais que são múltiplos de i ou de j e ou de ambos.
Exemplo: Para n = 6 , i = 2 e j = 3 a saída deverá ser : 0,2,3,4,6,8.
'''

n = int(input('informe um valor para n: '))
i = int(input('informe um valor para i: '))
j = int(input('informe um valor para j: '))

multiplicador, contador, resto_i, resto_j = 0,0,0,0

if i and j != 0:

    for contador in range(contador, n):

        multiplicador = i * contador
        resto_i = multiplicador % i
        if resto_i == 0:
            multiplicador_i = multiplicador

        multiplicador = 0
        multiplicador = j * contador
        resto_j = multiplicador % j    
        if resto_j == 0:
            multiplicador_j = multiplicador
        
        if multiplicador_i == multiplicador_j:
            print(multiplicador_i)
            contador += 1
        else:
            contador += 1
            print(f"{multiplicador_i} | {multiplicador_j}")
else:
    print('<<Informe valores positivos diferentes de 0>>')
