import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
df = pd.read_csv(file_path)

# Lista das colunas que você deseja analisar
columns_to_analyze = ["MC 1º", "MC 2º", "MC 3º", "MC 4º", "MC 5º"]

# Loop sobre as colunas e calcular contagens e percentuais
results = {}
for column in columns_to_analyze:
    counts = df[column].value_counts().sort_index()
    total_samples = counts.sum()
    percentages = (counts / total_samples) * 100
    results[column] = pd.DataFrame({
        f"00-49 ({column})": [f"{i}: {counts[i]} x ({percentages[i]:.2f}%)" for i in range(50)],
        f"50-99 ({column})": [f"{i}: {counts[i]} x ({percentages[i]:.2f}%)" for i in range(50, 100)]
    })

# Exibir os resultados
for column, result_df in results.items():
    print(f"Resultados para {column}:")
    print(result_df)
    print()
