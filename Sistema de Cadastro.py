from time import sleep

import bancodedados.CRUD as CRUD
from bancodedados.calculos import *
from bancodedados.conect import conexao, cursor, config_mysql
from editext.analiticstring import name, sexo, pergunta
from editext.layout import menu, titulo, final
from editnum import leiaint, situacao, media, lista_notas
from senc import password

while True:
    try:
        conex = config_mysql('localhost', 'root', password, 'toledo_ltda')
        intermediador = cursor(conex)

        sleep(0.5)
        opcao = menu(
            'menu principal',
            ['Novo Cadastro',
             'Acessar informações',
             'Atualizar informações',
             'Deletar informações',
             'sair do programa'])

        if opcao == 1:
            sleep(0.5)
            novo = menu('Novos cadastros', ['Novo Aluno', 'Novo Boletim'])
            try:
                if novo == 1:
                    sleep(0.5)
                    titulo('Novo Aluno')
                    nome = name('Nome Completo: ')
                    sex = sexo('Sexo: ')
                    print('Data de Nascimento: ')
                    year = ano('Ano: ')
                    month = mes('Mês: ')
                    day = dia('Dia: ', month, year)
                    nasci = nascimento(year, month, day)
                    pessoa_fisica = CPF('CPF: ')
                    responsavel1 = name('Primeiro responsável: ')
                    responsavel2 = name('Segundo responsável: ')
                    data_ingresso = date.today()
                    turma = leiaint('Turma de Ingresso: ')
                    informações = CRUD.cad_aluno(nome, sex, nasci, pessoa_fisica, responsavel1, responsavel2,
                                                 data_ingresso, turma)
                    enviar = conexao(intermediador, informações, conex)
                    final(1)
                elif novo == 2:
                    sleep(0.5)
                    titulo('Novo Boletim')
                    nome = name('Nome Completo: ')
                    turma = leiaint('Turma: ')
                    notas = lista_notas()
                    média = media(notas)
                    situação = situacao(notas)
                    informações = CRUD.cad_boletim(nome, turma, notas[0], notas[1], notas[2], notas[3], média, situação)
                    enviar = conexao(intermediador, informações, conex)
                    final(1)
                else:
                    red(f'\"{novo}\" é uma opção inválida!')
                    continue

            except Exception as erro:
                print(f'Erro: {erro}.')

        elif opcao == 2:
            sleep(0.5)
            lista = menu('informações', ['Lista de Alunos', 'Boletim'])
            try:
                if lista == 1:
                    tabela = CRUD.acessar_info(intermediador, 'alunos')

                    contador = 0
                    for elemento in tabela:
                        contador += 1
                    if contador == 0:
                        red('Erro: Não foram encontrados cadastros!')
                        sleep(1.5)

                    else:
                        tabela_completa = CRUD.tabela_alunos(tabela)
                        resposta = pergunta('Deseja continuar? ')
                        if resposta == 'S':
                            while True:
                                id_aluno = leiaint('Id do aluno: ')
                                ids_disponíveis = CRUD.acumulador_ID(tabela)
                                if id_aluno in ids_disponíveis:
                                    busca = CRUD.acessar_info_detalhada(intermediador, conex, 'alunos', id_aluno)
                                    tabela_completa = CRUD.tabela_alunos(busca)
                                    resposta = pergunta('Deseja continuar? ')
                                    if resposta == 'N':
                                        final(2)
                                        break
                                    else:
                                        continue
                                else:
                                    red(f'O ID \"{id_aluno}\" não existe!')
                elif lista == 2:
                    tabela = CRUD.acessar_info(intermediador, 'boletim')

                    contador = 0
                    for elemento in tabela:
                        contador += 1
                    if contador == 0:
                        red('Erro: Não foram encontrados cadastros!')
                        sleep(1.5)

                    else:
                        tabela_completa = CRUD.tabela_boletim(tabela)
                        resposta = pergunta('Deseja Continuar? ')
                        if resposta == 'S':
                            while True:
                                id_aluno = leiaint('Id do aluno: ')
                                ids_disponíveis = CRUD.acumulador_ID(tabela)
                                if id_aluno in ids_disponíveis:
                                    busca = CRUD.acessar_info_detalhada(intermediador, conex, 'boletim', id_aluno)
                                    tabela_completa = CRUD.tabela_boletim(busca)
                                    resposta = pergunta('Deseja continuar? ')
                                    if resposta == 'N':
                                        final(2)
                                        break
                                    else:
                                        continue
                                else:
                                    red(f'O ID \"{id_aluno}\" não existe!')
                else:
                    red(f'\"{lista}\" é uma opção inválida!')
                    continue
            except Exception as erro:
                print(f'Erro: {erro}')

        elif opcao == 3:
            alterar = menu('Atualizar', ['informações Alunos', 'informações boletim'])
            try:
                if alterar == 1:
                    tabela = CRUD.acessar_info(intermediador, 'alunos')
                    alterar_coluna = CRUD.coluna_aluno('ID da Coluna a ser alterada: ')
                    nova_informação = CRUD.nova_info_aluno(alterar_coluna, 'Nova informação: ')
                    ids_disponíveis = CRUD.acumulador_ID(tabela)
                    alunos_disponiveis = CRUD.listagem(tabela)
                    while True:
                        info_de_controle = leiaint('Id do aluno: ')
                        if info_de_controle in ids_disponíveis:
                            comando = CRUD.update_alunos('alunos', alterar_coluna, nova_informação, info_de_controle)
                            enviar = conexao(intermediador, comando, conex)
                            break
                        else:
                            red(f'O ID \"{info_de_controle}\" não existe!')
                            continue
                    final(3)

                elif alterar == 2:
                    tabela = CRUD.acessar_info(intermediador, 'boletim')
                    alterar_coluna = CRUD.coluna_boletim('ID da Coluna a ser alterada: ')
                    nova_informação = CRUD.nova_info_boletim(alterar_coluna)
                    ids_disponíveis = CRUD.acumulador_ID(tabela)
                    alunos_disponiveis = CRUD.listagem(tabela)
                    while True:
                        info_de_controle = leiaint('Id do aluno: ')
                        if info_de_controle in ids_disponíveis:
                            comando = CRUD.update_alunos('boletim', alterar_coluna, nova_informação, info_de_controle)
                            enviar = conexao(intermediador, comando, conex)
                            break
                        else:
                            red(f'O ID \"{info_de_controle}\" não existe!')
                    final(3)
                else:
                    red(f'\"{alterar}\" é uma opção inválida!')
                    continue
            except Exception as error:
                red(f'Erro: {error}')

        elif opcao == 4:
            deletar = menu('Deletar', ['Apagar Aluno', 'Deletar boletim'])
            if deletar == 1:
                try:
                    tabela = CRUD.acessar_info(intermediador, 'alunos')

                    contador = 0
                    for elemento in tabela:
                        contador += 1
                    if contador == 0:
                        red('Erro: Não foram encontrados cadastros!')
                        sleep(1.5)

                    else:
                        comando = CRUD.deletar(tabela, 'alunos')
                        enviar = conexao(intermediador, comando, conex)
                        final(4)
                except Exception as error:
                    red(f'Erro: {error}')
            elif deletar == 2:
                try:
                    tabela = CRUD.acessar_info(intermediador, 'boletim')

                    contador = 0
                    for elemento in tabela:
                        contador += 1
                    if contador == 0:
                        red('Erro: Não foram encontrados cadastros!')
                        sleep(1.5)
                    else:
                        comando = CRUD.deletar(tabela, 'boletim')
                        enviar = conexao(intermediador, comando, conex)
                        final(4)
                except Exception as error:
                    red(f'Erro: {error}')
            else:
                red(f'\"{deletar}\" é uma opção inválida!')
                continue

        elif opcao == 5:
            final(5)
            break

        else:
            red(f'ERRO: \"{opcao}\" é uma opção inválida!')
            continue
    except Exception as error:
        red(f'Erro: {error}')
