import pandas as pd

# Leitura do arquivo
df = pd.read_csv('current_catalog.csv')

# Padronização dos nomes das colunas
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Limpeza básica de textos
colunas_texto = df.select_dtypes(include='object').columns
for col in colunas_texto:
    df[col] = df[col].astype(str).str.strip()

# Converter datas, se existir a coluna epoch
if 'epoch' in df.columns:
    df['epoch'] = pd.to_datetime(df['epoch'], errors='coerce')

# Quantidade antes da limpeza
antes = len(df)

# 1) Remove linhas totalmente duplicadas
df = df.drop_duplicates()

# 2) Remove duplicados com base no identificador principal
if 'norad_id' in df.columns:
    df = df.drop_duplicates(subset='norad_id', keep='first')
else:
    df = df.drop_duplicates(subset='name', keep='first')

# Quantidade depois da limpeza
depois = len(df)

print(f'Registros antes: {antes}')
print(f'Registros depois: {depois}')
print(f'Removidos: {antes - depois}')

# Salvar versão limpa
df.to_csv('df_satelites_limpo.csv', index=False)

df.head()