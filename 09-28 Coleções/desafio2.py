def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)
        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True
    return txt


def validar_edv(edv):
    while True:
        edv = edv.strip()
        if len(edv) != 8 or not edv.isdigit():
            print("O EDV deve conter 8 dígitos. Digite novamente:")
            edv = input('EDV............: ')
        else:
            return edv


def validar_celular(celular):
    while True:
        celular = celular.strip()
        if len(celular) != 14:
            print('O celular deve ter 14 caracteres, formato (99)99999-9999.')
        elif celular[0] != '(' or celular[3] != ')' or celular[9] != '-':
            print('O celular deve seguir o formato (99)99999-9999.')
        else:
            valido = True
            for pos, c in enumerate(celular):
                if pos in [0, 3, 9]:
                    continue
                if not c.isdigit():
                    valido = False
                    break
            if valido:
                return celular
            print('O celular deve seguir o formato (99)99999-9999.')
        celular = input('Celular............: ')


def validar_email(email):
    dominios_validos = [
        'gmail.com', 'hotmail.com', 'hotmail.com.br', 'outlook.com', 'outlook.com.br',
        'yahoo.com', 'yahoo.com.br', 'icloud.com', 'aol.com', 'proton.me', 'protonmail.com',
        'zoho.com', 'mail.com', 'gmx.com', 'gmx.net', 'bol.com.br', 'uol.com.br',
        'terra.com.br', 'globo.com', 'r7.com', 'ig.com.br', 'zipmail.com.br','unicamp.br'
    ]
    while True:
        email = email.strip()
        achou = any(email.endswith(d) for d in dominios_validos)
        if len(email) < 9:
            print("O e-mail está muito curto. Digite um válido:")
        elif '@' not in email:
            print("O e-mail deve conter o caractere '@'. Digite um válido:")
        elif email[0] == '@':
            print("O e-mail deve conter algo antes do '@'. Digite um válido:")
        elif not achou:
            print("O domínio do e-mail deve ser aceito, ex: @gmail.com. Digite um válido:")
        else:
            return email
        email = input('e-mail pessoal.....: ')



def cadastrar(agenda):
    while True:
        nome = input('\nNome...............: ').strip()
        if len(nome) <= 1 or not nome.replace(" ","").isalpha():
            print("Digite um nome válido (sem números ou caracteres especiais).")
            continue
        if nome in agenda:
            print("Pessoa já existente - Favor redigitar...")
            continue
        break

    edv = validar_edv(input('EDV...........: '))
    celular = validar_celular(input('Celular............: '))
    email = validar_email(input('e-mail pessoal.....: '))

    agenda[nome] = {"EDV": edv, "Celular": celular, "Email": email}
    print('Cadastro realizado com sucesso!')

def procurar(agenda):
    if not agenda:
        print("Nenhum contato cadastrado ainda.")
        return
    nome = input("Digite o nome a procurar: ")
    if nome in agenda:
        info = agenda[nome]
        print("\nContato encontrado:")
        print("Nome.......:", nome)
        print("EDV........:", info["EDV"])
        print("Celular....:", info["Celular"])
        print("e-mail.....:", info["Email"])
    else:
        print("Contato não encontrado.")

def listar(agenda):
    if not agenda:
        print("Nenhum contato cadastrado ainda.")
        return
    print("\nCONTATOS CADASTRADOS:\n")
    for nome, info in agenda.items():
        print("Nome.......:", nome)
        print("EDV........:", info["EDV"])
        print("Celular....:", info["Celular"])
        print("e-mail.....:", info["Email"])
        print("-" * 50)

def excluir(agenda):
    nome = input("Nome.......: ")
    if nome not in agenda:
        print("Pessoa inexistente")
        return
    info = agenda[nome]
    print("EDV........:", info["EDV"])
    print("Celular....:", info["Celular"])
    print("e-mail.....:", info["Email"])

    resposta = umTexto("Deseja realmente excluir? (S ou N) ", "Você deve digitar S ou N", ['S','s','N','n'])
    if resposta.upper() == 'S':
        del agenda[nome]
        print("Remoção realizada com sucesso!")
    else:
        print("Remoção não realizada!")

def verifica_permissao():
    while True:
        tipo = input("Qual seu usuário (Padrão ou Admin)? ").strip().upper()
        
        if tipo in ["ADMIN", "ADM"]:
            usuario = input("Digite seu usuário: ").strip()
            senha = input("Digite sua senha: ").strip()
            if senha == "1234":
                print("Bem-vindo, Admin!")
                return "ADMIN"
            else:
                print("Senha errada! Tente novamente.")
        
        elif tipo in ["PADRAO", "PADRÃO"]:
            print("Bem-vindo, usuário padrão!")
            return "PADRAO"
        
        else:
            print("Tipo de usuário inválido. Digite 'Admin' ou 'Padrão'.")

agenda = {}

tipo_usuario = verifica_permissao()

while True:
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('|                      Cadastro Pessoal                       |')
    print('|                                                             |')
    print('|  1- Cadastrar                                               |')
    print('|  2- Procurar                                                |')
    print('|  3- Listar                                                  |')
    if tipo_usuario == "ADMIN":
        print('|  4- Excluir                                                 |')
        print('|  5- Sair                                                    |')
    else:
        print('|  4- Sair                                                    |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

    opcao = input("Opção: ").strip()

    if tipo_usuario == "ADMIN":
        if opcao == "1":
            cadastrar(agenda)
        elif opcao == "2":
            procurar(agenda)
        elif opcao == "3":
            listar(agenda)
        elif opcao == "4":
            excluir(agenda)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")
    else: 
        if opcao == "1":
            print("Acesso negado! Apenas Admin pode cadastrar.")
        elif opcao == "2":
            procurar(agenda)
        elif opcao == "3":
            listar(agenda)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

 