import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
df = pd.read_csv(file_path)

# Lista das colunas que você deseja analisar
columns_to_analyze = ["MC 1º", "MC 2º", "MC 3º", "MC 4º", "MC 5º"]

# Loop sobre as colunas e calcular contagens e percentuais
for column in columns_to_analyze:
    counts = df[column].value_counts().sort_index()
    total_samples = counts.sum()
    percentages = (counts / total_samples) * 100

    # Exibir os resultados para a coluna atual
    print(f"Resultados para {column}:")
    for i in range(100):
        count_str = f"{counts[i]:<5}" if i in counts.index else "     "
        percentage_str = f"{percentages[i]:.2f}%" if i in percentages.index else "     "
        print(f"{i:<5}{count_str}{percentage_str}")
    print()
