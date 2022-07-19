import os, amiguinho, atividades


def criar():
    amiguinho.limpa()

    assunto = input('Qual o assunto da atividade? ')
    arquivo = open(f'{assunto}.txt', 'w')

    nome_arquivo = f'{assunto}.txt'

    continua = 's'
    while(continua == 's'):
        amiguinho.limpa()

        enunciado = input("Insira o enunciado: ")
        enunciado = enunciado + '\n'
        arquivo.write(enunciado)

        a = input("Insira a alternativa A: ")
        a = a + '\n'
        arquivo.write(a)

        b = input("Insira a alternativa B: ")
        b = b + '\n'
        arquivo.write(b)

        c = input("Insira a alternativa C: ")
        c = c + '\n'
        arquivo.write(c)

        d = input("Insira a alternativa D: ")
        d = d + '\n'
        arquivo.write(d)

        correta = input("\nQual alternativa correta? ")
        correta = correta + '\n'
        arquivo.write(correta)

        print('\nDeseja criar a próxima questão? ')
        continua = input('[(s) ou (n)] ')

        if continua == 'n':
            arquivo.close()
            os.system('cls')
            print('\nA questão foi armazenada e inserida na aba de atividades!')
            atividades.lista_bio.append(assunto)
            atividades.arquivos.append(nome_arquivo)

            print('\nAperte ENTER para voltar ao início.')
            input()
            amiguinho.menu()

if(__name__ == "__main__"):
    criar()

