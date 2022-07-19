import os, amiguinho, area_prof


def rank():
    amiguinho.limpa() 
    print('''
--------RANKING 3º ano A--------

1. Roberto Arruda - 390 pontos
2. Anderson Silva - 375 pontos
3. Geysa Arruda - 310 pontos
4. Diego Figueiredo - 245 pontos
5. Rainha Elizabeth - 110 pontos
''')

    print('\nAperte ENTER para voltar.')
    input()
    area_prof.prof()




if(__name__ == "__main__"):
    rank()