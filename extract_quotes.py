import os

clipings_file = os.path.join(os.path.dirname(__file__), 'My Clipings.txt')
quotes_file = os.path.join(os.path.dirname(__file__), 'quotes.txt')

# Extrair citações do arquivo "My Clipings.txt"
with open(clipings_file, 'r', encoding='utf-8') as f:
    clipings = f.read()

# Processar as citações e gravar no arquivo "quotes.txt"
# Você precisa implementar o código de processamento das citações aqui

with open(quotes_file, 'w', encoding='utf-8') as f:
    f.write('Processed quotes')  # Substitua esta linha pelo código de processamento das citações

print('Quotes extracted and saved successfully!')
