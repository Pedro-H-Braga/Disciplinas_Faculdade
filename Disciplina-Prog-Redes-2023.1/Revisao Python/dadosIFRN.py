<<<<<<< HEAD
import requests

url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

dados = requests.get(url).json()


# Questão 01: Listar os campi e a sua 
# quantidade de alunos
campi = set(map(lambda c: c['campus'], dados))
for campus in campi:
    filtro = lambda c: c['campus'] == campus
    alunos = list(filter(filtro, dados))
    qt_alunos = len(alunos)
    print(f'Campus {campus}: {qt_alunos} Alunos')


# Questão 02: Solicitar a sigla de um campus e listar os cursos do
#             campus e a quantidade de alunos de cada curso 

=======
import requests

url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

dados = requests.get(url).json()


# Questão 01: Listar os campi e a sua 
# quantidade de alunos
'''
campi = set(map(lambda c: c['campus'], dados))
for campus in campi:
    filtro = lambda c: c['campus'] == campus
    alunos = list(filter(filtro, dados))
    qt_alunos = len(alunos)
    print(f'Campus {campus}: {qt_alunos} Alunos')
    print(alunos)
'''
# Questão 02: Solicitar a sigla de um campus e listar os cursos do
#             campus e a quantidade de alunos de cada curso 

# input para pegar o campi
in_campi = input('Informe o Campi: ') 
# pegando todos os dados do campi
filtro_campi = lambda c: c['campus'] == in_campi
dados_campi = list(filter(filtro_campi, dados))

# criar lista com todos os cursos para filtrar da lista dados_campi
# pegando todos os cursos de maneira única 
todos_cursos = set(map(lambda c: c['curso'], dados_campi))

# para cada curso em todos_cursos pegue a quantidade de aparições daquele curso na lista
for curso in todos_cursos:
    # filto
    aluns = list(map(lambda c: c == curso, dados_campi))
    # tamanho da lista gerada por cada aparição de cada curso
    qt_al_curso = len(aluns)  
    # Exibindo
    print(f'{curso} tem: {qt_al_curso} Alunos')
>>>>>>> 3e1a20d4407c1489d8823be810ebd50825d980b6
