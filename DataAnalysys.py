"""
Você trabalha em uma emrpesa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
Isso representa uma perda de milhões para a empresa.
O que a empresa precisa fazer para resolver isso?

"""
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "vscode"

# Importar as bases de dados da empresa
tabela = pd.read_csv(r'C:\Users\User\OneDrive\Documentos\pythonLira\telecom_users.csv')

# Visualizar as bases de dados
# - entender quais as informações que temos
# - descobrir as cagadas da base de dados
tabela = tabela.drop('Unnamed: 0', axis=1) # deletando coluna inútil

# tratamento de dados
# - valores reconhecidos da forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - valores vazios
# -- colunas completamente vazias
tabela = tabela.dropna(how="all", axis=1)

# -- linhas com pelo menos 1 valor vazio
tabela = tabela.dropna(how="any", axis=0)

# análise inicial (entender como estão os cancelamentos)
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True))

# análise completa (entender o motivo do cancelamento)
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.show()

# print(tabela.info())

# criar soluções a partir dos gráficos