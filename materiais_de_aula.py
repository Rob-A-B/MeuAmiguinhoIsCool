import webbrowser, amiguinho, time

def materiais():
    amiguinho.limpa()
    print('''       Materiais de aula (PDFs, slides, etc):

[1] Biologia (SD)
[2] Matemática
[3] Projetos 1

[0] Voltar ao início
''')
    resposta = int(input("De qual matéria deseja acessar os materiais? "))
    if resposta == 1:
        webbrowser.open('https://classroom.google.com/u/3/w/NDYwNjEyNzEyODUx/t/all')
        materiais()
    elif resposta == 2:
        webbrowser.open('https://classroom.google.com/u/3/w/NDY5NjU1NTY2NzU3/t/all')
        materiais()
    elif resposta == 3:
        webbrowser.open('https://classroom.google.com/u/3/c/NDY5MzU0NDMwOTMw')
        materiais()
    elif resposta == 0:
        amiguinho.menu()
    else:
        print("Selecione uma opção válida.")
        time.sleep(2)
        materiais()

if(__name__ == "__main__"):
    materiais()
