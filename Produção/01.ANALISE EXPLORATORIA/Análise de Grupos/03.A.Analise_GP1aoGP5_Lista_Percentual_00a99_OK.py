import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
df = pd.read_csv(file_path)

# Lista das colunas que você deseja analisar
columns_to_analyze = ["GP 1º", "GP 2º", "GP 3º", "GP 4º", "GP 5º"]

# Inicializar um dicionário para armazenar as contagens de cada número de 0 a 25
number_counts = {str(i).zfill(2): 0 for i in range(26)}

# Loop sobre as colunas e calcular contagens de cada número de 0 a 25
for column in columns_to_analyze:
    for index, value in df[column].items():
        if pd.notna(value) and 0 <= value <= 25:  # Verificar se o valor não é NaN e está entre 0 e 25
            number = str(value).zfill(2)  # Converter para string e preencher com zero à esquerda, se necessário
            number_counts[number] += 1

# Calcular a média das contagens de cada número de 0 a 25
total_samples = sum(number_counts.values())
number_average = {number: (count, count / total_samples * 100) for number, count in number_counts.items()}

# Exibir os resultados
print("Média e quantidade de ocorrências de GRUPOS de 0 a 25 em cada coluna:")
for number, (count, average) in number_average.items():
    print(f"Número {number}: Quantidade: {count}, Média: {average:.2f}%")
