import oracledb

def conectar_oracle():
    user="rm569578"
    dsn="oracle.fiap.com.br:1521/orcl"
    password=input("Digite a sua senha: ")

    try:
        conn = oracledb.connect(user= user, dsn= dsn, password= password)
        print("Conexão estabelecida com sucesso!")
        return conn
    except oracledb.DatabaseError as e:
        (erro,) = e.args
        print(f"Erro ao conectar ao oracle: {erro.message}")
        return None

def testar_conexao():
    conn = conectar_oracle()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT sysdate FROM dual")  # Faz a consulta
        resultado = cursor.fetchone()               # Recupera só uma linha no formato de tupla
        print(f"Teste ok: {resultado[0]}")          # Tupla não muda de tamanho nem de itens.
        cursor.close()                              # Fechando a linha
        conn.close()


testar_conexao()
