import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Caminho completo do arquivo de dados
caminho_arquivo = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024_Casa_Decimal.csv"

# Carregar os dados
dados = pd.read_csv(caminho_arquivo)

# Especificar as colunas a serem analisadas
colunas_analisadas = ["M 1º", "C 1º", "D 1º", "U 1º",
                      "M 2º", "C 2º", "D 2º", "U 2º",
                      "M 3º", "C 3º", "D 3º", "U 3º",
                      "M 4º", "C 4º", "D 4º", "U 4º",
                      "M 5º", "C 5º", "D 5º", "U 5º"]

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

# Cores para cada número de 0 a 9
cores = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

# Dividir as colunas em cinco grupos
grupos_colunas = [colunas_analisadas[i:i+4] for i in range(0, len(colunas_analisadas), 4)]

# Visualizações gráficas das probabilidades
for i, grupo in enumerate(grupos_colunas):
    fig, axs = plt.subplots(1, 4, figsize=(16, 4))
    for j, coluna in enumerate(grupo):
        numeros = list(resultados[coluna].keys())
        probabilidades = list(resultados[coluna].values())
        axs[j].bar(numeros, probabilidades, color=[cores[numero] for numero in numeros])
        axs[j].set_title(coluna)
        axs[j].set_xticks(range(10))
        axs[j].set_xlabel("Número")
        axs[j].set_ylabel("Probabilidade")
    plt.tight_layout()
    plt.show()
