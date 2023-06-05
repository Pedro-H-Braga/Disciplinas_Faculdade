'''
Dados dois números inteiros positivos, determinar o máximo 
divisor comum entre eles usando o algoritmo de Euclides

1 var auxiliar, 2 entradas, se entradas < 0 exiba(error), se a < b exiba(error):

pegar resto de a por b > dividir b pelo resto até ser igual a 0

<<<professor eu juro que eu tentei, passei mais de 5 horas nessa questão>>>>
'''

a = int(input('Informe o primeiro numero: '))
b = int(input('Informe o segundo numero: '))
auxiliar = 0

if a and b > 0:
    for auxiliar in range(True):
    #while b != 0:  
    
        if b == 0:
            print(f'O MDC pelo algoritmo de euclides é: {a}')
            break
        else: 
            print(f'O MDC pelo algoritmo de euclides é: {a}')

        auxiliar = b
        print(auxiliar)
        b = a % b
        print(b)
        a = auxiliar
        print(a)
else:  
    print('INFORME VALORES VALIDOS')