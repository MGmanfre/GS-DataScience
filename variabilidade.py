import pandas as pd

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
