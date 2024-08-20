import pandas as pd


# Função para ajustar os números para terem 4 dígitos
def ajustar_numeros(numero):
    return str(numero).zfill(4)


# Função para carregar e ajustar o DataFrame
def carregar_dataframe(file_path):
    # Carregar o arquivo CSV em um DataFrame do Pandas
    df = pd.read_csv(file_path)

    # Ajustar todos os números do DataFrame para terem 4 dígitos
    df = df.applymap(ajustar_numeros)

    return df


# Função para encontrar os números de milhar não sorteados em uma coluna de prêmio
def numeros_nao_sorteados_coluna(df, premio):
    # Criar um conjunto para armazenar os números sorteados nesta coluna de prêmio
    numeros_sorteados = set(df[premio])

    # Criar uma lista com todos os números de milhar de 0000 a 9999
    todos_numeros = set(str(numero).zfill(4) for numero in range(10000))

    # Encontrar os números de milhar que não foram sorteados nesta coluna de prêmio
    numeros_nao_sorteados = todos_numeros - numeros_sorteados

    return numeros_nao_sorteados


# Função para exibir os números não sorteados e o total por premio
def exibir_numeros_nao_sorteados_coluna(numeros_nao_sorteados, premio):
    print(f"\nNúmeros de milhar não sorteados no {premio}:")
    for idx, numero in enumerate(sorted(numeros_nao_sorteados), start=1):
        print(numero, end=", ")
        if idx % 10 == 0:
            print()
    print("\nTotal de números de milhar não sorteados no", premio + ":", len(numeros_nao_sorteados))


# Função para analisar os números não sorteados por premio
def analisar_numeros_nao_sorteados(df, premio):
    premio_coluna = f"{premio}º PRÊMIO"
    numeros_nao_sorteados = numeros_nao_sorteados_coluna(df, premio_coluna)
    exibir_numeros_nao_sorteados_coluna(numeros_nao_sorteados, premio_coluna)


# Função para exibir o menu de escolha
def exibir_menu():
    print("\nEscolha uma opção:")
    print("1 - Analisar 1º Prêmio")
    print("2 - Analisar 2º Prêmio")
    print("3 - Analisar 3º Prêmio")
    print("4 - Analisar 4º Prêmio")
    print("5 - Analisar 5º Prêmio")
    print("6 - Analisar números não sorteados em geral")
    print("7 - Sair")


# Caminho do arquivo CSV
file_path = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"

# Carregar e ajustar o DataFrame
df = carregar_dataframe(file_path)

# Loop para exibir o menu e processar a escolha do usuário
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "7":
        print("Programa encerrado.")
        break

    elif escolha in ["1", "2", "3", "4", "5"]:
        premio = int(escolha)
        analisar_numeros_nao_sorteados(df, premio)

    elif escolha == "6":
        numeros_sorteados = set()
        for coluna in ["1º PRÊMIO", "2º PRÊMIO", "3º PRÊMIO", "4º PRÊMIO", "5º PRÊMIO"]:
            numeros_sorteados.update(df[coluna].astype(str))

        todos_numeros = set(str(numero).zfill(4) for numero in range(10000))
        numeros_nao_sorteados = todos_numeros - numeros_sorteados

        exibir_numeros_nao_sorteados_coluna(numeros_nao_sorteados, "Geral")

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
