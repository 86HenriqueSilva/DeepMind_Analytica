import pandas as pd

# Caminho para o arquivo CSV
caminho_arquivo = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"

# Colunas que queremos selecionar
colunas_desejadas = ["Concurso", "Data", "D/SEMAN", "1º PRÊMIO", "2º PRÊMIO", "3º PRÊMIO", "4º PRÊMIO", "5º PRÊMIO"]

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv(caminho_arquivo, usecols=colunas_desejadas)

# Organizar os dados para ter um prêmio por linha
# Para isso, primeiro criamos uma lista vazia para armazenar os novos dados
novos_dados = []

# Iteramos sobre as linhas do DataFrame original
for index, row in df.iterrows():
    # Para cada linha, iteramos sobre as colunas de prêmios
    for i in range(1, 6):  # As colunas de prêmio vão de 1º PRÊMIO a 5º PRÊMIO
        # Criamos um novo dicionário com os dados do prêmio
        novo_registro = {
            "Concurso": row["Concurso"],
            "Data": row["Data"],
            "D/SEMAN": row["D/SEMAN"],
            "Prêmio": row[f"{i}º PRÊMIO"]  # Selecionamos o prêmio correspondente à coluna atual
        }
        # Adicionamos o novo registro à lista
        novos_dados.append(novo_registro)

# Transformamos a lista de dicionários em um novo DataFrame
novo_df = pd.DataFrame(novos_dados)

# Salvamos o novo DataFrame em um arquivo CSV
novo_df.to_csv("/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Lista_1ao5.csv", index=False)

# Visualizamos as últimas cinco linhas do novo DataFrame
print(novo_df.tail())
