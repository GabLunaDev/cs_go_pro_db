import csv
import mysql.connector

# Função para obter os nomes das colunas de uma tabela
def obter_nomes_colunas(cursor, tabela):
    cursor.execute(f"SELECT * FROM {tabela} LIMIT 1")
    colunas = [column[0] for column in cursor.description]
    cursor.fetchall()  # Ler todos os resultados para evitar o erro "Unread result found"
    return colunas

# Função para formatar os dados do arquivo CSV
def formatar_dados_csv(nome_arquivo):
    dados_formatados = []
    with open(nome_arquivo, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Remover o símbolo de porcentagem e converter para float
            for chave, valor in row.items():
                if '%' in valor:
                    row[chave] = float(valor.rstrip('%'))
            dados_formatados.append(row)
    return dados_formatados

# Função para conectar ao banco de dados MySQL e inserir os dados do arquivo CSV
def inserir_dados_mysql(host, user, password, database, dados_formatados, tabela):
    # Conectar ao banco de dados MySQL
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Obter os nomes das colunas da tabela
    colunas_tabela = obter_nomes_colunas(cursor, tabela)

    # Preparar a lista de colunas para a inserção
    colunas_para_inserir = [coluna for coluna in dados_formatados[0].keys() if coluna in colunas_tabela]

    # Query SQL para inserir os dados na tabela
    colunas = ", ".join(colunas_para_inserir)
    placeholders = ", ".join(["%s" for _ in colunas_para_inserir])
    query = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"

    # Inserir os dados na tabela
    cursor.executemany(query, [tuple(d[coluna] for coluna in colunas_para_inserir) for d in dados_formatados])

    # Commit para salvar as alterações no banco de dados
    conexao.commit()

    # Fechar o cursor e a conexão
    cursor.close()
    conexao.close()

# Chamada da função para formatar os dados do arquivo CSV
dados_formatados = formatar_dados_csv("C:\\Users\\danie\\OneDrive\\Área de Trabalho\\desisto\\caminho\\csgo_players.csv")

# Chamadas separadas da função para inserir dados no MySQL para cada tabela
inserir_dados_mysql(
    host="localhost",
    user="root",
    password="12345678",
    database="csgo_players",
    dados_formatados=dados_formatados,
    tabela="player"
)

inserir_dados_mysql(
    host="localhost",
    user="root",
    password="12345678",
    database="csgo_players",
    dados_formatados=dados_formatados,
    tabela="team"
)

inserir_dados_mysql(
    host="localhost",
    user="root",
    password="12345678",
    database="csgo_players",
    dados_formatados=dados_formatados,
    tabela="p_stat"
)

inserir_dados_mysql(
    host="localhost",
    user="root",
    password="12345678",
    database="csgo_players",
    dados_formatados=dados_formatados,
    tabela="weapon_stat"
)

inserir_dados_mysql(
    host="localhost",
    user="root",
    password="12345678",
    database="csgo_players",
    dados_formatados=dados_formatados,
    tabela="round_stat"
)