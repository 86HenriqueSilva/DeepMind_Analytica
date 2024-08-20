import pandas as pd

# Passo 1: Ler o arquivo CSV
caminho_arquivo = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
dados = pd.read_csv(caminho_arquivo)

# Passo 2: Selecionar apenas as colunas desejadas
colunas_selecionadas = ["Concurso", "Data", "D/SEMAN", "1º PRÊMIO", "2º PRÊMIO", "3º PRÊMIO", "4º PRÊMIO", "5º PRÊMIO"]
dados_selecionados = dados[colunas_selecionadas].copy()

# Passo 3 e 4: Criar novas colunas para cada casa decimal e preencher com zeros à esquerda
casas_decimais = {"M": 0, "C": 1, "D": 2, "U": 3}  # Dicionário para mapear as letras para as casas decimais
for premio in colunas_selecionadas[3:]:  # Ignorando as três primeiras colunas
    for letra, casa_decimal in casas_decimais.items():
        nova_coluna = f"{letra} {premio.split()[0]}"  # Remove o sufixo "PRÊMIO"
        dados_selecionados[nova_coluna] = dados_selecionados[premio].astype(str).str.zfill(4).str[casa_decimal]

# Passo 5: Exportar os dados tratados para um novo arquivo CSV
caminho_saida = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024_Casa_Decimal.csv"
dados_selecionados.drop(columns=colunas_selecionadas[3:], inplace=True)  # Remove as colunas dos prêmios originais
dados_selecionados.to_csv(caminho_saida, index=False)
