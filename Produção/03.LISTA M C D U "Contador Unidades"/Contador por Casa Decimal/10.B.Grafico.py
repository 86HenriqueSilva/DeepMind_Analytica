import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('/home/henrique/PycharmProjects/DeepMind_Analytica/DULCE IA/BASE DE DADOS/Lista_1ao5.csv')

# Preencher os valores da coluna 'Prêmio' com zeros à esquerda até
df['Prêmio'] = df['Prêmio'].astype(str).str.zfill(4)

# Inicializar os contadores para cada casa decimal
contadores = {'Milhar': [0] * 10, 'Centena': [0] * 10, 'Dezena': [0] * 10, 'Unidade': [0] * 10}

# Iterar sobre os valores da coluna 'Prêmio' e contar os dígitos
for premio in df['Prêmio']:
    for i, digito_str in enumerate(str(premio)):
        if digito_str.isdigit():
            digito = int(digito_str)
            if i == 0:
                contadores['Milhar'][digito] += 1
            elif i == 1:
                contadores['Centena'][digito] += 1
            elif i == 2:
                contadores['Dezena'][digito] += 1
            elif i == 3:
                contadores['Unidade'][digito] += 1

# Criar um DataFrame a partir dos contadores
contagem_df = pd.DataFrame(contadores)

# Plotar as barras para cada casa decimal
fig, axs = plt.subplots(1, 4, figsize=(15, 5))

# Cores para os dígitos
cores = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

for i, coluna in enumerate(contagem_df.columns):
    axs[i].bar(contagem_df.index, contagem_df[coluna], color=cores)
    axs[i].set_title(coluna)
    axs[i].set_xlabel('Dígito')
    axs[i].set_ylabel('Contagem')

plt.tight_layout()
plt.show()
