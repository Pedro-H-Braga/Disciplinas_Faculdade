'''
    O TSE divulga na sua página oficial um webservice que fornece os dados 
    das apurações das eleições realizadas no Brasil.

    O fragmento de código a seguir monta um dicionário (dados_retorno) com o 
    resultado das eleições do ano de 2022 no 1º turno para Presidente.

    Com base na documentação da API contida na URL 
    https://www.tse.jus.br/eleicoes/eleicoes-2022/interessados-na-divulgacao-de-resultados-2022


    Pede-se que seja desenvolvido um programa que solicite ao usuário o 
    ano da eleição, tipo de eleição (estadual, nacional) e o cargo eletivo 
    e o programa  deverá montar um dicionário {k:v} no seguinte formato:
    {
        num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                         'votos': quantidade_votos, 
                         'percentual': percentual_votos},
        num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                         'votos': quantidade_votos, 
                         'percentual': percentual_votos},
        ...
    }
    
    O dicionário deverá ser ordenado de forma decrescente pela quantidade de
    votos que o candidato obteve.

    Em seguida, deverá ser gerado um arquivo (resultados.csv) onde na 
    primeira linha deverá constar a seguinte string:
        numero;nome,partido;quantidade_votos;percentual_votos

    Da segunda linha em diante deverão constar os dados correspondentes de
    cada candidato

    url_original = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'
'''

import requests
a - g
print(f'\
Tipos de eleições:\n\
------------------------\n\
* 544 - Eleição Federal\n\
* 546 - Eleição Estadual\n\
------------------------\n\
* Sigla UF em minúsculo\n\
------------------------\n\
Cargos da eleição:\n\
* 0001 Presidente\n\
* 0003 Governador\n\
* 0005 Senador\n\
* 0011 Prefeito\n\
* 0006 Deputado Federal\n\
* 0007 Deputado Estadual\n\
* 0008 Deputado Distrital\n\
* 0013 Vereador\n\
------------------------\n\
')
'''
# ano
ano_eleicoes = str(input('Informe o ano da eleição: '))
# tipo
tipo_eleicoes = str(input('Informe o código do tipo de eleição: '))
if tipo_eleicoes == '546': sigla_uf = str(input('Informe o estado: '))
else: sigla_uf = 'br'
# cargo
cargo_eleicoes = str(input('Informe o código do cargo da eleição: '))
'''
ano_eleicoes    = '2022'
tipo_eleicoes   = '544'
cargo_eleicoes  = '0001'
sigla_uf        = 'br'
url = f'https://resultados.tse.jus.br/oficial/ele{ano_eleicoes}/{tipo_eleicoes}/dados-simplificados/{sigla_uf}/{sigla_uf}-c{cargo_eleicoes}-e000{tipo_eleicoes}-r.json'
dados_ele = requests.get(url).json() # é um DICIONARIO com LISTAS com DICIONARIOS dentro
#print(dados_retorno)


# Lista com os dados dos candidatos, cada elemento da lista é um dicionario e cada dicionario tem sua chave:valor
lista_ele = list(dados_ele["cand"])
# lista que pegará os dados dos candidatos
cabecalho     = 'num_candidato;nome;partido;votos;percentual'
lista_aux     = []
lista_valores = []

#     CRIANDO ARQUIVO COM SAIDA
arq_csv = open('Apuracoes_TSE.csv', mode='w',encoding='utf-8')
arq_csv.write(f'{cabecalho}\n')
# laço para percorrer a lista, para cada posição pega um dict e um determinado valor
for dicio in lista_ele:
    num_candidato    = dicio["sqcand"]
    nome_candidato   = dicio["nm"]
    nome_partido     = dicio["cc"]
    quantidade_votos = dicio["vap"]
    percentual_votos = dicio["pvap"]

    #print(num_candidato)
    #print(nome_candidato)
    #print(nome_partido)
    #print(quantidade_votos)
    #print(percentual_votos)


    dict_candidato = {
            num_candidato: { 'nome': nome_candidato, 'partido': nome_partido, 
                            'votos': quantidade_votos, 
                            'percentual': percentual_votos},
        }
    # adicionando a uma lista os valores 
    lista_valores.append(f'{num_candidato};{nome_candidato};{nome_partido};{quantidade_votos};{percentual_votos};')

for dados in lista_valores:        
    arq_csv.writelines(f'{dados}\n')

arq_csv.close()

print('Arquivo criado com sucesso!')

#print(lista_valores)
'''
    # formatação
    dados_dict.append(num_candidato)
    formatacao = list(dict_candidato[num_candidato].values())
    for dado in formatacao:
        dados_dict.append(dado)
    # lista de dicionario com dados dos candidatos
    
#lista_dados.append(dados_dict)
'''
   
'''
print('dict_candidato', dict_candidato)
#     CRIANDO ARQUIVO COM SAIDA
with open('Apuracoes_TSE.csv', mode='w',encoding='utf-8') as saida:
    # percorrer dicionario e de acordo com a ordem, escrever no arquivo para formato csv
    for dicio in dados_dict:
        
        print(f'DICIO: {dicio}')    

        for header in lista_dados:
            # formato de saida do arquivo.csv
            lista_dados.append(dict_candidato[num_candidato])
            saida.writelines(lista_dados)
'''
'''
for enum,pos in enumerate(dados_ele):
    print(f'pos: {pos}')
    if enum == 5: break
'''
'''
    filtro = lambda c: c['campus'] == campus
    alunos = list(filter(filtro, dados))
    dict_candidatos = {
            num_candidato: { 'nome ': nome_candidato, 'partido': nome_partido, 
                            'votos': quantidade_votos, 
                            'percentual': percentual_votos},
        }
'''
'''

COMO É PRA SER AS REQUISIÇÕES:
Solicitar da eleição:
        Ano
        Sigla do estado
        Cargo 
        Id 
Ex: 544/546

- Dependendo do estado fica:
'https://resultados.tse.jus.br/oficial/ele{ano_eleicoes}/{tipo_eleicoes}/dados-simplificados/{SIGLA-ESTADO}/{SIGLA-ESTADO}-c{CARGO}-e000{tipo_eleicoes}-r.json'
'''