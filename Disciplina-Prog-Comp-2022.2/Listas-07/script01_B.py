
# (USAR LISTAS E/OU TUPLAS) Fazer um programa que efetue a leitura dos arquivos que estão contidos
# no arquivo serie_historica_anp.rar e realize as seguintes operações (descompacte o arquivo em um
# diretório/pasta chamado serie_historica_anp): Observação: o programa deverá reconhecer a inclusão
# de novos arquivos no diretório/pasta sem ser necessária a alteração no código fonte.

# Deverá ser gerada uma lista contendo as seguintes informações de todos os arquivos lidos: 
# '\ufeffRegiao - Sigla', 'Estado - Sigla', 'Produto', 'Data da Coleta', 'Valor de Venda', 'Bandeira';

# LÓGICA PARA DESCOMPACTAR O ARQUIVO:
# caminho do winrar para descompactar: "C:\Program Files\WinRAR\UnRAR.exe"

# from rarfile import RarFile
# RarFile.UNRAR_TOOL='C:\Program Files\WinRAR\UnRAR.exe'

# with RarFile('test.rar') as file:
#     file.extract(file.namelist())

# pip install patool
# import patoolib
# patoolib.extract_archive("foo_bar.rar", outdir="path here")


from os import getcwd,walk,path
from minhasFuncoes import espacamento,criaLista
import patoolib
import time

tempo_exec_inicial = time.time()


paths = fr'{getcwd()}\Docs da lista'
print(espacamento(),'caminho arquivos python:', paths)

for _,_,arq in walk(paths):
    lista_arquivos = arq
print(lista_arquivos)
# Verificando se a pasta series_anp ja existe e pulando o código se já existir
path_pyExiste = fr'{getcwd()}\Python Files\dados_estatisticos\serie_historica_anp'
existe = path.exists(path_pyExiste)
# descompactando e levando os arquivos para a pasta (fazer tratamento de error se a pasta não existir)
path_pyFiles = fr'{getcwd()}\Python Files\dados_estatisticos'
if existe == False:
    patoolib.extract_archive(f"{paths}\serie_historica_anp.rar", outdir=path_pyFiles)
else:
    print(espacamento(),'OS ARQUIVOS JÁ FORAM DESCOMPACTADOS PARA:', path_pyFiles)
    pass

# --------------------------------------------------------
# Lendo os csv's e criando uma lista 
#lista_valores = set()
lista_valores = list(criaLista(f'\ufeffRegiao - Sigla', 'Estado - Sigla', 'Produto', 'Data da Coleta', 'Valor de Venda', 'Bandeira'))


tempo_exec_final = time.time()
tempo_exec = int(tempo_exec_final - tempo_exec_inicial)

print(espacamento(),f'<<ARQUIVO LIDO COM SUCESSO>>')
print(f'O tamanho do arquivo é: {len(lista_valores)} linhas')
print(f'Tempo de execução do código SCRIPT_B: {tempo_exec} segundos')
print(espacamento())
