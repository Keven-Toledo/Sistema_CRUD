"""Esse módulo é composto por funções que modificam
o layout das saídas de dados.

As ferramentas dispoíveis são:

- Criar uma linha com 10 caracteres a mais
que o texto informado pelo programador
- Criar um título formatado (linhas duplas)
- Criar um título formatado (linhas simples)
- Criar um menu com opções
- Mensagem de finalização do programa
"""

from editext.cores import red, white, green, yellow
from editnum import leiaint
from time import sleep


def linha(txt):
    """Essa função imprime uma linha com 10
    caracteres a mais que o texto informado
    pelo programador"""
    try:
        tam = len(txt) + 10
        print('-' * tam)
    except Exception as error:
        red(f'Erro: {error}')


def titulo(txt):
    """Essa função imprime um título formatado
    com alinhamento centralizado e duas linhas duplas"""
    try:
        tam = len(txt) + 10
        white('=' * tam)
        white(f'{txt:^{tam}}'.upper())
        white('=' * tam)
    except Exception as error:
        red(f'Erro: {error}')


def titulo2(txt):
    """Essa função imprime um título formatado
    com alinhamento centralizado e duas linhas simples"""
    try:
        tam = len(txt) + 10
        print('-' * tam)
        print(f'{txt:^{tam}}'.upper())
        print('-' * tam)
    except Exception as error:
        red(f'Erro: {error}')


def menu(cabecalho, lista):
    try:
        titulo(cabecalho)
        for numero, item in enumerate(lista):
            item_tratado = str(item).strip().upper()
            white(f'{numero + 1} - {item_tratado}')
        linha(cabecalho)
        pergunta = leiaint('Escolha uma opção: ')
        return pergunta
    except Exception as error:
        red(f'Erro: {error}')


def final(opcao):
    if opcao == 1:
        yellow('Processando...')
        sleep(0.5)
        green('Cadastrado!')
    elif opcao == 2:
        yellow('Processando...')
        sleep(0.5)
        green('Consulta Finalizada!')
    elif opcao == 3:
        yellow('Processando...')
        sleep(0.5)
        green('Atualização Finalizada!')
    elif opcao == 4:
        yellow('Processando...')
        sleep(0.5)
        green('Arquivo Deletado!')
    elif opcao == 5:
        yellow('Processando...')
        sleep(0.5)
        green('Programa Encerrado!')