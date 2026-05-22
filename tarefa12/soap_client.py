import requests

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

codigo = input("Digite o código do país: ")
operacao = input("Digite 1 para código telefônico, 2 para moeda e 3 para nome do país: ")

if operacao == "1":
    funcao = "CountryIntPhoneCode"
elif operacao == "2":
    funcao = "CountryCurrency"
elif operacao == "3":
    funcao = "CountryName"
else:
    print("Opção inválida!")
    exit()

payload =f"""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <{funcao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
                <sCountryISOCode>{codigo}</sCountryISOCode>
                </{funcao}>
            </soap:Body>
            </soap:Envelope>"""

# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}

# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
print(response.text)
dom = parseString(response.text)
response = dom.documentElement.getElementByTagName("m:CountryNameResult")[0].firstChild.nodeValue
print(response)