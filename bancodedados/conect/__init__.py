"""Esse módulo é composto por funções para conectar
o python ao banco de dados."""


import mysql.connector
from bancodedados.conect import *
from editext.cores import red


# Configuração do Banco de dados de destino
def config_mysql(host, usuário, senha, bancodedados):
    try:
        conexao = mysql.connector.connect(
            host=f'{host}',
            user=f'{usuário}',
            password=f'{senha}',
            database=f'{bancodedados}')
        return conexao
    except Exception as error:
        red(f'Erro: {error}')


# Intermediador entre config_mysql e o comando
def cursor(conexão):
    try:
        cursor = conexão.cursor()
        return cursor
    except Exception as error:
        red(f'Erro: {error}')


# Conecta a config com o comando e commita
def conexao(cursor, comando, config_mysql):
    try:
        cursor.execute(comando)
        config_mysql.commit()
    except Exception as error:
        red(f'Erro: {error}')
