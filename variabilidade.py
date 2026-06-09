import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("current_catalog.csv")

tudo = []
colunas = []

list_of_columns = df.select_dtypes(include='number')
for column in list_of_columns:
    colunas.append(column)
    colunas.append(df[column].std())
    tudo.append(colunas)
    colunas = []

#esse for mostra as colunas que tem variabilidade numericas.
for i in range(len(tudo)):
    # como o ID é unico por satélite, ele não tem variabilidade, por isso o if.
    if i > 0:
        print(f"{tudo[i][0]}: {tudo[i][1]}")

#grafico de barras que indica a quantidade de satélites por país
nomes = df["country"].value_counts()[:20].index
quantidade = df["country"].value_counts()[:20].values

plt.boxplot(quantidade)

plt.title("Quantidade de Satélites por País")
plt.xlabel("País")
plt.ylabel("Quantidade")


plt.show()
