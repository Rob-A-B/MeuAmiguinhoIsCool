import os, atividades, amiguinho
os.system('cls')

def criar(nome_arquivo):
    nome_do_arquivo = nome_arquivo
    lista = []
    enu = 0
    qa = 1
    qb = 2
    qc = 3
    qd = 4
    cor = 5

    inicio = 0
    fim = 6

    arquivo = open(nome_arquivo, "r")
    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)
    arquivo.close()

    tamanho = int(len(lista)/6)
    for c in range(tamanho):
        for i in range(inicio, fim):
            linha = lista[i]

            if i == enu:
                linha = linha.strip()
                atividades.enunciados.append(linha)
            elif i == qa:
                linha = linha.strip()
                atividades.alternativa_a.append(linha)
            elif i == qb:
                linha = linha.strip()
                atividades.alternativa_b.append(linha)
            elif i == qc:
                linha = linha.strip()
                atividades.alternativa_c.append(linha)
            elif i == qd:
                linha = linha.strip()
                atividades.alternativa_d.append(linha)
            elif i == cor:
                linha = linha.strip()
                atividades.corretas.append(linha)

        inicio += 6
        fim += 6
        enu += 6
        qa += 6
        qb += 6
        qc += 6
        qd += 6
        cor += 6
    
    atividades.biologia()

    
if(__name__ == "__main__"):
    criar('teste.txt')
    
