'''
Faça um programa que calcule a soma dos números positivos digitados pelo usuário. O programa deve
permitir que o usuário digite uma quantidade não determinada de números. O programa encerra e
imprime o valor da soma quando o usuário digitar o valor 0 (ZERO)
'''
operando = 0
positivos = 0
entrada = 1

while entrada != 0: 

    entrada = int(input("Informe um valor: "))
    
    if entrada % 2 == 0:
        positivos += entrada       
    
print("A soma e: ", positivos)
