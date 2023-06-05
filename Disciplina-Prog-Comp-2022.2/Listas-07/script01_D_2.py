'''
(USAR LISTAS E/OU TUPLAS) Fazer um programa que efetue a leitura dos arquivos que estão contidos
no arquivo serie_historica_anp.rar1 e realize as seguintes operações (descompacte o arquivo em um
diretório/pasta chamado serie_historica_anp): Observação: o programa deverá reconhecer a inclusão
de novos arquivos no diretório/pasta sem ser necessária a alteração no código fonte.
'''
import os
from minhasFuncoes import criaLista, espacamento
import time

tempo_exec_inicial = time.time()

# pegando caminho absoluto do local deste arquivo e adicionando o local que eu quero executar
father_path = os.path.dirname(os.path.abspath(__file__))
file_path   = father_path + '\\dados_estatisticos\\' 

nome_arquivo = 'media_produto_regia.txt'
file_txt = f'{file_path+nome_arquivo}'  

# 'Regiao - Sigla', 'Estado - Sigla', 'Produto', 'Data da Coleta', 'Valor de Venda', 'Bandeira';
lista_valores_D2 = list(criaLista(f'Produto', f'\ufeffRegiao - Sigla', 'Data da Coleta'))

valores_txt = [valores+';' for valores in lista_valores_D2]

# criando arquivo txt
arq_txt_anp = open(file_txt, 'w+', encoding='utf-8')
arq_txt_anp.writelines(valores_txt)
arq_txt_anp.close()


tempo_exec_final = time.time()
tempo_exec = int(tempo_exec_final - tempo_exec_inicial)

print(espacamento())
print('ARQUIVO CRIADO')
print(f'O tamanho do arquivo é: {len(lista_valores_D2)} linhas')
print(f'Tempo de execução do código SCRIPT_D2: {tempo_exec} segundos')
print(espacamento())