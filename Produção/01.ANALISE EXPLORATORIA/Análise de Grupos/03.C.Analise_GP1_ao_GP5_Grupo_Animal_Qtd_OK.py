import pandas as pd

# Carregar o arquivo CSV em um DataFrame
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
df = pd.read_csv(file_path)

# Lista das colunas que você deseja analisar
columns_to_analyze = ["GP 1º", "GP 2º", "GP 3º", "GP 4º", "GP 5º"]

# Dicionário de conversão de números para animais
tabela_grupos = {
    "01": "AVESTRUZ", "02": "ÁGUIA", "03": "BURRO", "04": "BORBOLETA", "05": "CACHORRO",
    "06": "CABRA", "07": "CARNEIRO", "08": "CAMELO", "09": "COBRA", "10": "COELHO",
    "11": "CAVALO", "12": "ELEFANTE", "13": "GALO", "14": "GATO", "15": "JACARÉ",
    "16": "LEÃO", "17": "MACACO", "18": "PORCO", "19": "PAVÃO", "20": "PERU",
    "21": "TOURO", "22": "TIGRE", "23": "URSO", "24": "VEADO", "25": "VACA",
}

# Inicializar um dicionário para armazenar as contagens de cada animal
animal_counts = {animal: 0 for animal in tabela_grupos.values()}

# Loop sobre as colunas e calcular contagens de cada animal
for column in columns_to_analyze:
    for index, value in df[column].items():
        if pd.notna(value) and str(value).zfill(2) in tabela_grupos:
            # Verificar se o valor não é NaN e está presente no dicionário tabela_grupos
            animal = tabela_grupos[str(value).zfill(2)]
            animal_counts[animal] += 1

# Calcular a média das contagens de cada animal
total_samples = sum(animal_counts.values())
animal_average = {animal: (count, count / total_samples * 100) for animal, count in animal_counts.items()}

# Exibir os resultados
print("Média e quantidade de ocorrências de cada animal em todas as colunas:")
for animal, (count, average) in animal_average.items():
    print(f"Animal: {animal}, Quantidade: {count}, Média: {average:.2f}%")
