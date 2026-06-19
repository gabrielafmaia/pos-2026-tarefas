import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

# user = input("user: ")
# password = getpass()

# data = {"username":user,"password":password}

# response = requests.post(api_url+"token/pair", json=data)
# token = response.json()["access"]
# print(response.json())

token = ""
headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

ano = input("Digite o ano letivo: ")
periodo = input("Digite o período: ")
url = api_url+f"ensino/meu-boletim/{ano}/{periodo}/"
print(url)
response = requests.get(url, headers=headers)

disciplinas = response.json()["results"]
for disciplina in disciplinas:
    print(f"{disciplina['disciplina']} - "f"{disciplina['nota_etapa_1']['nota']} - "f"{disciplina['nota_etapa_2']['nota']} - "f"{disciplina['nota_etapa_3']['nota']} - "f"{disciplina['nota_etapa_4']['nota']}")
print(response)
