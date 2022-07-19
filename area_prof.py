import amiguinho, atividades, criar_questao, time, ranking_prof

def verificacao():

    while (True):
        amiguinho.limpa()
        pin = int(input('Insira seu PIN: '))
    
        if pin == 1234 or pin == 1234 or pin == 1234 or pin == 1234:
            prof()
        else:
            print('Pin incorreto!')
            time.sleep(2)


def prof():
    amiguinho.limpa()
    print('''Bem vindo, Erick Simões!

[1] Criar questões
[2] Fazer upload do txt
[3] Ranking dos alunos
''')
    resposta = int(input("O que deseja fazer? "))
    if resposta == 1:
        criar_questao.criar()

    if resposta == 2:
        amiguinho.limpa()
        input('''Insira o txt na pasta de arquivos.
        
Pressione ENTER para continuar.''')
        
        amiguinho.limpa()
        assunto = input("Qual o assunto da atividade? ")
        atividades.lista_bio.append(assunto)
        arquivo = input('Qual o nome do arquivo? ')
        atividades.arquivos.append(arquivo)
        print('\nAs questões foram inseridas na aba atividades.')
        time.sleep(3)
        amiguinho.menu()
    
    if resposta == 3:
        ranking_prof.rank()
            



if(__name__ == "__main__"):
    prof()