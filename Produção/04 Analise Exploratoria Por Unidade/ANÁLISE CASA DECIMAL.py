import pandas as pd

def carregar_dados(caminho_arquivo):
    # Carregar o arquivo CSV
    return pd.read_csv(caminho_arquivo)

def ajustar_exibicao():
    # Ajustar a exibição para mostrar todas as informações em uma mesma linha
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)

def calcular_frequencia_numeros(dados):
    # Calcular a frequência dos números
    frequencia_numeros = dados.iloc[:, 3:].stack().value_counts().sort_index()
    return frequencia_numeros

def calcular_frequencia_por_posicao(dados):
    # Calcular a frequência por posição
    frequencia_por_posicao = dados.iloc[:, 3:].apply(pd.Series.value_counts).fillna(0)
    return frequencia_por_posicao

def calcular_atraso_numeros(dados):
    # Calcular o atraso dos números em relação ao número do concurso anterior
    atraso_numeros = dados.iloc[:, 3:].diff().fillna(0)
    # Arredondar os valores para números inteiros
    atraso_numeros = atraso_numeros.round().astype(int)
    return atraso_numeros

def analisar_geral(dados):
    print("\nFrequência por posição:")
    print(calcular_frequencia_por_posicao(dados))

def analisar_ultimos_concursos(dados, quantidade_concursos):
    print(f"\nAnalisando os últimos {quantidade_concursos} concursos:")
    dados_ultimos_concursos = dados.tail(quantidade_concursos)
    print("\nFrequência por posição:")
    print(calcular_frequencia_por_posicao(dados_ultimos_concursos))

def analisar_por_periodo(dados, data_inicio, data_fim):
    dados_periodo = dados[(dados['Data'] >= data_inicio) & (dados['Data'] <= data_fim)]
    print("\nFrequência por posição no período especificado:")
    print(calcular_frequencia_por_posicao(dados_periodo))

def main():
    caminho_arquivo = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024_Casa_Decimal.csv"
    dados_lotofacil = carregar_dados(caminho_arquivo)
    ajustar_exibicao()

    while True:
        print("\nMENU:")
        print("1. Analisar Geral")
        print("2. Analisar os últimos 5 concursos")
        print("3. Analisar os últimos 10 concursos")
        print("4. Analisar por período")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            analisar_geral(dados_lotofacil)
        elif opcao == "2":
            analisar_ultimos_concursos(dados_lotofacil, 5)
        elif opcao == "3":
            analisar_ultimos_concursos(dados_lotofacil, 10)
        elif opcao == "4":
            data_inicio = input("Digite a data de início (DD/MM/AAAA): ")
            data_fim = input("Digite a data de término (DD/MM/AAAA): ")
            analisar_por_periodo(dados_lotofacil, data_inicio, data_fim)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
