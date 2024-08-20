import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
df = pd.read_csv(file_path)

# Lista das colunas que você deseja analisar
columns_to_analyze = ["D 1º", "D 2º", "D 3º", "D 4º", "D 5º"]

# Inicializar um dicionário para armazenar as contagens de cada dezena
dezena_counts = {str(i).zfill(2): 0 for i in range(100)}

# Loop sobre as colunas e calcular contagens de cada dezena
for column in columns_to_analyze:
    for index, value in df[column].items():
        if pd.notna(value) and 0 <= value < 100:  # Verificar se o valor não é NaN e está entre 0 e 99
            dezena = str(value).zfill(2)  # Converter para string e preencher com zero à esquerda, se necessário
            dezena_counts[dezena] += 1

# Calcular a média das contagens de cada dezena
total_samples = sum(dezena_counts.values())
dezena_average = {dezena: (count, count / total_samples * 100) for dezena, count in dezena_counts.items()}

# Exibir os resultados
print("Média e quantidade de ocorrências entre |D1º| ao |D5º| DEZENA E UNIDADE:")
for dezena, (count, average) in dezena_average.items():
    print(f"Dezena {dezena}: Quantidade: {count}, Média: {average:.2f}%")
