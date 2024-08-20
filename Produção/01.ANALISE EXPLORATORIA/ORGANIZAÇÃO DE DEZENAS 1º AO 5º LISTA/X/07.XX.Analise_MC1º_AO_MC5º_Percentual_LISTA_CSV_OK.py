# Importar a biblioteca pandas
import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
df = pd.read_csv(file_path)

# Lista das colunas que você deseja analisar
columns_to_analyze = ["MC 1º", "MC 2º", "MC 3º", "MC 4º", "MC 5º"]

# Inicializar uma lista para armazenar os resultados
results_data = []

# Loop sobre as colunas e calcular contagens e percentuais
for column in columns_to_analyze:
    counts = df[column].value_counts().sort_index()
    total_samples = counts.sum()
    percentages = (counts / total_samples) * 100

    # Adicionar os resultados à lista de dados
    for i in range(100):
        value = i if i in counts.index else None
        count = counts[i] if i in counts.index else None
        percentage = percentages[i] if i in percentages.index else None
        results_data.append({"Column": column, "Value": value, "Count": count, "Percentage": percentage})

# Criar o DataFrame a partir da lista de dados
results_df = pd.DataFrame(results_data)

# Escrever o DataFrame de resultados em um arquivo CSV
results_file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/RELATÓRIOS DEZENA MC/PERCENTUAL DE DEZENA DE 00A99 DO 1 AO 5 LISTA/Resultados.csv"
results_df.to_csv(results_file_path, index=False)
