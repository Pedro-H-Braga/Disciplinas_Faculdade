# Projeto 26/12/2022 Redes de Computadores

## Questão:
29.45.32.0/24 para endereçar três departamentos com VLSM, conforme a seguir:

- Departamento Financeiro com 55 hosts
- Departamento Comercial com 62 hosts
- Departamento Contábil com 20 hosts

Etapa 1: Responda
a) Quantos bits serão necessários para fazer a divisão
e obter pelo menos 3 subredes?

b) Quantos endereços de hosts válidos estarão
disponíveis em cada subrede?

c) Quais as novas máscaras de subrede de cada subrede?

d) Listar a faixa de endereços de cada subrede.

Etapa 2: Simule
a) Utilizando o Cisco Packet Tracer, configure o cenário encontrado na etapa 1.
b) Para cada departamento configure dois clientes: o primeiro host e o último host
c) Realize os testes de comunicação: i) entre as máquinas do mesmo departamento (mesma subrede) e ii) entre máquinas de departamentos diferentes (subredes diferentes). O que aconteceu?

### Resumo sobre VLSM:

Atividade para praticar o VLSM(Variable Length Subnet Mask):
    O VLSM é basicamente alocação de hots dinamicamente envés de estaticamente, exemplo:
Para dividir uma rede de 3 sub-redes com 30 hots cada, usariámos um SALTO de 32 para cada sub-rede, já pelo VLSM não seria necessário o SALTO de 32 para cada, e sim de acordo com a demanda de hots para cada sub-rede.

### Desenvolvimento lógico do projeto:
Seguindo a lógica do seguinte site:

https://www.geeksforgeeks.org/introduction-of-variable-length-subnet-mask-vlsm/
e do vídeo: 
https://www.youtube.com/watch?v=X8tboS6NZLA&list=TLPQMjcxMjIwMjK6sOUSjfBPng&index=2&ab_channel=HardwareRedesBrasil

1. Selecionando o tamanho dos blocos por requisito
Será necessário:
- Departamento Financeiro com 55 hosts
- Departamento Comercial com 62 hosts
- Departamento Contábil com 20 hosts
Soma total de host s 137: 

Seguindo o passo a passo do vídeo de (VLSM):

1° Dividir quantas sub-redes eu precisarei, quantos hosts teram cada uma

2° Achar mascaras que caibam cada quantidade de hosts de cada sub-rede, ex: dep. comercial 62 (pegar uma mascara ".64"(lembrar de base 2) e tirar 2 para rede, que dá 62 hosts válidos).
Sendo assim, criar essas máscaras para cada sub-rede.
- Lembrando da regra do octeto nas divisões das máscaras para cada sub-rede, ex: 2(elevado a)6 será igual a 2 uns(1) e 6 zeros(0) = 11000000
- ir somando os saltos com da última sub rede, ex:
sub-rede 1: 255.255.255.64                      64(2elevado6) 
sub-rede 2: 
255.255.255.64+2(elevado a N hosts) 8(2elevado3)->64 + 8 = 192, sendo assim a máscara da sub-rede2 será:
255.255.255.192 e assim por diante

3°

ANOTAÇÕES sobre cabos no packet tracer:

* MÁQUINAS DIFERENTES: cabo direto (cooper straight-through)
* MÁQUINAS IGUAIS: cabo crossover (cooper Cross-Over)
























