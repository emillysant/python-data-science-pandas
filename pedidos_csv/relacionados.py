import pandas as pd

def risco():
    print("-" * 110)


# Lendo os arquivos CSV usando o método read_csv
clientes_df = pd.read_csv("clientes.csv")
pedidos_df = pd.read_csv("pedidos.csv")

risco()
print(clientes_df)
risco()
print(pedidos_df)
risco()

# # Fazendo o merge dos dois DataFrames usando o método merge e especificando o campo cliente_id como chave
resultado = pedidos_df.merge(clientes_df, how='inner', left_on="cliente_id", right_on="id")

# # Mostrando o resultado
print(resultado)
