'''
Faça um programa que emule o jogo da forca. O programa terá uma constante chamada
PALAVRA_CHAVE que armazenara a palavra a ser descoberta. O programa deverá solicitar ao usuário
as letras e à medida que as letras forem sendo digitadas o programa irá exibir se o usuário acertou ou
não. O jogo deverá considerar maiúsculas e minúsculas iguais. O jogador poderá errar 6 vezes antes de
ser enforcado

VARIAVEIS:
palavra_chave
tamanho_palavra
acertos
erros
falta_quanto

LÓGICA:
fazer laço que pegue entradas até completar a palavra e que se diferente da letra da palavra pegue
 o contador e some mais um até completar 6, se chegar em 6 saia do laço. 
Quando pegar as entradas, varrer a string palavra_chave verificando se tem alguma letra informado
que tem na palavra_chave, se sim, conte mais um para acertos e mostre quantas letras faltam para 
completar a palavra, se não conte mais um para erros e mostre quantos erros já tem.
Deixar todas as letras minuscula depois da entrada
'''
palavra_chave = 'jose'
acertos, erros, falta_quanto = 0,0,0
tamanho_palavra = len(palavra_chave)

while True:
    print('!!!!!!!!!!BEM VINDO AO JOGO DA FORCA!!!!!!!!!!')
    print('!!!!VOCE TEM 6 TENTATIVAS DE ERROS NO TOTAL!!!!')

    entrada = input('INFORME UMA LETRA: ').lower()    
    
    if entrada in palavra_chave:        # se tem a palavra na frase, acertos soma mais um 
        acertos += 1
        print(f'voce tem "{acertos}" acertos e "{erros}" erros')
    
    elif entrada not in palavra_chave:  # se diferente erros soma mais um 
        erros += 1
        print(f'voce tem "{acertos}" acertos e "{erros}" erros')

    # se quantidade de acertos igual a palavra chave, saia do programa e exiba voce ganhou
    if acertos == tamanho_palavra:
        print(f'****PARABENS****, voce descobriu a palavra chave: {palavra_chave.upper()}')
        break
    elif erros > 5:
        print(f'****QUE PENA VOCE PERDEU****, a palavra chave era: {palavra_chave.upper()}')
        break