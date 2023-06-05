''' 
Faça um programa que leia um número e imprima o seu fatorial.

𝑛! = 𝑛 ∗ (𝑛 − 1) ∗ (𝑛 − 2) ∗ … ∗ 1

𝐸𝑥𝑒𝑚𝑝𝑙𝑜:
6! = 6 ∗ 5 ∗ 4 ∗ 3 ∗ 2 ∗ 1
6! = 720

Lembrando ainda que:
0! = 1
'''

entrada = int(input("Informe um valor: "))
fatorial = 1
contador = 1

while contador <= entrada:

    if entrada == 0:
        fatorial = 1
        break
    else:      
        fatorial *= contador
        contador += 1

print(f"Fatorial de {entrada} e: {fatorial}")