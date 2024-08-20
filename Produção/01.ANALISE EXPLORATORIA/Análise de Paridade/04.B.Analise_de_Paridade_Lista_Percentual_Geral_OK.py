import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
df = pd.read_csv(file_path)

# Lista das colunas que você deseja analisar
columns_to_analyze = ["GP P/I 1º", "GP P/I 2º", "GP P/I 3º", "GP P/I 4º", "GP P/I 5º"]

# Inicializar um dicionário para armazenar as contagens de cada tipo de paridade
paridade_counts = {"Par": 0, "Ímpar": 0}

# Loop sobre as colunas e calcular contagens de cada tipo de paridade
for column in columns_to_analyze:
    for value in df[column]:  # Iterar diretamente sobre os valores da coluna
        if pd.notna(value):  # Verificar se o valor não é NaN
            # Verificar se o valor é "PAR" ou "IMPAR" antes de tentar converter para inteiro
            if value.upper() == "PAR":
                paridade_counts["Par"] += 1
            elif value.upper() == "IMPAR":
                paridade_counts["Ímpar"] += 1

# Calcular a média das contagens de paridade
total_samples = sum(paridade_counts.values())
paridade_average = {paridade: (count, count / total_samples * 100) for paridade, count in paridade_counts.items()}

# Exibir os resultados
print("Média e quantidade de ocorrências de paridade (Ímpar ou Par):")
for paridade, (count, average) in paridade_average.items():
    print(f"{paridade}: Quantidade: {count}, Média: {average:.2f}%")
