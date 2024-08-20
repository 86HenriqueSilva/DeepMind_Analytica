import pandas as pd
from datetime import datetime

def resumo_dezenas(arquivo_entrada):
    df = pd.read_csv(arquivo_entrada)
    resultados_por_dezena = {str(dezena).zfill(2): [] for dezena in range(100)}
    dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

    for index, row in df.iterrows():
        concurso = row['Concurso']
        data = row['Data']
        sorteios = [row[f'D {i}º'] for i in range(1, 6)]

        for i, sorteio in enumerate(sorteios, 1):
            dezena = str(sorteio).zfill(2)
            if dezena in resultados_por_dezena:
                atraso = concurso - resultados_por_dezena[dezena][-1]['Concurso'] if resultados_por_dezena[dezena] else 0
                resultados_por_dezena[dezena].append({'Concurso': concurso, 'Data': data, 'Dia da Semana': dias_da_semana[datetime.strptime(data, '%Y-%m-%d').weekday()],
                                                       'Sorteio': f'D {i}º', 'Atraso': atraso})

    resumo_por_dezena = {}
    for dezena, resultados in resultados_por_dezena.items():
        if resultados:
            df_resultados = pd.DataFrame(resultados)
            df_resultados.sort_values(by='Concurso', ascending=False, inplace=True)
            resumo_por_dezena[dezena] = df_resultados

    return resumo_por_dezena

arquivo_entrada = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"

# Calcular resumo de dezenas
resumo = resumo_dezenas(arquivo_entrada)

# Encontrar o último concurso para cada dezena
ultimos_concursos = {dezena: df_resumo.iloc[0]['Concurso'] if not df_resumo.empty else 0 for dezena, df_resumo in resumo.items()}

# Encontrar o último concurso global
ultimo_concurso_global = max(ultimos_concursos.values())

# Atualizar atrasos para o último concurso global
for dezena, resultados in resumo.items():
    for index, row in resultados.iterrows():
        atraso = row['Concurso'] - ultimo_concurso_global
        resultados.at[index, 'Atraso'] = atraso if atraso != 0 else 0

# Imprimir resultados
for dezena, resultados in resumo.items():
    print(f"DEZENA {dezena}")
    print(f"Concurso de Referência: {ultimo_concurso_global}")
    for sorteio in ['D 1º', 'D 2º', 'D 3º', 'D 4º', 'D 5º']:
        sorteio_atual = resultados[resultados['Sorteio'] == sorteio]
        if not sorteio_atual.empty:
            ultimo_sorteio = sorteio_atual.iloc[0]
            print(f"Sorteio {sorteio}: Concurso {ultimo_sorteio['Concurso']} - Data {ultimo_sorteio['Data']} - Dia da Semana {ultimo_sorteio['Dia da Semana']} - Atraso {ultimo_sorteio['Atraso']}")
    print()
