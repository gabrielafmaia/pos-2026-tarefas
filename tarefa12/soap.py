import requests
from xml.dom.minidom import parseString

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
op = input("Digite 1 para código telefônico, 2 para capital e 3 para nome do país: ")
if op == "1":
    operation = "CountryIntPhoneCode"
elif op == "2":
    operation = "CapitalCity"
elif op == "3":
    operation = "CountryName"
else:
    print("Código inválido!")

country_code = input("Digite o código do país: ")
# XML estruturado
payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				<soap:Body>
					<{operation} xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
						<sCountryISOCode>{country_code}</sCountryISOCode>
					</{operation}>
				</soap:Body>
			</soap:Envelope>"""
# headers
headers = {
	'Content-Type': 'text/xml; charset=utf-8'
}
# request POST
response = requests.request("POST", url, headers=headers, data=payload)

# imprime a resposta
if response.status_code == 200:
    if op == "1":
        print("O código telefônico do país é " + parseString(response.text).documentElement.getElementsByTagName("m:CountryIntPhoneCodeResult")[0].firstChild.nodeValue)
    elif op == "2":
        print("A capital do país é " + parseString(response.text).documentElement.getElementsByTagName("m:CapitalCity")[0].firstChild.nodeValue)
    elif op == "3":
        print("O nome do país é " + parseString(response.text).documentElement.getElementsByTagName("m:CountryName")[0].firstChild.nodeValue)

