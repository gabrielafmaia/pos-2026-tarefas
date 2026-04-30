import json

with open("tarefa10/imobiliaria.json", "r") as arquivo:
    dados = json.load(arquivo)

nomes = {
    "nome": "Nome",
    "email": "Email",
    "telefone": "Telefone",
    "rua": "Rua",
    "bairro": "Bairro",
    "cidade": "Cidade",
    "número": "Número",
    "tamanho": "Tamanho",
    "numQuartos": "Número de quartos",
    "numBanheiros": "Número de banheiros"
}

print("---IMÓVEIS DISPONÍVEIS---")
for i in range(len(dados)):
    print(i + 1, "-", dados[i]["descricao"])

opcao = int(input("Digite o id do imóvel para saber mais: "))
imovel = dados[opcao - 1]

print("\n---DETALHES DO IMÓVEL---")
print("Descrição:", imovel["descricao"])
print("-----------------------")
print("Proprietário:")
for chave in imovel["proprietario"]:
    print(nomes[chave] + ":", imovel["proprietario"][chave])
print("-----------------------")
print("Endereço:")
for chave in imovel["endereco"]:
    print(nomes[chave] + ":", imovel["endereco"][chave])
print("-----------------------")
print("Características:")
for chave in imovel["caracteristicas"]:
    print(nomes[chave] + ":", imovel["caracteristicas"][chave])
print("-----------------------")
print("Valor:", imovel["valor"])