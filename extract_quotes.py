import re

# Caminho para o arquivo "My Clipings.txt"
file_path = "kind-to-notion/My Clipings.txt"

# Função para extrair as citações do arquivo e escrevê-las em "quotes.txt"
def extract_quotes():
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
        quotes = re.findall(r"^(.*?)\s*\((.*?)\)\s*\n- (.*?)\n\n", contents, re.MULTILINE)
        with open("quotes.txt", "w", encoding="utf-8") as output_file:
            for quote in quotes:
                output_file.write(f"{quote[0]}\n{quote[1]}\n{quote[2]}\n\n")

# Chame a função para extrair as citações
extract_quotes()
