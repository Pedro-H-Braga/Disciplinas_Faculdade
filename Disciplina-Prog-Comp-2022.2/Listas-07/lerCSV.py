#-------------------------------------------------------------------
# Lendo os arquivos CSV para manipulação
import os
import csv

try:
    father_path = os.path.dirname(os.path.abspath(__file__))
    file_path   = father_path + '\\dados_estatisticos' 
    data_path   = file_path   + '\\serie_historica_anp'

    path_pyFiles = list(os.listdir(data_path))
except:
    print('ARQUIVO INEXISTENTE')

for path_file in path_pyFiles: 
    csv_file  =  open(data_path+f'\{path_file}', 'r', encoding='utf-8') 

    reader_csv = csv.DictReader(csv_file,restkey=0, restval=0 ,delimiter=';')
    dados_csv = tuple(reader_csv)

    csv_file.close()

DADOS_CSV = dados_csv


# print(f'O tamanho do arquivo é: {len(dados_csv)}')
# print(dados_csv[0],end='\n')
# print(dados_csv[10])

