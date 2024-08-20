import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
df = pd.read_csv(file_path)

# Lista das colunas que você deseja analisar
columns_to_analyze = ["GP P/I 1º", "GP P/I 2º", "GP P/I 3º", "GP P/I 4º", "GP P/I 5º"]

# Loop sobre as colunas e calcular contagens e percentuais
results = {}
for column in columns_to_analyze:
    counts = df[column].value_counts().sort_index()
    total_samples = counts.sum()
    percentages = (counts / total_samples) * 100
    results[column] = pd.DataFrame({
        "Paridade (0 - Par, 1 - Ímpar)": [f"{i}: {counts.iloc[i]} x ({percentages.iloc[i]:.2f}%)" for i in range(2)]
    })

# Exibir os resultados
for column, result_df in results.items():
    print(f"Resultados para {column}:")
    print(result_df)
    print()
