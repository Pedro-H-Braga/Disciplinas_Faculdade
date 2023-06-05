''' 
Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não)
triangular, de acordo com a definição.

(n * (n+1)) /2
'''
entrada = 1

# ver se é um numero triangular n vezes
while entrada > 0:
    
    entrada = int(input("Digite o valor de n: "))
    
    nTriangular = (entrada*(entrada+1))/2
    meiaEntrada = entrada / 2
    if nTriangular == meiaEntrada:
       print(f"{entrada} EH um numero triangular")
    else:
        print(f"{entrada} NAO um numero triangular")
    