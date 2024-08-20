import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Plotar o gráfico de barras empilhadas em 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'b', 'y', 'g']  # Alterando a ordem das cores para evitar a sobreposição do verde com o azul
for i, (casa_decimal, color) in enumerate(zip(contagem_df.columns, colors)):
    ax.bar(contagem_df.index, contagem_df[casa_decimal], zs=i, zdir='y', color=color, alpha=0.8)

ax.set_xlabel('Dígito')
ax.set_ylabel('')
ax.set_zlabel('Contagem')
ax.set_yticks(range(len(contagem_df.columns)))
ax.set_yticklabels('')

plt.title('Contagem de dígitos na coluna "Prêmio" em 3D')
plt.show()
