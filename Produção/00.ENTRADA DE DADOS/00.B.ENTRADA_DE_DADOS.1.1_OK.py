import pandas as pd
import numpy as np
from io import StringIO
import os
import logging
from datetime import datetime, timedelta
import re
from babel.dates import format_date, Locale

logging.basicConfig(level=logging.INFO)

class AtualizadorDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.nomes_colunas = [
            "Concurso", "Data", "D/SEMAN",
            "1º PRÊMIO", "S 1º", "MC 1º", "MC P/I 1º", "P/I 1º", "D 1º", "D P/I 1º", "GP 1º", "GP P/I 1º", "BICHO 1º",
            "2º PRÊMIO", "S 2º", "MC 2º", "MC P/I 2º", "P/I 2º", "D 2º", "D P/I 2º", "GP 2º", "GP P/I 2º", "BICHO 2º",
            "3º PRÊMIO", "S 3º", "MC 3º", "MC P/I 3º", "P/I 3º", "D 3º", "D P/I 3º", "GP 3º", "GP P/I 3º", "BICHO 3º",
            "4º PRÊMIO", "S 4º", "MC 4º", "MC P/I 4º", "P/I 4º", "D 4º", "D P/I 4º", "GP 4º", "GP P/I 4º", "BICHO 4º",
            "5º PRÊMIO", "S 5º", "MC 5º", "MC P/I 5º", "P/I 5º", "D 5º", "D P/I 5º", "GP 5º", "GP P/I 5º", "BICHO 5º"
        ]

        self.tabela_grupos = {
            "01": {"grupo": "AVESTRUZ", "dezenas": ["01", "02", "03", "04"]},
            "02": {"grupo": "ÁGUIA", "dezenas": ["05", "06", "07", "08"]},
            "03": {"grupo": "BURRO", "dezenas": ["09", "10", "11", "12"]},
            "04": {"grupo": "BORBOLETA", "dezenas": ["13", "14", "15", "16"]},
            "05": {"grupo": "CACHORRO", "dezenas": ["17", "18", "19", "20"]},
            "06": {"grupo": "CABRA", "dezenas": ["21", "22", "23", "24"]},
            "07": {"grupo": "CARNEIRO", "dezenas": ["25", "26", "27", "28"]},
            "08": {"grupo": "CAMELO", "dezenas": ["29", "30", "31", "32"]},
            "09": {"grupo": "COBRA", "dezenas": ["33", "34", "35", "36"]},
            "10": {"grupo": "COELHO", "dezenas": ["37", "38", "39", "40"]},
            "11": {"grupo": "CAVALO", "dezenas": ["41", "42", "43", "44"]},
            "12": {"grupo": "ELEFANTE", "dezenas": ["45", "46", "47", "48"]},
            "13": {"grupo": "GALO", "dezenas": ["49", "50", "51", "52"]},
            "14": {"grupo": "GATO", "dezenas": ["53", "54", "55", "56"]},
            "15": {"grupo": "JACARÉ", "dezenas": ["57", "58", "59", "60"]},
            "16": {"grupo": "LEÃO", "dezenas": ["61", "62", "63", "64"]},
            "17": {"grupo": "MACACO", "dezenas": ["65", "66", "67", "68"]},
            "18": {"grupo": "PORCO", "dezenas": ["69", "70", "71", "72"]},
            "19": {"grupo": "PAVÃO", "dezenas": ["73", "74", "75", "76"]},
            "20": {"grupo": "PERU", "dezenas": ["77", "78", "79", "80"]},
            "21": {"grupo": "TOURO", "dezenas": ["81", "82", "83", "84"]},
            "22": {"grupo": "TIGRE", "dezenas": ["85", "86", "87", "88"]},
            "23": {"grupo": "URSO", "dezenas": ["89", "90", "91", "92"]},
            "24": {"grupo": "VEADO", "dezenas": ["93", "94", "95", "96"]},
            "25": {"grupo": "VACA", "dezenas": ["97", "98", "99", "00"]}
        }

    def _ler_arquivo_csv(self):
        try:
            with open(self.caminho_arquivo, 'r') as file:
                return file.read()
        except Exception as e:
            logging.error(f'Erro ao ler o arquivo CSV: {str(e)}')
            return None

    def _carregar_dados_csv(self):
        dados_csv = self._ler_arquivo_csv()
        if dados_csv:
            dados_io = StringIO(dados_csv)
            dados = pd.read_csv(dados_io, names=self.nomes_colunas, skiprows=1, dtype=str)
            dados['Concurso'] = dados['Concurso'].astype(int)
            return dados
        else:
            return None

    def _completar_paridade(self, dados):
        for i in range(1, 6):
            coluna_s = f'S {i}º'
            coluna_p_i = f'P/I {i}º'

            dados[coluna_p_i] = dados[coluna_s].apply(
                lambda x: f'[{",".join(["P" if int(digito) % 2 == 0 else "I" for digito in str(x).zfill(4)])}]'
                if pd.notnull(x) else '[0000]'
            )

    def _validar_data_formato(self, data):
        return re.match(r'\d{4}-\d{2}-\d{2}', data) is not None

    def _tratar_erro_valor_invalido(self, mensagem):
        while True:
            valor = input(mensagem)
            if valor.isdigit() and len(valor) <= 4:
                return valor.zfill(4)
            else:
                print("Formato inválido. Os resultados devem ter 4 dígitos. Tente novamente.")

    def _validar_data_concurso(self, data):
        try:
            data_concurso = datetime.strptime(data, '%Y-%m-%d')
            dia_semana = data_concurso.weekday()
            if dia_semana == 2 or dia_semana == 5:
                return True
            else:
                return False
        except ValueError:
            return False

    def _obter_bicho(self, dezena):
        for grupo, info in self.tabela_grupos.items():
            if dezena in info["dezenas"]:
                return info["grupo"]

    def _obter_nova_linha(self, dados):
        novo_concurso = dados['Concurso'].iloc[-1] + 1
        logging.info(f"Concurso a ser atualizado: {novo_concurso}")

        while True:
            try:
                nova_data = input("Digite a data (0000-00-00) para o novo concurso: ")

                if self._validar_data_formato(nova_data) and self._validar_data_concurso(nova_data):
                    break
                else:
                    print(
                        "Data inválida para o sorteio. Tente novamente ou escolha uma data válida para quarta-feira ou sábado.")
            except ValueError:
                print("Por favor, digite uma data válida.")

        nova_linha = pd.DataFrame({'Concurso': [novo_concurso], 'Data': [nova_data]})

        for coluna in ["1º PRÊMIO", "2º PRÊMIO", "3º PRÊMIO", "4º PRÊMIO", "5º PRÊMIO"]:
            while True:
                valor = self._tratar_erro_valor_invalido(f"Digite o resultado para {coluna}: ")
                nova_linha[coluna] = np.array([valor.rjust(4, '0')])
                break

        for i in range(1, 6):
            coluna_bicho = f'BICHO {i}º'
            coluna_premio = f'{i}º PRÊMIO'

            resultado = nova_linha[coluna_premio].iloc[0].zfill(4)

            nova_linha[coluna_bicho] = self._obter_bicho(resultado)

        return nova_linha

    def _atualizar_dados(self, dados):
        nova_linha = self._obter_nova_linha(dados)
        dados = pd.concat([dados, nova_linha], ignore_index=True)
        dados.to_csv(self.caminho_arquivo, index=False)
        logging.info("Dados atualizados e salvos com sucesso!")
        return dados

    def _preencher_MC_e_D(self, dados):
        for i in range(1, 6):
            coluna_premio = f'{i}º PRÊMIO'
            coluna_mc = f'MC {i}º'
            coluna_d = f'D {i}º'

            dados[coluna_mc] = dados[coluna_premio].apply(lambda x: str(x).zfill(4)[:2] if pd.notnull(x) else '00')
            dados[coluna_d] = dados[coluna_premio].apply(lambda x: str(x).zfill(4)[2:] if pd.notnull(x) else '00')

    def _preencher_GP(self, dados):
        for i in range(1, 6):
            coluna_premio = f'{i}º PRÊMIO'
            coluna_gp = f'GP {i}º'

            dados[coluna_gp] = dados[coluna_premio].apply(lambda x: str(x)[-2:])

            def converter_dezena_para_grupo(dezena):
                return str((int(dezena) - 1) // 4 + 1).zfill(2)

            dados[coluna_gp] = dados[coluna_gp].apply(converter_dezena_para_grupo)

    def _preencher_BICHO(self, dados):
        for i in range(1, 6):
            coluna_premio = f'{i}º PRÊMIO'
            coluna_bicho = f'BICHO {i}º'

            dados[coluna_bicho] = dados[coluna_premio].apply(lambda x: str(x)[-2:])

            def obter_nome_grupo_animal(dezena):
                for grupo, info in self.tabela_grupos.items():
                    if dezena in info["dezenas"]:
                        return info["grupo"]

            dados[coluna_bicho] = dados[coluna_bicho].apply(obter_nome_grupo_animal)

    def _auto_completar(self):
        dados = self._carregar_dados_csv()
        if dados is not None and not dados.empty:
            dados['Data'] = pd.to_datetime(dados['Data'])
            locale = Locale('pt_BR')
            dados['D/SEMAN'] = dados['Data'].apply(
                lambda x: format_date(x, 'EEEE', locale=locale) if pd.notnull(x) else ''
            )

            self._preencher_MC_e_D(dados)

            for i in range(1, 6):
                coluna_premio = f'{i}º PRÊMIO'
                coluna_s = f'S {i}º'
                dados[coluna_s] = dados[coluna_premio].apply(
                    lambda x: f'[{",".join(str(x).zfill(4))}]' if pd.notnull(x) else '[0000]'
                )

            self._preencher_GP(dados)
            self._preencher_BICHO(dados)

            dados.to_csv(self.caminho_arquivo, index=False)
            logging.info("Colunas 'MC 1º a D 5º', 'GP 1º a GP 5º' e 'BICHO 1º a BICHO 5º' preenchidas com sucesso!")
        else:
            logging.error("Não foi possível carregar os dados para auto completar.")

    def _auto_completar_paridade_mc(self):
        dados = self._carregar_dados_csv()
        if dados is not None and not dados.empty:
            for i in range(1, 6):
                coluna_mc = f'MC {i}º'
                coluna_d = f'D {i}º'
                coluna_mc_p_i = f'MC P/I {i}º'
                coluna_d_p_i = f'D P/I {i}º'

                dados[coluna_mc_p_i] = dados[coluna_mc].apply(
                    lambda x: f'[{",".join(["P" if int(digito) % 2 == 0 else "I" for digito in str(x).zfill(2)])}]'
                    if pd.notnull(x) else '[00]'
                )

                dados[coluna_d_p_i] = dados[coluna_d].apply(
                    lambda x: f'[{",".join(["P" if int(digito) % 2 == 0 else "I" for digito in str(x).zfill(2)])}]'
                    if pd.notnull(x) else '[00]'
                )

            dados.to_csv(self.caminho_arquivo, index=False)
            logging.info("Colunas 'MC P/I 1º a MC P/I 5º' e 'D P/I 1º a D P/I 5º' preenchidas com sucesso!")
        else:
            logging.error("Não foi possível carregar os dados para auto completar paridade.")

    def _auto_completar_paridade_premio(self):
        dados = self._carregar_dados_csv()
        if dados is not None and not dados.empty:
            for i in range(1, 6):
                coluna_premio = f'{i}º PRÊMIO'
                coluna_p_i = f'P/I {i}º'

                dados[coluna_p_i] = dados[coluna_premio].apply(
                    lambda x: f'[{",".join(["P" if int(digito) % 2 == 0 else "I" for digito in str(x).zfill(4)])}]'
                    if pd.notnull(x) else '[0000]'
                )

            dados.to_csv(self.caminho_arquivo, index=False)
            logging.info("Colunas 'P/I 1º a P/I 5º' preenchidas com sucesso!")
        else:
            logging.error("Não foi possível carregar os dados para auto completar paridade.")

    def paridade_de_grupo(self, dados):
        for i in range(1, 6):
            coluna_gp = f'GP {i}º'
            coluna_gp_p_i = f'GP P/I {i}º'

            dados[coluna_gp_p_i] = dados[coluna_gp].apply(
                lambda x: 'PAR' if int(x) == 0 or int(x) % 2 == 0 else 'IMPAR'
                if pd.notnull(x) else 'PAR'
            )

        dados.to_csv(self.caminho_arquivo, index=False)
        logging.info("Colunas 'GP P/I 1º a GP P/I 5º' preenchidas com sucesso!")

    def _excluir_concurso(self, dados):
        try:
            concurso_excluir = int(input("Digite o número do concurso a ser excluído: "))

            if concurso_excluir in dados['Concurso'].values:
                dados = dados[dados['Concurso'] != concurso_excluir]
                dados.to_csv(self.caminho_arquivo, index=False)
                logging.info(f"Concurso {concurso_excluir} excluído com sucesso!")
            else:
                logging.warning(f"Concurso {concurso_excluir} não encontrado.")
        except ValueError:
            logging.error("Por favor, digite um número válido.")

    def menu_opcoes(self):
        while True:
            print("\nMENU DE OPÇÕES:")
            print("1. Atualização de Dados")
            print("2. Excluir Concurso")
            print("3. Auto Completar Paridade MC")
            print("4. Auto Completar Paridade Prêmio")
            print("5. Paridade de Grupo")
            print("6. Sair")

            try:
                opcao = int(input("Escolha uma opção: "))

                if opcao == 1:
                    dados = self._carregar_dados_csv()
                    if dados is not None and not dados.empty:
                        self._atualizar_dados(dados)
                    else:
                        logging.error("Não foi possível carregar os dados para atualizar.")
                elif opcao == 2:
                    dados = self._carregar_dados_csv()
                    if dados is not None and not dados.empty:
                        self._excluir_concurso(dados)
                    else:
                        logging.error("Não foi possível carregar os dados para excluir concurso.")
                elif opcao == 3:
                    self._auto_completar_paridade_mc()
                elif opcao == 4:
                    self._auto_completar_paridade_premio()
                elif opcao == 5:
                    dados = self._carregar_dados_csv()
                    if dados is not None and not dados.empty:
                        self.paridade_de_grupo(dados)
                    else:
                        logging.error("Não foi possível carregar os dados para realizar a paridade de grupo.")
                elif opcao == 6:
                    logging.info("Encerrando o programa.")
                    break
                else:
                    logging.warning("Opção inválida. Escolha uma opção de 1 a 6.")
            except ValueError:
                logging.error("Por favor, digite um número válido.")


if __name__ == "__main__":
    caminho_pasta = '/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS'
    nome_arquivo = 'Base_2024.csv'
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

    atualizador = AtualizadorDados(caminho_arquivo)

    # Definindo o formato de exibição para manter os zeros à esquerda
    pd.set_option("display.float_format", lambda x: f"{x:04}")

    atualizador.menu_opcoes()
