"""Esse módulo compõe um conjunto de funções que analisam
o dado informado pelo usuário e retorna, se verdadeiro,
para a variável que receberá o valor dessa função.

As funções desse módulo satisfazem as perguntas abaixo:
— Qual é o seu nome?
— Deseja continuar?
— Qual é o seu sexo?
"""

from editext.cores import red, yellow
import re


def name(txt):
    """Essa função analisa se o usuário escreveu um nome ou um número.
    Nomes não possuem números. Deste modo, a função apenas aceita
    nomes reais

    :parameter: 'txt' recebe a palavra informada pelo usuário"""

    try:
        while True:
            x = str(input(txt)).strip().lower()
            y = x.replace(' ', '')
            z = re.sub(r"[^ãâáõôóéêía-z]", ' ', x)
            if y.isalpha():
                nome = z.upper()
                break
            else:
                red(f'\"{x}\" é um nome inválido.')
        return nome
    except Exception as error:
        red(f'Ops! Algo deu errado: {error}')


def pergunta(txt):
    """Essa função analisa se o usuário respondeu à pergunta
    informando 'sim,' ou 'não'.

    :parameter: 'txt' recebe a resposta do usuário."""
    try:
        while True:
            questão = str(input(txt)).strip().upper()[0]
            while questão not in 'SN':
                red('Erro! Informe Sim ou Não')
                questão = str(input('Deseja continuar? ')).strip().upper()[0]
            else:
                break
        return questão
    except Exception as error:
        red(f'Erro: {error}')


def string(txt):
    """Essa função analisa se o usuário escreve algo que difira de número
    e de um espaço vazio.

    :parameter: 'txt' recebe a palavra escrita pelo usuário."""
    try:
        while True:
            texto = str(input(f'\033[1;32m{txt}\033[m')).strip().capitalize()
            while texto == '' or texto.isnumeric():
                red('Informação inválida!')
                texto = str(input(f'\033[1;32m{txt}\033[m')).strip().capitalize()
            else:
                break
        return texto
    except Exception as error:
        red(f'Erro: {error}')


def sexo(msg):
    """A função sexo retorna apenas M, para masculino,
    e F, para Feminino.
    : param msg: Recebe um texto do desenvolvendor e funciona
    como a função input"""

    try:
        while True:
            sex = string(msg).upper()[0]
            if sex in 'MF':
                break
            else:
                red(f'\"{sex}\" não é válido!')
                yellow('Dica: Masculino ou Feminino')
        return sex
    except Exception as erro:
        red(f'Erro: {erro}')
