#Feito Por Vinicius Santos-Tech
import requests

Contaçao_Anterior = None

def Alarme(anterior, atual):
    if anterior is None:
        print("Nenhuma mudança (primeira leitura)")
        return
    
    if atual < anterior:
        print(f"Alerta! O preço caiu! de R${anterior:.2f} para R${atual:.2f}")
        print(f"Queda de R${anterior - atual:.2f}")
    elif atual > anterior:
        print(f"Alerta! O preço subiu! de R${anterior:.2f} para R${atual:.2f}")
        print(f"Aumento de R${atual - anterior:.2f}")
    else:
        print(f"Preço estável em R${atual:.2f}")

def Valor():
    global Contaçao_Anterior
    
    try:
        url = "http://economia.awesomeapi.com.br/json/last/USD-BRL"
        dados = requests.get(url, timeout=5)
        dados.raise_for_status()

        Resposta = dados.json()
        contaçao_Dolar = Resposta['USDBRL']['bid']
        ContaçaoAtual = float(contaçao_Dolar)
        
        print('---------------------------------------')
        Alarme(Contaçao_Anterior, ContaçaoAtual)
        print(f"Contação atual: R${ContaçaoAtual:.2f}")
        print("---------------------------------------")
        
        Contaçao_Anterior = ContaçaoAtual
        
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Erro ao processar dados: {e}")
        return None


print("Monitor de Cotação do Dólar")
Valor()
