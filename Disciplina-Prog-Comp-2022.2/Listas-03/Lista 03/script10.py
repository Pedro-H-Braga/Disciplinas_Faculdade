'''
> Faça um programa que receba uma quantidade indeterminada de valores numéricos, considere que para
encerrar a entrada de dados deve ser digitado o valor 0 (ZERO) e que ao finalizar a entrada dos valores
(desconsiderando o valor 0)
> exiba na tela o maior, o menor e a média dos valores digitados. 
> O programa deverá desconsiderar os valores negativos informados.
'''

# para media
soma = quantidade = media = 0
# para maior numero
maior = menor = 0
# Media dos valores digitados
while True:
    entrada = int(input("Digite um número inteiro: "))
    # desconsiderando os valores negativos e '0' informado
    if entrada > 0:
    # media
        soma += entrada
        quantidade += 1
        media = soma / quantidade
        # maior e menor
        if quantidade == 1:
            maior = menor = entrada
        else:
            if entrada > maior:
                maior = entrada
            if entrada < menor:
                menor = entrada

        # para sair do laço
    elif entrada == 0:
            print("SAINDO DO PROGRAMA\n")
            break

# media
print(f"Quantidade de números digitados: {quantidade}",end='\n')
print(f"Soma: {soma}", end='\n')
print(f"Média: {media:10.2f}", end='\n')
# maior menor
print(f"O maior foi {maior} e o menor foi {menor}", end='\n')