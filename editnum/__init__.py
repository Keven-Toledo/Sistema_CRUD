"""Esse módulo é composto de funções que realizam
analises e cálculos matemáticos.

Nesse módulo encontrará:
— Verificador de número INTEIRO
— Verificador de número REAL
— Calculo de Média Aritmética
— Informa a situação do aluno
— Pergunta o número
- Listagem de notas bimestrais"""

from editext.cores import red, white
from time import sleep


def leiaint(mensagem=''):
    """Essa função verifica se o dado informado
    pelo usuário é um número inteiro. Em seguida,
    ela retorna esse número.

    :parameter: 'mensagem' recebe a frase de input"""
    try:
        numero = 0
        while True:
            x = str(input(f'\033[1;32m{mensagem}\033[m'))
            if x.isnumeric():
                numero = int(x)
                break
            else:
                red(f'\"{x}\" não é válido!')
                continue
        return numero
    except Exception as error:
        red(f'Erro: {error}')


def leiafloat(mensagem=''):
    """Essa função verifica se o dado informado
    pelo usuário é um número real. Em seguida,
    ela retorna esse número.

    :parameter: 'mensagem' recebe a frase de input"""
    try:
        while True:
            x = str(input(f'\033[1;34m{mensagem}\033[m')).strip().replace(',', '.')
            if x.isalpha() or x == '':
                red(f'\"{x}\" é Inválido!')
            else:
                num = float(x)
                break
        return num
    except Exception as error:
        red(f'Erro: {error}')


def lista_notas():
    try:
        white('Informe as Notas')
        notas = []
        sleep(0.5)
        for ciclo in range(1, 5):
            while True:
                bimestre = leiafloat(f'{ciclo}º Bimestre: ')
                if 0 <= bimestre <= 10:
                    notas.append(bimestre)
                    break
                else:
                    red('Nota incorreta!')
        return notas
    except Exception as erro:
        red(f'Erro: {erro}')


def media(lista):
    """Essa função retorna a média aritmética
    dos números informados.

    :param: 'lista' recebe a lista que contem os números"""
    try:
        média = (sum(lista)) / len(lista)
        return média
    except Exception as error:
        red(f'Erro: {error}')


def situacao(lista):
    """Essa função retorna a situação do
    aluno se aprovado ou reprovado.

    :parameter: 'lista' recebe a lista de notas
    para calcular a média"""
    try:
        media = sum(lista) / len(lista)
        if media >= 7.0:
            situação = 'Aprovado'
        else:
            situação = 'Recuperação'
        return situação
    except Exception as error:
        red(f'Erro: {error}')


def perguntar(lista_analise):
    pergunta = leiaint('Escolha um ID: ')
    while pergunta not in lista_analise:
        red(f'{pergunta} não é um ID válido!')
        pergunta = leiaint('Tente Novamente: ')
    else:
        return pergunta
