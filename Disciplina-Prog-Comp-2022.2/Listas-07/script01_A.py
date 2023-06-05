'''
(USAR LISTAS E/OU TUPLAS) Fazer um programa que efetue a leitura dos arquivos que estão contidos
no arquivo serie_historica_anp.rar1 e realize as seguintes operações (descompacte o arquivo em um
diretório/pasta chamado serie_historica_anp): Observação: o programa deverá reconhecer a inclusão
de novos arquivos no diretório/pasta sem ser necessária a alteração no código fonte.

O programa deverá criar um diretório chamado dados_estatisticos na mesma pasta que está o
arquivo .py;
'''
from os import makedirs,getcwd
from minhasFuncoes import espacamento,criaLista
import time

tempo_exec_inicial = time.time()

paths_py = fr'{getcwd()}\Python Files'
print(espacamento()+str('Caminho informado:'), paths_py)

try:
    makedirs(fr'{paths_py}\dados_estatisticos')
    print('O DIRETORIO FOI CRIADO')
except FileExistsError:
    print('DIRETORIO JÁ EXISTENTE')

tempo_exec_final = time.time()

tempo_exec = int(tempo_exec_final - tempo_exec_inicial)

print(f'Tempo de execução do código: {tempo_exec} segundos')