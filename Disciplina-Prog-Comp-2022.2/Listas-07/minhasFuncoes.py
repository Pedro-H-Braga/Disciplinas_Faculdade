'''
ARQUIVO DESTINADO A CRIAÇÃO DE FUNÇÕES PARA SEREM USADAS NOS CÓDIGOS
'''

#-------------------------------------------------------------------
# Para formatação de exibições
def espacamento():
    exibe = '-'*100
    return exibe+str('\n')



#-------------------------------------------------------------------
# cria lista de acordo com o argumento da função
def criaLista(*args):
    from lerCSV import DADOS_CSV
    
    lista_titulo = []
    lista_dados  = []
    for arg in args:
        lista_titulo.append(arg)
    contador = 0
    # percorre a lista de titulos e a tupla de dados_csv 
    for titulo in lista_titulo:
        for dado in DADOS_CSV:
            lista_dados.append(dado[titulo])

    return lista_dados
'''
import os
father_path = os.path.dirname(os.path.abspath(__file__))
file_path   = father_path + '\\dados_estatisticos' 
data_path   = file_path   + '\\serie_historica_anp'
print(f'caminho: {data_path}')
path_pyFiles = list(os.listdir(data_path))
print(f'caminho: {path_pyFiles}')
'''