import pandas as pd

# Lê o arquivo "dados.csv" como um DataFrame do Pandas
df = pd.read_csv("dados.csv")

# Grava o DataFrame como um arquivo "dados.json"
df.to_json("dados.json", orient="records")

