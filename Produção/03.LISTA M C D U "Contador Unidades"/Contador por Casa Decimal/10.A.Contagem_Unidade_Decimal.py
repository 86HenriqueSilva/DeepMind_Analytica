import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Lista_1ao5.csv')

# Preencher os valores da coluna 'Prêmio' com zeros à esquerda até atingir 4 dígitos
df['Prêmio'] = df['Prêmio'].astype(str).str.zfill(4)

# Inicializar os contadores para cada casa decimal
contadores = {'M': [0] * 10, 'C': [0] * 10, 'D': [0] * 10, 'U': [0] * 10}

# Iterar sobre os valores da coluna 'Prêmio' e contar os dígitos
for premio in df['Prêmio']:
    for i, digito_str in enumerate(str(premio)):
        if digito_str.isdigit():
            digito = int(digito_str)
            if i == 0:
                contadores['M'][digito] += 1
            elif i == 1:
                contadores['C'][digito] += 1
            elif i == 2:
                contadores['D'][digito] += 1
            elif i == 3:
                contadores['U'][digito] += 1

# Criar um DataFrame a partir dos contadores
contagem_df = pd.DataFrame(contadores)

# Substituir os valores dos contadores pelo número de vezes seguido de 'X'
contagem_df = contagem_df.apply(lambda x: x.astype(str) + 'X')

# Ajustar a exibição para que os valores estejam alinhados
contagem_df.index.name = ''
contagem_df.columns.name = ''
pd.set_option('display.unicode.east_asian_width', True)

# Exibir a contagem de dígitos por casa decimal
print("Contagem de dígitos na coluna 'Prêmio':")
print(contagem_df)
