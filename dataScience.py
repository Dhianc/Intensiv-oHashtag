"""
O desafio é conseguir prever as vendas que vamos ter em determinado período com base nos gastos em anúncios
nas 3 grandes redes que a empresa investe: TV, jornal e rádio

Tv, rádio e jornal estão em milhares de reais
Vendas está em milhões

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


# Entendimento do desafio
# Entendimento da área/empresa
# Extração/obtenção de dados
tabela = pd.read_csv('advertising.csv')
# print(tabela)

# ajuste de dados (tratamento/limpeza)
# print(tabela.info())

# Análise exploratória
sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)
plt.show()

# modelagem + algoritmos
y = tabela["Vendas"] # quem eu quero prever 
x = tabela[["TV", "Radio", "Jornal"]] # quem vou usar pra prever

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

# interpretação de resultados
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)

print(r2_score(y_teste, previsao_arvoredecisao))
print(r2_score(y_teste, previsao_regressaolinear))

tabela_nova = pd.read_csv('novo.csv')
previsao = modelo_arvoredecisao.predict(tabela_nova)
print(previsao)