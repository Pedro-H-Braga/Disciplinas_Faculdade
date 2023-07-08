import requests

API_KEY = '6393292683:AAFNdH8vA74bNrrwTpJsaZFx30CZ4bLWI0o'

url_req = f'https://api.telegram.org/bot{API_KEY}'

requisicao = requests.get(url_req + '/getUpdates')

print(requisicao.status_code)
print(requisicao.json())

id_chat = int(input('Informe o ID do chat: '))

resposta = {'chat_id':id_chat,'text':'Olá...'}

envio = requests.post(url_req+'/sendMessage',data=resposta)