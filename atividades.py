import os, amiguinho, estatisticas, gerador_de_questao, time, status

enunciados = []
alternativa_a = []
alternativa_b = []
alternativa_c = []
alternativa_d = []
corretas = []
lista_bio = ['Genética', 'Zoologia']
arquivos = ['genetica.txt', 'zoologia.txt']

def limpa():
    os.system('cls')

def escolha_materia():
    limpa()
    print('''[1] Biologia
[2] História
''')
    resposta = int(input('Qual matéria deseja realizar a atividade? '))
    if(resposta == 1):
        atividades_bio()
        

def atividades_bio():
    amiguinho.limpa()
    print('Biologia:')

    for i in range(len(lista_bio)):
        print(f'[{i+1}] {lista_bio[i]}')
    
    print('\n[0] Voltar ao início')
        
    assunto = int(input('\nQual assunto? '))

    if assunto == 0:
        amiguinho.menu()  

    elif lista_bio[assunto-1] == 'Concluído!':

        print('\nEssa atividade já foi concluída.')
        print('Deseja visualizar?')
        resposta = input('[(s) ou (n)]')
        
        if resposta == 's':
            amiguinho.limpa()
            manipulador = open(arquivos[assunto-1], 'r')
            texto = manipulador.read()
            print(texto)
            print('\nAperte ENTER para voltar ao início.')
            input()
            amiguinho.menu()
        else:
            time.sleep(2)
            atividades_bio()

    else:
        lista_bio[assunto-1] = 'Concluído!'
        gerador_de_questao.criar(arquivos[assunto-1])

    

def biologia():
    pontos = 0
    acertos = 0
    
    for i in range(len(enunciados)):
        limpa()
        print(f'\n{i+1}ª) {enunciados[i]}')
        print(f'a) {alternativa_a[i]}')
        print(f'b) {alternativa_b[i]}')
        print(f'c) {alternativa_c[i]}')
        print(f'd) {alternativa_d[i]}')

        resposta = input('Digite sua resposta: ')

        if resposta == corretas[i]:
            acertos = acertos + 1
            pontos = pontos + (100/len(enunciados))
    
    
    fim_da_atividade(pontos, acertos, 'bio')



def fim_da_atividade(pontos, acertos, materia):

    amiguinho.limpa()
    
    print("\nAtividade concluída!\n")
    print(f'Pontos: {round(pontos, 2)} de 100')
    print(f'Acertos: {acertos} de {len(enunciados)}')

    enunciados.clear()
    alternativa_a.clear()
    alternativa_b.clear()
    alternativa_c.clear()
    alternativa_d.clear()
    corretas.clear()

    estatisticas.bio += 1
    status.atualizar_valor("moedas", status.puxar_valor("moedas") + 10)
    status.atualizar_valor("saude", status.puxar_valor("saude") + acertos*4)


    print(f'Você ganhou 10 moedas e {acertos * 4} pontos de saúde.')
    
    print('\nAperte ENTER para voltar ao início.')
    input()
    amiguinho.menu()



if(__name__ == "__main__"):
    escolha_materia()