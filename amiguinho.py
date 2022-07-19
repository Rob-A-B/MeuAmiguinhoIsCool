import os
import jogos, estatisticas, atividades, ranking, area_prof, materiais_de_aula, login, time, status
from datetime import datetime

def limpa():
    os.system('cls')

#Variáveis globais
moedas = 0
exp = 0
saude = 56

def opcoes(local, um, dois):
    limpa()
    print(f'''{local}

[1] {um}
[2] {dois}
[3] Loja
[0] Voltar ao início   
''')

    resposta= int(input('O que deseja fazer? '))

    if (local == 'SALA DE ESTAR'):
        if (resposta == 1):
            jogos.jogos()
        elif (resposta == 2):
            #bolinha()
            pass
    elif (local == 'SALA DE ESTUDOS'):
        if (resposta == 1):
            atividades.escolha_materia()
            pass
        elif (resposta == 2):
            materiais_de_aula.materiais()
            pass
        
    elif (local == 'SALA DE AULA'):
        if (resposta == 1):
            estatisticas.barras()
            pass
        elif (resposta == 2):
            ranking.rank()
            pass

    if (resposta == 3):
        loja()
    if(resposta == 0):
        menu()


    #LOJA
def loja():

    limpa()
    print('''        LOJA
   Estamos fechados     
     no momento!

[0] Voltar ao início
''')
    resposta= int(input('O que deseja fazer? '))
    if (resposta == 1):
       pass
    elif (resposta == 2):
       pass
    elif(resposta == 0):
        menu()


    #SALA DE ESTAR
def sala_de_estar():
    um = 'Jogos'
    dois = 'Bolinha'
    opcoes('SALA DE ESTAR', um, dois)


    #SALA DE ESTUDOS   
def sala_de_estudos():
    um = 'Atividades'
    dois = 'Materias de aula'
    opcoes('SALA DE ESTUDOS', um, dois)
        

    #SALA DE AULA
def sala_de_aula():
    um = 'Estatísticas'
    dois = 'Ranking'
    opcoes('SALA DE AULA', um, dois)

def bem():
    print('''
                   ▄▄▀▀▀▀▀▀▀▀▄▄
                  █░░░░░░░░░░░░█
                 █░░░░░░░░░░░░░░█
                █▀▀██▐███▀▀██▐████
                █░░█▌████░░█▌█████
                █░░░▀▀▀▀░░░░▀▀▀▀░█
                █░░░░█░░░░░░░░█░░█
                █░░░░░█░░░░░░█░░░█
                 █░░░░░▀▀▀▀▀▀░░░█
                  █░░░░░░░░░░░░█
                   ▀▀▄▄▄▄▄▄▄▄▀▀

       O seu amiguinho está se sentindo bem.''', sep="", end="")

def mal():
    print('''
                   ▄▄▀▀▀▀▀▀▀▀▄▄
                  █░░░░░░░░░░░░█
                 █░░░░░░░░░░░░░░█
                █░░░░░░░░░░░░░░░░█
                █░░█▌████░░█▌███░█
                █░░░░░░░░░░░░░░░░█
                █░░░░░░░░░░░░░░░░█
                █░░░░░░░░░░░░░░░░█
                 █░░░░░▀▀▀▀▀▀░░░█
                  █░░░░░░░░░░░░█
                   ▀▀▄▄▄▄▄▄▄▄▀▀
   Seu amiguinho não está se sentindo muito bem.''', sep="", end="")

def faleceu():
    print('''
                            ▄▄▀▀▀▀▀▀▀▀▄▄
                   █░░░░░░░░░░░░█
                 █░░░░░░░░░░░░░░█
              █▀▀                   ▀▀               ░█
              █░░     x           ░░        x      ░█
              █░░░             ░░░░            ░█
              █░░░░░░██████░░░░█
              █░░░░░█░░░░░░█░░░█
                 █░░░█░░░░░░░░█░█
                   █░░░░░░░░░░░░█
                      ▀▀▄▄▄▄▄▄▄▄▀▀
    Infelizmente, seu amiguinho não está mais entre nós,
        peça ajuda a seu professor para revivê-lo.''', sep="", end="")                

def tempo():
    segundos_passados = 0
    try:
        tempo_passado = status.puxar_valor("tempo")
        segundos_passados = int(datetime.now().timestamp()) - tempo_passado
    except:
        pass
    status.atualizar_valor("saude", status.puxar_valor("saude") - round(0.0006 * segundos_passados))
    status.atualizar_valor("tempo", int(datetime.now().timestamp()))

    #---------------MENU--------------
def menu():
    tempo()
    limpa()
    valores = status.carregar_valores()

    if valores['saude'] >= 60:
        bem()
    elif valores['saude'] < 60 and valores['saude'] >= 10:
        mal()
    else:
        faleceu()
        exit()

    print(f'''
-----------------------------------------------------
Saúde: {valores['saude']}/100 | Experiência: {valores['exp']}->100 | Moedas: {valores['moedas']}
-----------------------------------------------------

     INÍCIO
[1] Sala de estar
[2] Sala de estudos
[3] Sala de aula
[4] Sair
''')

    resposta = int(input(""))
    if resposta == 1:
        sala_de_estar()
    elif resposta == 2:
        sala_de_estudos()
    elif resposta == 3:
        sala_de_aula()
    elif resposta == 4:
        limpa()
        print("Tchauzinho!")
        time.sleep(2)
        login.rodar()


if(__name__ == "__main__"):
    menu()
    