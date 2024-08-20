import pyfiglet
from termcolor import colored

def generate_ascii_art(text, font="slant"):
    # Cria a arte ASCII com o texto fornecido usando uma fonte personalizada
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art

# Texto para a arte ASCII
name_text = "D U L C E"

# Define o acrônimo e suas descrições com cores diferentes
acronym = {
    "D": colored("        D-Digital", color='red'),
    "U": colored("U-Understanding", color='green'),
    "L": colored("L-Lottery", color='yellow'),
    "C": colored("C-Calculation", color='blue'),
    "E": colored("E-Expert", color='magenta')
}

# Define um tamanho padrão para a largura da tela
columns = 80

# Centraliza o nome na tela
name_ascii_art = generate_ascii_art(name_text)
name_ascii_art_lines = name_ascii_art.split('\n')
centered_name_ascii_art = [line.center(columns) for line in name_ascii_art_lines]

# Adiciona cor ao nome e exibe
for line in centered_name_ascii_art:
    colored_name_ascii_art = colored(line, color='cyan', attrs=['bold'])
    print(colored_name_ascii_art)

# Exibe o acrônimo em uma linha horizontal com cores diferentes para cada letra
acronym_line = ' '.join([acronym[letter] for letter in acronym])
print(acronym_line)

# Adiciona a data de criação
creation_date = "                                                                        26-04-2024 "  # Data fixa
print(creation_date)
