import requests
import json

link_firebase = "###"


# Criando requisições com a biblioteca Requests

# POST()
dados = {'nome': 'Vilela', 'preco': 123, 'produto': 'teclado mecanico'}
requisicao = requests.post(f'{link_firebase}/Vendas/.json', data=json.dumps(dados))

print(requisicao)
print(requisicao.text)
