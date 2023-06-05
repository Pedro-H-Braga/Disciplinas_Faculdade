'''
Faça um programa que solicite ao usuário uma frase, uma palavra antiga e uma palavra nova. O
programa deverá imprimir a frase digitada, as duas palavras digitadas (a antiga e a nova) e a frase
substituindo a palavra antiga pela palavra nova.
'''
#duas entrada 
entrada_frase = input("informe uma frase: ")
print(entrada_frase)
entrada_antiga = input("trocar: ")
entrada_nova = input("por: ")
# achar a palavra_antiga na frase e dar um replace, exibir a palavra antiga e a nova 
frase_antiga = entrada_frase
entrada_frase = entrada_frase.replace(entrada_antiga, entrada_nova)

print(f"A entrada antiga era:'{frase_antiga}', a nova é:'{entrada_frase}'")