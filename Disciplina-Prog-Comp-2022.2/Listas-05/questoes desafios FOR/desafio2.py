lst_uf        = ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe']
lst_siglas    = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
lst_populacao = [3365351, 14985284, 9240580, 7153262, 4059905, 9674793, 3289290, 3560903, 2338474]

soma_populacao = 0
# Imprimir na tela os dados obedecendo o seguinte layout:
for x in range(len(lst_uf)):
# 'O estado NOME_ESTADO (SIGLA) possui (QUANTIDADE) habitantes'
    print(f'O estado {lst_siglas[x]} possui {lst_populacao[x]} habitantes')
    soma_populacao += lst_populacao[x]
# E no final imprimir a seguinte informação:
# 'O Nordeste possui um total de (QUANTIDADE TOTAL) habitantes'
print(f'O Nordeste possui um total de {soma_populacao} habitantes')
