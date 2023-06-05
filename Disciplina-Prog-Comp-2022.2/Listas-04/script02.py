'''
Faça um programa que solicite ao usuário uma frase e substitua todos os espaços por _ 
(underline/sublinhado). O programa deverá exibir a frase original e a frase após as substituições.

'''
entrada = input("informe algo: ")

string_nova = entrada.replace(' ', '_')
print('antiga entrada: ' + entrada+', nova entrada: '+string_nova)