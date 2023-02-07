import pandas as pd

# Lendo os arquivos CSV usando o método read_csv
clientes_df = pd.read_csv("clientes.csv")
pedidos_df = pd.read_csv("pedidos.csv")

print("-" * 110)
print(clientes_df)
print("-" * 110)
print(pedidos_df)
print("-" * 110)

# Fazendo o merge dos dois DataFrames usando o método merge e especificando o campo cliente_id como chave
resultado = pd.merge(clientes_df, pedidos_df, on="cliente_id")

# Mostrando o resultado
print(resultado)
