"""Esse módulo é composto por funções que modificam
o banco de dados realizando as operações do C.R.U.D.
(CREATE, READ, UPDATE e DELETE)"""

from time import sleep

from bancodedados.calculos import *
from editext.analiticstring import name, sexo, string
from editext.layout import titulo
from editnum import leiaint, leiafloat, perguntar, lista_notas, media, situacao


# CREATE
def cad_boletim(name, classe, bi1, bi2, bi3, bi4, media, situação):
    try:
        inserir = f"""
        INSERT INTO boletim
        VALUES 
            (id_aluno, '{name}', {classe}, {bi1}, {bi2}, {bi3}, {bi4}, {media}, '{situação}');"""
        return inserir
    except Exception as error:
        red(f'Erro: {error}')


def cad_aluno(name, sexo, nascimento, cpf, resp1, resp2, ingresso, turma):
    try:
        inserir = f"""
        INSERT INTO alunos
        VALUES 
            (id_aluno, '{name}', '{sexo}', '{nascimento}', '{cpf}', 
            '{resp1}', '{resp2}', '{ingresso}', {turma});"""
        return inserir
    except Exception as error:
        red(f'Erro: {error}')


# READ
def acessar_info(cursor, tabela):
    try:
        acessar = f"SELECT * FROM {tabela};"
        cursor.execute(acessar)
        resultados = cursor.fetchall()

        return resultados
    except Exception as error:
        red(f'Erro: {error}')


def acumulador_ID(tabela):
    ids = [0]
    lista_ids = []
    for aluno in tabela:
        for indice, elemento in enumerate(aluno):
            if indice in ids:
                lista_ids.append(elemento)
    return lista_ids


# Recebe todas as colunas filtradas de uma tabela específica,
def acessar_info_detalhada(cursor, conexão, tabela, num):
    try:
        acessar = f"SELECT * FROM {tabela} WHERE id_aluno = {num};"
        cursor.execute(acessar)
        resultados = cursor.fetchall()
        return resultados
    except Exception as error:
        red(f'Erro: {error}')


# Mostra a tabela de alunos resultante
def tabela_alunos(resultados):
    try:
        numeros = {0: 'id_aluno', 1: 'Aluno', 2: 'Sexo', 3: 'Nascimento',
                   4: 'CPF',  5: '1º Responsável', 6: '2º Responsável',
                   7: 'Ingresso', 8: 'Turma de ingresso'}
        nome = ''
        for resultado in resultados:
            print('--' * 20)
            for indice, elemento in enumerate(resultado):
                for key, value in numeros.items():
                    if key == indice:
                        nome = value
                print(f'{nome:.<20}{elemento}')
            sleep(1)
    except Exception as error:
        red(f'Erro: {error}')


# Mostra a tabela de alunos resultante
def tabela_boletim(resultados):
    try:
        numeros = {0: 'id_aluno', 1: 'Aluno', 2: 'Turma', 3: '1º BI', 4: '2º BI',
                   5: '3º BI', 6: '4º BI', 7: 'Média', 8: 'Situação'}
        nome = ''
        for resultado in resultados:
            print('--' * 20)
            for indice, elemento in enumerate(resultado):
                for key, value in numeros.items():
                    if key == indice:
                        nome = value
                print(f'{nome:.<20}{elemento}')
            sleep(1)
    except Exception as error:
        red(f'Erro: {error}')


# UPDATE
# Comando para atualizar banco de dados
def update_alunos(tabela, alterar_coluna, nova_informação, info_controle):
    coluna_numero = ['turma_ingresso', 'Turma']
    if alterar_coluna == coluna_numero:
        atualizar = f"""UPDATE {tabela} 
                        SET {alterar_coluna} = {nova_informação}
                        WHERE id_aluno = {info_controle}"""
    elif alterar_coluna == 'Notas':
        notas = nova_informação
        b1 = notas[0]
        b2 = notas[1]
        b3 = notas[2]
        b4 = notas[3]
        med = media(notas)
        sit = situacao(notas)
        atualizar = f"""UPDATE {tabela}
                        SET bi1 = {b1}, bi2 = {b2}, bi3 = {b3}, bi4 = {b4}, media = {med}, situaçãotest = '{sit}'
                        WHERE id_aluno = {info_controle}
                        """
    else:
        atualizar = f"""UPDATE {tabela} 
                        SET {alterar_coluna} = '{nova_informação}'
                        WHERE id_aluno = {info_controle}"""
    return atualizar


def coluna_aluno(mensagem=''):
    """Essa função retorna o nome de uma coluna
    a partir da escolha de um ID predefinido:

    parameter: mensagem (parametro opcional usado
    para receber uma frase que servirá de input"""
    try:
        ids = ''
        colunas_alunos = {1: 'nome_aluno', 2: 'sexo', 3: 'nascimento',
                          4: 'cpf', 5: 'responsavel1',
                          6: 'responsavel2', 7: 'turma_ingresso'}
        titulo('Colunas disponíveis')
        for key, value in colunas_alunos.items():
            print(f'''{key:.<6}{value:20}''')
        print('-' * 30)
        while True:
            escolha = leiaint(mensagem)
            if 0 < escolha <= len(colunas_alunos):
                for key, value in colunas_alunos.items():
                    if escolha == key:
                        ids = value
                        break
            else:
                red(f'ID {escolha} é inválido!')
                continue
            break
        return ids
    except Exception as error:
        red(f'Erro: {error}')


def nova_info_aluno(coluna, txt=''):
    """Essa função retorna a nova informação para a coluna
    informada."""
    palavras = ['nome_aluno', 'sexo', 'cpf',
                'responsavel1', 'responsavel2']
    novo = ''
    if coluna in palavras:
        for palavra in palavras:
            if coluna == palavra:
                if palavra in ['nome_aluno', 'responsavel1', 'responsavel2']:
                    novo = name('Novo Nome: ')
                elif palavra == 'sexo':
                    novo = sexo('Novo Sexo: ')
                elif palavra == 'cpf':
                    novo = CPF('Novo CPF: ')
                else:
                    novo = string(txt)

    elif coluna == 'turma_ingresso':
        novo = leiaint('Nova Turma: ')

    elif coluna == 'nascimento':
        sleep(0.5)
        print('Nova data de nascimento: ')
        a = ano('Ano: ')
        m = mes('Mês: ')
        d = dia('Dia: ', m, a)
        novo = nascimento(a, m, d)

    return novo


def coluna_boletim(mensagem):
    """Essa função retorna o nome de uma coluna
        a partir da escolha de um ID predefinido:

        parameter: mensagem (parametro opcional usado
        para receber uma frase que servirá de input"""
    try:
        colunas_boletim = {1: 'Nome do aluno', 2: 'Turma', 3: 'Notas'}
        titulo('Colunas disponíveis')
        for key, value in colunas_boletim.items():
            print(f'''{key:.<6}{value:20}''')
        print('-' * 30)
        ids = ''
        while True:
            escolha = leiaint(mensagem)
            if 0 < escolha <= len(colunas_boletim):
                for key, value in colunas_boletim.items():
                    if escolha == key:
                        ids = value
                        break
            else:
                red(f'ID \"{escolha}\" é inválido!')
                continue
            break
        return ids
    except Exception as error:
        red(f'Erro: {error}')


def nova_info_boletim(coluna):
    """Essa função retorna a nova informação para a coluna
    informada."""
    try:
        palavras = ['Turma', 'Notas']
        novo = ''
        if coluna in palavras:
            for palavra in palavras:
                if coluna == palavra:
                    if palavra == 'Turma':
                        novo = leiaint('Nova Turma: ')
                    else:
                        novo = lista_notas()

        elif coluna == 'nome_aluno':
            novo = name('Nome Completo: ')
        return novo
    except Exception as error:
        red(f'Erro: {error}')


# DELETE
# Comando para deletar informações do banco de dados
def listagem(tabela):
    try:
        titulo('Alunos Cadastrados')
        lista = [0, 1]
        ids = nome = ''
        lista_ids = []
        print(f'{"ID":>6}{"Nome do Aluno":>16}')
        for aluno in tabela:
            for indice, elemento in enumerate(aluno):
                if indice in lista:
                    if indice == 0:
                        ids = elemento
                        lista_ids.append(elemento)
                    elif indice == 1:
                        nome = elemento
            print(f'{ids:>5}    {nome}')
        return lista_ids
    except Exception as Error:
        red(f'Erro: {Error}')


def deletar(tabela, bancodedados):
    try:
        lista_ids = listagem(tabela)
        opcao = perguntar(lista_ids)
        sql = f'DELETE FROM {bancodedados} WHERE id_aluno = {opcao}'
        return sql
    except Exception as Error:
        red(f'Erro: {Error}')
