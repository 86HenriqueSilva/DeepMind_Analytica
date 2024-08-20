import pandas as pd
from datetime import datetime

# Função para realizar a análise dos sorteios
def analisar_sorteios(arquivo_entrada, arquivo_saida):
    # Carregar o arquivo CSV em um DataFrame do Pandas
    df = pd.read_csv(arquivo_entrada)

    # Inicializar uma lista para armazenar os resultados
    resultados = []

    # Inicializar o valor do primeiro concurso em que a dezena é exibida
    primeiro_concurso_dezena = None

    # Nomes dos dias da semana em português
    dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

    # Iterar sobre cada linha do DataFrame
    for index, row in df.iterrows():
        concurso = row['Concurso']
        data = row['Data']
        sorteios = [row['D 1º'], row['D 2º'], row['D 3º'], row['D 4º'], row['D 5º']]

        # Verificar em qual sorteio a dezena "0" foi sorteada
        for i, sorteio in enumerate(sorteios, 1):
            if sorteio == 0:  # Aqui consideramos que '0' indica a dezena sorteada
                # Calcular o atraso em relação ao último sorteio onde a dezena "0" foi sorteada
                atraso = concurso - resultados[-1]['Concurso'] if resultados else 0

                # Definir o valor do primeiro concurso em que a dezena é exibida
                if primeiro_concurso_dezena is None:
                    primeiro_concurso_dezena = concurso

                # Adicionar os resultados
                resultados.append({'Concurso': concurso, 'Data': data, 'Dia da Semana': dias_da_semana[datetime.strptime(data, '%Y-%m-%d').weekday()],
                                    'Sorteio': f'D {i}º', 'Dezena 0': sorteio, 'Atraso': atraso})
                break  # Interrompe a busca após encontrar a dezena "0" no sorteio atual

    # Definir o total de atraso na primeira linha
    if resultados:
        resultados[0]['Atraso'] = primeiro_concurso_dezena

    # Criar um DataFrame a partir dos resultados
    df_resultados = pd.DataFrame(resultados)

    # Salvar os resultados em um arquivo CSV
    df_resultados.to_csv(arquivo_saida, index=False)

    print(f"Os resultados foram salvos em '{arquivo_saida}'.")

# Chamada da função principal
arquivo_entrada = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
arquivo_saida = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/RELATÓRIOS DEZENA DU/analise_de_dezena01.csv"
analisar_sorteios(arquivo_entrada, arquivo_saida)
