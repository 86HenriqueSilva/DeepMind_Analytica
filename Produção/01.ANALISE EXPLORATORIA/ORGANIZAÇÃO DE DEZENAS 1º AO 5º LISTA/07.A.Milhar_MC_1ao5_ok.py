import pandas as pd

# Caminho do arquivo CSV
caminho_arquivo = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv(caminho_arquivo)

# Organizar as colunas e criar a nova coluna "MC 5/1" com base nas datas
nova_lista = []
for index, row in df.iterrows():
    data = row['Data']
    nova_lista.append({'Concurso': row['Concurso'], 'Data': data, 'MC 5/1': row['MC 5º']})
    nova_lista.append({'Concurso': row['Concurso'], 'Data': data, 'MC 5/1': row['MC 4º']})
    nova_lista.append({'Concurso': row['Concurso'], 'Data': data, 'MC 5/1': row['MC 3º']})
    nova_lista.append({'Concurso': row['Concurso'], 'Data': data, 'MC 5/1': row['MC 2º']})
    nova_lista.append({'Concurso': row['Concurso'], 'Data': data, 'MC 5/1': row['MC 1º']})

# Criar DataFrame a partir da lista
novo_df = pd.DataFrame(nova_lista)

# Salvar o novo DataFrame como um arquivo CSV
caminho_saida = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/RELATÓRIOS DEZENA MC/COLUNA MC/Organização_de_MC.csv"
novo_df.to_csv(caminho_saida, index=False)
