'''
(USAR LISTAS E/OU TUPLAS) Fazer um programa que efetue a leitura dos arquivos que estão contidos
no arquivo serie_historica_anp.rar1 e realize as seguintes operações (descompacte o arquivo em um
diretório/pasta chamado serie_historica_anp): Observação: o programa deverá reconhecer a inclusão
de novos arquivos no diretório/pasta sem ser necessária a alteração no código fonte.

A lista gerada deverá ser salva em um único arquivo chamado serie_historica_anp.txt dentro do
diretório criado no item a. Cada informação deverá ser separada por ; (ponto e vírgula).
'''
import os
from script01_B import lista_valores

# pegando caminho absoluto do local deste arquivo e adicionando o local que eu quero executar
father_path = os.path.dirname(os.path.abspath(__file__))
file_path   = father_path + '\\dados_estatisticos\\' 

nome_arquivo = 'serie_historica_anp.txt'
file_txt = f'{file_path+nome_arquivo}'  

valores_txt = [valores+';' for valores in lista_valores]

# criando arquivo txt
arq_txt_anp = open(file_txt, 'w+', encoding='utf-8')
arq_txt_anp.writelines(valores_txt)
arq_txt_anp.close()


print('ARQUIVO CRIADO')