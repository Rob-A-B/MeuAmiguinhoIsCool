import os, time, amiguinho, area_prof
os.system("cls")
pode = True

def limpa():
    os.system("cls")

def menu():
    print('''Bem-vindo ao Meu Amiguinho IsCool

[1] Cadastrar novo usuário
[2] Fazer login
[3] Sair
''')
    escolha = int(input("Digite sua opção: "))
    return escolha

def cadastrar():
    limpa()
    mat = input("Matricula ou PIN: ")
    login = input("Usuário: ")
    senha = input("Senha: ")
    return login,senha, mat

def fazer_login():
    limpa()
    login = input("Usuário: ")
    senha = input("Senha: ")
    return login,senha

def fazer_login_prof():
    limpa()
    pinf = input("PIN: ")
    login = input("Usuário: ")
    senha = input("Senha: ")
    return login,senha,pinf
    
  
def usuario(login, senha):
    usuarios =[]
    try:
        arquivo = open('usuarios.txt', 'r+', newline='')
        for linha in arquivo:
            linha = linha.strip(",")
            usuarios.append(linha.split())
        for usuario in usuarios:
            nome  = usuario[0]
            password = usuario[1]
            if login ==nome and senha == password:
                return True
    except FileNotFoundError:
        return False

def usuario_prof(login, senha, mat):
    usuarios =[]
    try:
        arquivo = open('usuarios.txt', 'r+', newline='')
        for linha in arquivo:
            linha = linha.strip(",")
            usuarios.append(linha.split())
        for usuario in usuarios:
            nome  = usuario[0]
            password = usuario[1]
            matf = usuario[2]
            if login == nome and senha == password and mat == matf:
                return True
    except FileNotFoundError:
        return False
    
def rodar():            
    while True:
        os.system('cls')
        opcao = menu()
        
        if opcao == 1:
            #Cadastrar novo usuario
            amiguinho.limpa()
            print('''[1] Aluno
[2] Professor
''')
            resposta = int(input("Escolha seu cargo: ")) 
            login, senha, mat = cadastrar()
            if login == senha:
                print("\nA senha deve ser diferente do nome do usuário!")
                senha = input("Senha:")
            user = usuario(login, senha)
            if user == True:
                print("Usuário já existe!")
                time.sleep(3)
            else:
                with open('usuarios.txt', 'a+', newline='') as arquivo:
                    arquivo.writelines(f'{login} {senha} {mat}\n')
                print("\nCadastro aprovado!")
                time.sleep(3)
                               
        elif opcao == 2:
            #Fazer o login do usúario
            amiguinho.limpa()
            print('''[1] Aluno
[2] Professor
''')
            resposta = int(input("Escolha seu cargo: "))

            if resposta == 1:
                login, senha = fazer_login()
                user = usuario(login, senha)
                if user == True:
                    print("\nLogin realizado com sucesso!")
                    time.sleep(3)
                    amiguinho.menu()
                else:
                    print("\nVocê deve ter digitado seu nome de usuário ou a senha errado \nPor favor verifique se está correto")
                    time.sleep(3)
            if resposta == 2:
                login, senha, mat = fazer_login_prof()
                user = usuario_prof(login, senha, mat)
                if user == True:
                    print("\nLogin realizado com sucesso!")
                    time.sleep(3)
                    area_prof.prof()
                else:
                    print("\nVocê deve ter digitado seu nome de usuário ou a senha errado \nPor favor verifique se está correto")
                    time.sleep(3)

                


        elif opcao == 3:
            amiguinho.limpa()
            print("Tchauzinho!")
            pode = False
            time.sleep(3)
            break

if(__name__ == "__main__" and pode == True):
    rodar()