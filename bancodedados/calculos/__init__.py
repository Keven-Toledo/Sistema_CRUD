"""Esse módulo é composto por funções que realizam cálculos
e analise algébricas para que o dado seja inserido
corretamento no banco de dados.

Ferramentas disponíveis são:
- Compilado de funções para criar data
- verificador de CPF"""

from datetime import date
from editext.cores import red


def ano(txt):
    """Essa função verifica se o ano inserido pelo
    usuário é valido através do processo de:

    - Verificar se foi escrito um número
    - Analisar se esse numero tem 4 algorimos
    - Verificar se o ano de nascimento é menor que o ano
    atual

    Após a verificação a função retorna o ano informado
    pelo usuário em formato de número inteiro."""
    try:
        y = date.today().year
        while True:
            x = str(input(txt)).strip()
            if x.isnumeric():
                if len(x) == 4:
                    numero = int(x)
                    if numero != 0:
                        if numero <= y:
                            break
                    else:
                        red(f'\"{numero}\" é maior que o ano atual.')
                else:
                    red(f'\"{x}\" ano maior que 4 algorimos.')
            else:
                red(f'\"{x}\" não é um número.')
        return numero
    except Exception as error:
        red(f'Erro: {error}')


def mes(txt):
    """Essa função verifica se o mês inserido pelo
    usuário é valido através do processo de:

    — Verificar se foi escrito um número
    — Analisar se esse numero tem até 2 algorimos
    — Verifica se o número é maior e diferente de 0
    — Verificar se o mês está contido nos meses possíveis
    (1 a 12)

    Após a verificação a função retorna o mês informado
    pelo usuário em formato de número inteiro."""
    try:
        meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        while True:
            x = str(input(txt)).strip()
            if x.isnumeric():
                if len(x) <= 2:
                    numero = int(x)
                    if 0 < numero != 0:
                        if numero in meses:
                            break
                        else:
                            red(f'Mês \"{x}\" ultrapassa o limite de 12 meses.')
                    else:
                        red(f'\"{x}\" não é um número positivo não nulo.')
                else:
                    red(f'\"{x}\" possui mais de 2 algorimos.')
            else:
                red(f'\"{x}\" não é válido.')
        return numero
    except Exception as error:
        red(f'Erro: {error}')


def ano_bissexto(ano):
    """Essa função analisa se o ano informado foi bissexto
    e retorna o último dia de feveiro. A saber:
    - 29 para anos bissextos
    - 28 para anos NÃO bissestos"""
    x = ''
    try:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            x = 29
        else:
            x = 28
        return x
    except Exception as error:
        red(f'Erro: {error}')


def ultimo_dia(mes, ano_nascimento):
    """Essa função retorna o último dia do mês de cada mês,
    além de alterar o último dia de feveiro verificando se
    o ano informado pelo usuário era bissexto ou não, após isso
    retorna dia 29 se o ano foi bissexto ou dia 28 se o ano
    não foi bissexto Alterando o dicionário de meses e dias"""
    try:
        y = ano_bissexto(ano_nascimento)
        info = {1: 31, 2: y, 3: 31, 4: 30,
                5: 31, 6: 30, 7: 31, 8: 31,
                9: 30, 10: 31, 11: 30, 12: 31}
        x = ''
        for key, values in info.items():
            if key == mes:
                x = values
                break
        return x
    except Exception as error:
        red(f'Erro: {error}')


def dia(txt, mes, ano_nascimento):
    dias = [1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15,
            16, 17, 18, 19, 20,
            21, 22, 23, 24, 25,
            26, 27, 28, 29, 30,
            31]
    try:
        while True:
            y = ultimo_dia(mes, ano_nascimento)
            x = str(input(txt)).strip()
            if x.isnumeric():
                if len(x) <= 2:
                    numero = int(x)
                    if 0 < numero != 0:
                        if numero in dias:
                            if numero <= y:
                                break
                            else:
                                red(f'O dia \"{numero}\" é maior que o último dia do mês.')
                        else:
                            red(f'O dia \"{numero}\" não existe.')
                    else:
                        red(f'\"{numero}\" não é um número positivo não nulo.')
                else:
                    red(f'\"{x}\" é maior que 2 algorismos.')
            else:
                red(f'\"{x}\" não é válido.')
        return numero
    except Exception as error:
        red(f'Erro: {error}')


def nascimento(anos, meses, dias):
    try:
        data = str(f'{anos}/{meses}/{dias}')
        return data
    except Exception as error:
        red(f'Erro: {error}')


def CPF(txt):
    """Essa função retorna o CPF, analisando se
    o usuário informou um RG válido.

    :parameter: 'txt' recebe o texto para input"""
    try:
        while True:
            y = str(input(txt))
            if y.isnumeric():
                if len(y) == 11:
                    cpf = int(y)
                    break
                else:
                    red(f'\"{y}\" quantidade de caracteres insuficiente.')
            else:
                red(f'\"{y}\" não é válido.')
        return cpf
    except Exception as error:
        red(f'Erro: {error}')
