import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Caminho completo do arquivo de dados
caminho_arquivo = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024_Casa_Decimal.csv"

# Carregar os dados
try:
    dados = pd.read_csv(caminho_arquivo)
except FileNotFoundError:
    print(f"Arquivo não encontrado: {caminho_arquivo}")
    exit()
except pd.errors.EmptyDataError:
    print(f"Arquivo vazio: {caminho_arquivo}")
    exit()

# Especificar as colunas a serem analisadas
colunas_analisadas = [
    "M 1º", "C 1º", "D 1º", "U 1º",
    "M 2º", "C 2º", "D 2º", "U 2º",
    "M 3º", "C 3º", "D 3º", "U 3º",
    "M 4º", "C 4º", "D 4º", "U 4º",
    "M 5º", "C 5º", "D 5º", "U 5º"
]

# Verificar se todas as colunas especificadas estão presentes no DataFrame
colunas_faltantes = [col for col in colunas_analisadas if col not in dados.columns]
if colunas_faltantes:
    print(f"As seguintes colunas estão faltando no DataFrame: {colunas_faltantes}")
    exit()

# Função para calcular as três maiores probabilidades em uma coluna
def calcular_tres_maiores_probabilidades(coluna):
    contagens = coluna.value_counts(normalize=True)
    return contagens.nlargest(3).items()

# Iterar sobre cada coluna especificada e calcular as três maiores probabilidades
resultados = {}
for coluna in colunas_analisadas:
    resultados[coluna] = calcular_tres_maiores_probabilidades(dados[coluna])

# Cores para cada número de 0 a 9
cores = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

# Dividir as colunas em cinco grupos
grupos_colunas = np.array_split(colunas_analisadas, 5)

# Mapeamento de nomes de colunas
nome_coluna_map = {
    "M": "Milhar",
    "C": "Centena",
    "D": "Dezena",
    "U": "Unidade"
}

# Visualizações gráficas das probabilidades
for i, grupo in enumerate(grupos_colunas):
    fig, axs = plt.subplots(1, len(grupo), figsize=(16, 4))
    for j, coluna in enumerate(grupo):
        coluna_descricao = nome_coluna_map[coluna[0]] + " " + coluna[2:]
        probabilidades_completas = [(numero, probabilidade) for numero, probabilidade in resultados[coluna]]
        numeros, probabilidades = zip(*probabilidades_completas[:3])  # Selecionar apenas as três maiores probabilidades
        axs[j].bar(numeros, probabilidades, color=[cores[numero] for numero in numeros])
        axs[j].set_title(f"{coluna_descricao}")
        axs[j].set_xlabel("Número")
        axs[j].set_ylabel("Probabilidade")
        axs[j].set_ylim(0, 1)  # Para que todas as barras tenham o mesmo eixo Y
    plt.suptitle(f"Extração {i + 1}")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Função para calcular a probabilidade de cada número de 0 a 9 aparecer em uma coluna
def calcular_probabilidades(coluna):
    total = len(coluna)
    probabilidades = {}
    for i in range(10):
        count = (coluna == i).sum()
        probabilidades[i] = count / total
    return probabilidades

# Iterar sobre cada coluna especificada e calcular as probabilidades
resultados = {}
for coluna in colunas_analisadas:
    probabilidades = calcular_probabilidades(dados[coluna])
    resultados[coluna] = probabilidades

# Imprimir os resultados em formato tabular com quatro colunas por linha
print("Análise das probabilidades dos números de 0 a 9 em cada coluna:")
print("-" * 67)
for i in range(0, len(colunas_analisadas), 4):
    print("{:<10} {:<10} {:<10} {:<10}".format(*colunas_analisadas[i:i+4]))
    print("-" * 67)
    for numero in range(10):
        probabilidade_linha = [f"{resultados[coluna].get(numero, 0):.4f}" for coluna in colunas_analisadas[i:i+4]]
        probabilidade_linha.append(numero)
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(*probabilidade_linha))
    print("-" * 67)
