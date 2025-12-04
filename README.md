
# 🔔 Monitor Inteligente de Cotações USD/BRL
 ## Sistema Python avançado para monitoramento em tempo real do dólar com alertas automáticos de variação.

## 🚀 Visão Geral
- Monitor automatizado que detecta mudanças na cotação USD/BRL e emite alertas quando o preço sobe ou desce, mostrando a magnitude da variação.

## ✨ Funcionalidades Principais
- ✅ Monitoramento em tempo real da cotação dólar/real

- ✅ Sistema de alertas inteligente que detecta subidas e quedas

- ✅ Cálculo automático da magnitude das variações

- ✅ Histórico simples (armazena última cotação)

- ✅ Tratamento robusto de erros (conexão e dados)

- ✅ Interface clara com separadores visuais

- ✅ Timeout configurável (5 segundos)

## 📦 Instalação e Uso
```
 Clone o repositório ou baixe o arquivo
 Instale a única dependência:
 pip install requests

 Execute o monitor:
python monitor_dolar.py

 Para monitoramento contínuo (Linux/Mac):
while true; do python monitor_dolar.py; sleep 300; done  # A cada 5 minutos
````
## 📊 Exemplo de Saída
```
Monitor de Cotação do Dólar
---------------------------------------
Alerta! O preço subiu! de R$5.20 para R$5.25
Aumento de R$0.05
Cotação atual: R$5.25
---------------------------------------
````
## 🏗️ Arquitetura do Sistema
- Fluxo principal:
```
1. Consulta API → 2. Compara com valor anterior → 3. Gera alerta → 4. Atualiza histórico
Componentes:
Alarme(): Lógica de detecção de variações

Valor(): Gerenciador principal das operações

Contaçao_Anterior: Armazenamento em memória do último valor
````

## 🔧 Tecnologias Utilizadas
- Python 3.8+ - Linguagem principal

- Requests 2.31+ - Comunicação HTTP com API

- AwesomeAPI - Fonte de dados econômicos

- Sistema de Timeout - Prevenção de travamentos

## 🛡️ Tratamento de Erros
 O sistema lida com:

- ✅ Perda de conexão com a internet

- ✅ API fora do ar

- ✅ Respostas mal formatadas

- ✅ Timeouts (5 segundos)

- ✅ Dados JSON inválidos
