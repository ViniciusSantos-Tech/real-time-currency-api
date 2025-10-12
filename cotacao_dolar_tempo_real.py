import requests

url = "http://economia.awesomeapi.com.br/json/last/USD-BRL"

dados = requests.get(url)

Resposta = dados.json()


contaçao_Dolal = Resposta['USDBRL']['bid']


print(f"A contaçao do dolar é: {float(contaçao_Dolal):.2f}")

print(f"A contaçao do real é: {1/float(contaçao_Dolal):.2f}")

