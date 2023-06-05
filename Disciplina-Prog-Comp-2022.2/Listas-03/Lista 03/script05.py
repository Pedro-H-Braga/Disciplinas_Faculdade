'''
Faça um programa que solicite valores inteiros ao usuário e a medida que o usuário o 
informe o valor, o programa deverá informar se o valor digitado é par ou ímpar. 
O programa encerra quando o usuário informar o valor 0 (ZERO)
'''
# laço para enquanto a verdadeiro faça
a        = True
while a == True:
    entrada = int(input("Informe um NUMERO que seja INTEIRO e POSITIVO ou 0 se quiser sair do programa: "))
    #se for positivo
    if entrada > 0:
        #se par, else impar
        if (entrada % 2) == 0:   
            print(f"Esse numero e PAR: {entrada}")    
        else: print(f"Esse numero e IMPAR: {entrada}")
    #se igual a 0 saia do programa
    elif entrada == 0:
        print("Saindo do programa")
        a = False
    #senao repita o valor novamente
    else: print(f"{entrada} NAO RECONHECIDO, repita o valor novamente.")
    # receber numero int positivo
    
