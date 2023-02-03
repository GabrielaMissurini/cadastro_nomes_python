from funcoes import *
from os.path import isfile
from time import sleep
import datetime
import pandas as pd
from datetime import date
import numpy as np
from tabulate import tabulate


#descobrindo se ja existe um arquivo de cadastro, se não existir, criar:
if isfile('cadastro_usuarios.txt') is False:
    with open('cadastro_usuarios.txt', 'w', encoding='utf-8') as arquivo:
        titulo = ['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF',  'Data de nascimento']
        for item in titulo:
            arquivo.write(f'{item},')
        arquivo.write('Idade')



#Criando a barra de início do programa
print('='*155)
print('\033[1;36mINÍCIO PROGRAMA\033[m'.center(155))
print('='*155)

#Criando a barra do menu do programa
print('\033[1;33m-'*155)
print('MENU'.center(145))
print('-\033[m'*155)

lista_menu = ['Exibir lista de usuários', 'Buscar usuário', 'Cadastrar usuário',
              'Remover usuário', 'Atualizar dados usuário', 'Estatísticas do sistema', 'Sair']
for i in range(len(lista_menu)):
           print((f'\033[1;33m[{i+1}] {lista_menu[i]}\033[m').center(130+len(lista_menu[i])))
print('\033[1;33m-\033[m'*155)


while True:
    try:
        n = int(input('Informe sua opção: '))
    except:
        print(f'\033[1;31mOpção inválida!\033[m Responda um número entre {lista_menu[0]} e {lista_menu[-1]}.')
    else:
    #Criando as opções
        if n == 1:
            print('.')
            print('.')
            tabela = leitura_arquivo('cadastro_usuarios.txt')
            print(tabulate(tabela, headers = ['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF',  'Data de nascimento','Idade'], tablefmt="mixed_grid"))
            print('.')
            print('.')

        elif n == 2:
            tabela = leitura_arquivo('cadastro_usuarios.txt')
            buscar_usuario = input('Para buscar um usuário especifico você deve ter em mãos o cpf (escreva da seguite forma XXX.XXX.XXX-XX): ').strip()
            cont = 0
            for usuario in tabela:
                if usuario[4] == buscar_usuario:
                    cont = 1
                    print(f'''Nome: {usuario[0]}  
Gênero: {usuario[1]}
E-mail: {usuario[2]}
Telefone: {usuario[3]}
CPF: {usuario[4]}
Data de nascimento: {usuario[5]}
Idade : {usuario[6]}.''')

            if cont < 1:
                print(f'\033[1;31mNão há nenhum usuário no cadastro com o CPF {buscar_usuario} ou você escreveu errado, lembre-se de não deixar de colacar pontos e traço.\033[m')

        elif n == 3:
            leitura_arquivo('cadastro_usuarios.txt')
            nome = input('Nome: ').strip().capitalize()
            genero = input('Gênero [M/F/Outro]: ').strip().upper()[0]
            email = input('E-mail: ').strip().lower()
            telefone = input('Telefone [(DDD) XXXXX-XXXX]: ').strip()
            cpf = input('CPF [XXX.XXX.XXX-XX]: ').strip()
            data_de_nascimento = input('Data de nascimento [dd/mm/aaaa]: ').strip()
            idade = input('Digite sua idade: ')
            novo_usuario = [nome, genero, email, telefone, cpf, str(data_de_nascimento), int(idade)]
            print('ANTES DA ATUALIZAÇÃO')
            print(tabulate(tabela, headers=['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento', 'Idade'],
                         tablefmt="mixed_grid"))
            print('DEPOIS DA ATUALIZAÇÃO')
            cadastrar_usuario(novo_usuario)
            tabela.append(novo_usuario)
            print(tabulate(tabela, headers=['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento', 'Idade'],
                         tablefmt="mixed_grid"))
            print(f'\033[1;32mCadastro do usuário realizado com sucesso!\033[m')

        elif n == 4:
            tabela = leitura_arquivo('cadastro_usuarios.txt')
            cpf = input('Escreva o CPF do usuário que você quer remover [XXX.XXX.XXX-XX]: ').strip()
            try:
                for i in tabela:
                    if cpf in i:
                        posicao = tabela.index(i)
                remover_usuario(posicao)
            except:
                print(f'\033[1;31mNão há nenhum usuário no cadastro com o CPF {cpf} ou você escreveu errado, lembre-se de não deixar de colacar pontos e traço.\033[m')
            else:
                print(tabulate([tabela[posicao]], headers=['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento','Idade'],
                                       tablefmt="mixed_grid"))
                print('A remoção do usuário acima foi realizado com sucesso!!!')

        elif n == 5:
            tabela = leitura_arquivo('cadastro_usuarios.txt')
            print('Selecione a informação que você deseja atualizar, deve ser feita uma informação por vez:')
            lista_atualiza = ['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento', 'Idade']
            for i in range(len(lista_atualiza)):
                print((f'[{i + 1}] {lista_atualiza[i]}'))

            num = int(input('Escolha uma opção: '))
            print(f'Voce escolheu a opção {lista_atualiza[num - 1]}, então coloque abaixo a informação alterada: ')
            valor_alterado = input(f'Novo(a) {lista_atualiza[num - 1]}: ')
            cpf = input(
                'Escreva o CPF da pessoa que você deseja alterar as informações, se for CPF que você quer alterar, escreva o CPF antigo:  ').strip()

            for i in tabela:
                if cpf == i[4]:
                    posicao = int(tabela.index(i))
            print('Registro do usuário antes da atualização: ')
            print(tabulate([tabela[posicao]],
                           headers=['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento', 'Idade'],
                           tablefmt="mixed_grid"))
            try:
                atualizando(posicao, valor_alterado, num)

            except:
                print('Este usuário não existe ou você digitou alguma informação errada!!!')
            else:
                tabela = leitura_arquivo('cadastro_usuarios.txt')
                print('Registro do usuário depois da atualização: ')
                print(tabulate([tabela[posicao]],
                               headers=['Nome', 'Gênero', 'E-mail', 'Telefone', 'CPF', 'Data de nascimento', 'Idade'],
                               tablefmt="mixed_grid"))
                print('Atualização foi realizada com sucesso!!!')

        elif n == 6:
            leitura_arquivo('cadastro_usuarios.txt')
            cont, cont_f, cont_18, cont_35, cont_65, cont_100 = 0, 0, 0, 0, 0, 0
            for i in tabela:
                try:
                    cont += 1
                    if i[1] == 'F':
                        cont_f += 1
                    if int(i[-1]) < 18:
                        cont_18 += 1
                    elif int(i[-1]) < 35:
                        cont_35 += 1
                    elif int(i[-1]) < 65:
                        cont_65 += 1
                    else:
                        cont_100 += 1
                except:
                    pass

            print(f'''
                A quantidade de usuários cadastrados é {cont}.
                A quantidade de usuários cadastrados do gênero feminino é {cont_f}.
                A quantidade de usuários cadastrados do gênero masculino é {cont - cont_f}.
                A quantidade de usuários cadastrados menores de 18 anos é {cont_18}.
                A quantidade de usuários cadastrados com idade entre 18 e 35 anos é {cont_35}.
                A quantidade de usuários cadastrados com idade entre 35 e 65 anos é {cont_65}.
                A quantidade de usuários cadastrados maiores de 65 anos é {cont_100}''')

        else:
            break
        sleep(1)


print('='*155)
print('\033[1;36mPROGRAMA FINALIZADO\033[m'.center(155))
print('='*155)