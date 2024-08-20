import pandas as pd
from datetime import datetime

def analisar_sorteios(arquivo_entrada, diretorio_saida):
    df = pd.read_csv(arquivo_entrada)
    resultados_por_dezena = {str(dezena): [] for dezena in range(100)}
    dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

    for index, row in df.iterrows():
        concurso = row['Concurso']
        data = row['Data']
        sorteios = [row[f'D {i}º'] for i in range(1, 6)]

        for i, sorteio in enumerate(sorteios, 1):
            dezena = str(sorteio)
            if dezena in resultados_por_dezena:
                atraso = concurso - resultados_por_dezena[dezena][-1]['Concurso'] if resultados_por_dezena[dezena] else 0
                if not resultados_por_dezena[dezena]:
                    resultados_por_dezena[dezena].append({'Concurso': concurso, 'Data': data, 'Dia da Semana': dias_da_semana[datetime.strptime(data, '%Y-%m-%d').weekday()],
                                                            'Sorteio': f'D {i}º', 'Dezena': dezena, 'Atraso': concurso})
                else:
                    resultados_por_dezena[dezena].append({'Concurso': concurso, 'Data': data, 'Dia da Semana': dias_da_semana[datetime.strptime(data, '%Y-%m-%d').weekday()],
                                                            'Sorteio': f'D {i}º', 'Dezena': dezena, 'Atraso': atraso})

    for dezena, resultados in resultados_por_dezena.items():
        if resultados:
            arquivo_saida = f"{diretorio_saida}/analise_de_dezena{dezena.zfill(2)}.csv"
            df_resultados = pd.DataFrame(resultados)
            df_resultados.to_csv(arquivo_saida, index=False)
            print(f"Os resultados para a dezena {dezena} foram salvos em '{arquivo_saida}'.")

arquivo_entrada = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Base_2024.csv"
diretorio_saida = "/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/RELATÓRIOS DEZENA DU/DU 00A99"
analisar_sorteios(arquivo_entrada, diretorio_saida)
