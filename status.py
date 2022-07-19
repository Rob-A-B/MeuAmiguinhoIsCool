from datetime import datetime

arquivo_status = "status"

def carregar_valores():
    global arquivo_status
    valores = {}
    with open(arquivo_status, "r") as f:
        conteudo = f.readlines()
        valores['moedas'] = int(conteudo[0].split(": ")[1].strip())
        valores['exp'] = int(conteudo[1].split(": ")[1].strip())
        valores['saude'] = int(conteudo[2].split(": ")[1].strip())
    return valores
    
def atualizar_valores(valores):
    global arquivo_status
    with open(arquivo_status, "w") as f:
        conteudo = [
            f"moedas: {valores['moedas']}\n",
            f"exp: {valores['exp']}\n",
            f"saude: {valores['saude']}\n",
            f"tempo: {int(datetime.now().timestamp())}"
        ]
        f.writelines(conteudo)

def puxar_valor(chave):
    with open(arquivo_status, "r") as f:
        conteudo = f.readlines()
        if (chave == "moedas"):
            return int(conteudo[0].split(": ")[1].strip())
        elif (chave == "exp"):
            return int(conteudo[1].split(": ")[1].strip())
        elif (chave == "saude"):
            return int(conteudo[2].split(": ")[1].strip())
        elif (chave == "tempo"):
            return int(conteudo[3].split(": ")[1].strip())

def atualizar_valor(chave, valor):
    valores = carregar_valores()
    valores[chave] = valor
    atualizar_valores(valores)