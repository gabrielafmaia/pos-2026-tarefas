from xml.dom.minidom import parse
import json

dom = parse("tarefa09/imobiliaria.xml")
imoveis = dom.getElementsByTagName("imovel")

dados = []

for imovel in imoveis:
    item = {}
    for elemento in imovel.childNodes:
        if elemento.nodeType == 1:
            if elemento.getElementsByTagName("*"):
                subitem = {}
                for filho in elemento.childNodes:
                    if filho.nodeType == 1:
                        subitem[filho.tagName] = filho.firstChild.nodeValue
                item[elemento.tagName] = subitem
            else:
                item[elemento.tagName] = elemento.firstChild.nodeValue
    dados.append(item)

with open("tarefa09/imobiliaria.json", "w") as arquivo:
    json.dump(dados, arquivo)