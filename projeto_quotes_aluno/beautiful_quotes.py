import requests
import urllib3
from bs4 import BeautifulSoup
from conexao_ora_aluno import conectar_oracle

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def coletar_citacoes():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('span', class_='text')
    author = soup.find_all('small', class_='author')

    # print(quotes)
    # print(author)
    dados = [(q.text.strip('""'), a.text) for q, a in zip(quotes, author)]
    # print(dados)
    return dados

def salvar_oracle(dados):
    conn = conectar_oracle()
    if conn:
        sql = "INSERT INTO quotes(quote_text, author_name) VALUES (:1, :2)"
        cursor = conn.cursor()
    try:
        cursor.executemany(sql, dados)
        conn.commit()
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir: {e}")
    finally:
        cursor.close()
        conn.close()



if __name__ == '__main__':
    dados = coletar_citacoes()
    salvar_oracle(dados)