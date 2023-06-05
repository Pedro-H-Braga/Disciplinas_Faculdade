'''readme.md
Faça um programa que leia a idade de 5 pessoas e o sexo de cada uma (assuma que só podem ser
informados a letra H para homes e a letra M para mulheres) e que calcule e mostre:
a. A idade média das 5 pessoas;
b. A idade média dos homens;
c. A idade média das mulheres.
'''
# leia a idade de 5 pessoas e o sexo de cada

contadorGeral = 0
contadorH     = 0
contadorM     = 0

idadeGeral    = 0
idadeH        = 0
idadeM        = 0

mediaGeral    = 0
mediaH        = 0
mediaM        = 0

while contadorGeral < 5:
    # para 5 entradas
    contadorGeral += 1
    # pegar idade
    idade = int(input("Informe sua idade: "))
    # pegar sexo
    sexo = input("Informe seu sexo: ")
    # media geral
    idadeGeral += idade
    # media para homens
    if sexo == 'M':
        contadorM += 1
        idadeM += idade

    # media para mulheres
    if sexo == 'H':
        contadorH += 1
        idadeH += idade

# media geral
mediaGeral = idadeGeral/contadorGeral
# media H
mediaH = idadeH/contadorH
# media M
mediaM = idadeM/contadorM
# exibindo tudo
print(f"A media geral foi: {mediaGeral}\nA media para homens foi: {mediaH}\nA media para mulheres foi: {mediaM}")
