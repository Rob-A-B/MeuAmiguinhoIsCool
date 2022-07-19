import os, forca, amiguinho

def limpa():
    os.system('cls')

    #JOGOS
def jogos():
    limpa()
    print('''O que deseja jogar?

[1] Forca
[2]

[0] Voltar ao início
''')
    resposta = int(input(""))
    if (resposta == 1):
        forca.jogar()
    elif (resposta == 2):
        pass
    elif (resposta == 0):
        amiguinho.menu()



if(__name__ == "__main__"):
    jogos()

