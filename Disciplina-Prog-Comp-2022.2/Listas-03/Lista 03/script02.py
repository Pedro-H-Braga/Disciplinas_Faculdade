'''
Faça um programa que solicite ao usuário um valor inteiro positivo e liste todos os seus divisores ou
informar que o número é primo caso não existam divisores diferentes de 1 e dele mesmo.

lógica do programa:
- Fazer IF pra ver se é positivo 
- Exibir divisores: 
* fazer um while que pega as divisões que tem resto zero do número X
* condição que fará as divisões até chegar em numero_teclado
* Sendo preciso de 2 variaveis:
° 1 pra guardar as divisões e em seguida exibir 
° Outra que guardará o número do teclado

- Fazer if de ignorar o resto 0 em número X ter resto 0 em 1 e pelo própio número X  
(Ou se divisores == 2 --> Número Primo)
- Se número X não tiver restos, exibir que ele é primo
'''

numero_teclado = int(input("Informe para ver seus divisores: "))

if numero_teclado > 0:
    contador = 0 # contador de laço que inicia em 0 até o numero informado
    contador_primos = 0 # contador de laço que inicia em 0 e conta + 1 para fazer se contador_primos == 2 é primo
    while contador < numero_teclado:   # fazer até ser menor que o numero informado   
        contador += 1 # contador receber mais 
        if (numero_teclado % contador) == 0: # fazer os restos de 0 até o numero informado 
            contador_primos += 1
            print(contador, end=' - ')
    
    if contador_primos == 2:
        print(f"\n{numero_teclado} E um numero PRIMO")
    else: print(f"\n{numero_teclado} NAO e PRIMO")
            
        
else: print(f"Valor Negativo:{numero_teclado}")