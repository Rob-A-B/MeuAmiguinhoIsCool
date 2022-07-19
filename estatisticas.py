import os, amiguinho, time, atividades
os.system('cls')

bio = 0
his = 0

def barras():
    os.system('cls')

    atv_bio = len(atividades.lista_bio)
    atv_his = 4

    bio_percent = (bio/atv_bio) *100

    print("Biologia:")
    for i in range(101):
        
        if(i<bio_percent):
            print("▣", end="", sep="")
        elif i>bio_percent and i<=100:
            print("▢", end="", sep="")
    print(f'  {round(bio_percent, 1)}%')
    print(f'{bio}/{atv_bio}')
    print()

    #his = int(input('\nQuantas atividades você fez de história? '))
    his_percent = (his/atv_his) * 100

    print("História:")
    for i in range(101):
        
        if(i<his_percent):
            print("▣", end="", sep="")
        elif i>his_percent and i<=100:
            print("▢", end="", sep="")
    print(f'  {his_percent}%')
    print(f'{his}/{atv_his}')

    print('\nAperte ENTER para voltar ao início.')
    input()
    amiguinho.menu()

if(__name__ == "__main__"):
    barras()
