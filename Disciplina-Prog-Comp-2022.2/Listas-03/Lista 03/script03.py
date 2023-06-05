'''
Faça um programa que solicite ao usuário um valor inteiro positivo e exiba os números
primos de 1 até o valor informado.
'''
#recebe numeros inteiros positivos
recebe_int_pos = int(input("INFORME UM INTEIRO POSITIVO: "))
#verificar se é um inteiro positivo

if(recebe_int_pos > 0):
    contador = 0
    while contador < recebe_int_pos:
        contador += 1
        #exibir os numeros de 1 ao numero informado
        if (recebe_int_pos % contador) == 1: # fazer os restos de 0 até o numero informado 
            print(contador, end=' - ')
    