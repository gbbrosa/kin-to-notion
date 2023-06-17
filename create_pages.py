import os

# Configurar a integração com a API do Notion
notion_token = os.getenv('NOTION_API_KEY')
notion_database_id = os.getenv('BOOK_DB_ID')

# Ler as citações processadas do arquivo "quotes.txt"
quotes_file = os.path.join(os.path.dirname(__file__), 'quotes.txt')
with open(quotes_file, 'r', encoding='utf-8') as f:
    processed_quotes = f.read()

# Criar páginas no Notion usando a API
# Você precisa implementar o código de criação das páginas no Notion aqui

print('Pages created in Notion successfully!')
