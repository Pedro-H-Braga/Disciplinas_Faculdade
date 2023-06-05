'''
Faça um programa que receba duas palavras e informe se uma é anagrama da outra.
Lembrando que anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra.
Exemplo: IRACEMA é um anagrama de AMERICA; ROMA é um anagrama de AMOR;...
'''
#recebe entrada e transforma em minusculo
entrada1 = input('entrada 1: ')
entrada2 = input('entrada 2: ')
entrada1,entrada2 = entrada1.lower(),entrada2.lower()
#varre as entrada ao contrário
entrada_invertida1 = entrada1[::-1]
entrada_invertida2 = entrada2[::-1]
#verfica se são anagramas uma da outra
if entrada_invertida1 == entrada2:
    print(f"As palavras '{entrada1}' e '{entrada2}' são ANAGRAMAS")
elif entrada_invertida2 == entrada1:
    print(f"As palavras '{entrada1}' e '{entrada2}' são ANAGRAMAS")
else: print(f"'{entrada1}' não é palindromo de '{entrada1}'")
