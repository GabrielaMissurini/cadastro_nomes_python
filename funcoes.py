#FUNÇÃO PARA LER ARQUIVO
def leitura_arquivo(nome_arquivo):
    tabela = []
    with open('cadastro_usuarios.txt', 'r', encoding='utf-8') as arquivo_leitura:
        lista_todos_usuarios = arquivo_leitura.readlines()
        for linha in range(1, len(lista_todos_usuarios)):
            tabela.append(lista_todos_usuarios[linha].rstrip(',\n').split(','))
    return tabela


#FUNÇÃO PARA CADASTRAR USUÁRIO
def cadastrar_usuario(novo):
    with open('cadastro_usuarios.txt', 'a', encoding='utf-8') as arquivo_escrita:
        arquivo_escrita.write('\n')
        for dado in novo:
            arquivo_escrita.write(f'{dado},')


#FUNÇÃO REMOVE USUÁRIO
def remover_usuario(posicao):
    with open('cadastro_usuarios.txt', 'r') as arquivo_remove:
        lines = arquivo_remove.readlines()
        del lines[posicao + 1]

    with open('cadastro_usuarios.txt', 'w') as arquivo_remove:
        for i in range(len(lines)):
            arquivo_remove.write(lines[i])


#FUNÇÃO ATUALIZA USUÁRIO
def atualizando(index, valor_alterado, num):
    with open('cadastro_usuarios.txt', 'r') as arquivo_atualiza:
        lines = arquivo_atualiza.readlines()
        linha = lines[index + 1].split(',')
        linha[num - 1] = valor_alterado
        juntar = ''
        for i in range(0,len(linha)-1):
            juntar += linha[i] + ','
        juntar = juntar + '\n'
        lines[index + 1] = juntar
        lines
    with open('cadastro_usuarios.txt', 'w') as arquivo_remove:
        for i in range(len(lines)):
            arquivo_remove.write(lines[i])