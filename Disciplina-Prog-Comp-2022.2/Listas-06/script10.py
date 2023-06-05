'''
Faça um programa que leia dois valores: x e n (x e n deverão ser solicitados ao usuário), onde x é a
quantidade de elementos que a lista deverá armazenar positivo e n serão os valores inteiros a serem
inseridos na lista, o programa deve terminar a leitura dos números quando for informado o valor 0 (o
valor 0 não deverá fazer parte da lista). A lista só deverá armazenar os x menores números informados,
seguindo a lógica abaixo:
'''

x = int(input('informe a quantidade de elementos da lista: '))
lista_valores = []
if x > 0:
    for i in range(x):
        n = int(input('informe um valor: '))
        if n == 0:
            print('<<SAINDO DO PROGRAMA>>')
            break 
        else:
            lista_valores.append(n)
            lista_valores.sort()
            print(lista_valores)
else:
    print('<<SAINDO DO PROGRAMA>>')