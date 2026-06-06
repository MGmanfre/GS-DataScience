import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("current_catalog.csv")

tudo = []
colunas = []

list_of_columns = df.columns.tolist()
for column in list_of_columns:
    colunas.append(column)
    colunas.append(df[column].duplicated().sum())
    tudo.append(colunas)
    colunas = []

#mostra numeros repitidos por coluna
for i in range(len(tudo)):
    print(f"{tudo[i][0]}: {tudo[i][1]}")

#grafico de barras que indica a quantidade de satélites por país
nomes = df["country"].value_counts()[:20].index
quantidade = df["country"].value_counts()[:20].values

plt.boxplot(quantidade)

plt.title("Quantidade de Satélites por País")
plt.xlabel("País")
plt.ylabel("Quantidade")


plt.show()