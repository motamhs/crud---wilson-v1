def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt


def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: 
            inicio=meio+1
            
    return [False,inicio]

def validar_edv(edv):
    while True:
        valido = True
        if len(edv) !=8:
            print("O EDV deve conter 8 dígitos.")
            valido = False
        if valido:
            return edv
        else:
            print("O edv deve conter 8 dígitos")
            
        edv = input('EDV............: ')

def validar_celular(celular):
    while True:
        celular=celular.strip()
        if len(celular) != 14:
            print('O celular deve ter exatamente 14 caracteres, seguindo esse formato (99)99999-9999, digite um válido')
        elif celular[0] != '(' or celular[3] != ')' or celular[9] != '-':
            print('O celular deve seguir esse formato (99)99999-9999.')
        else:
            pos = 0
            valido = True
            while pos < len(celular):
                if pos == 0:
                    if celular[pos] != '(':
                        valido = False
                elif pos == 3:
                    if celular[pos] != ')':
                        valido = False
                elif pos == 9:
                    if celular[pos] != '-':
                        valido = False
                else:
                    if not (celular[pos] >= '0' and celular[pos] <= '9'):
                        valido = False
                pos += 1

            if valido:
                return celular
            else:
                print('O celular deve seguir esse formato (99)99999-9999.')
                     
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
        achou = False
        pos = 0
        while pos < len(dominios_validos) and not achou:
            if email.endswith(dominios_validos[pos]):
                achou = True
            pos += 1

        if len(email) < 9:
            print("O e-mail está muito curto. Digite um válido:")
        elif '@' not in email:
            print("O e-mail deve conter o caractere '@'. Digite um válido:")
        elif email[0] == '@':
            print("O e-mail deve conter algo antes do '@'. Digite um válido:")
        elif not achou:
            print("O domínio do e-mail deve ser um dos aceitos como por exemplo @gmail.com. Digite um válido:")
        else:
            return email

        email = input('e-mail pessoal.....: ')

        
def cadastrar (agd):
    digitouDireito=False
    while not digitouDireito:
        nome = input('\nNome...............: ')
        nome = nome.strip()   
        while nome == '' or nome.isspace() or '0' in nome or '1' in nome or '2' in nome or '3' in nome or '4' in nome or '5' in nome or '6' in nome or '7' in nome or '8' in nome or '9' in nome or '!' in nome or len(nome)<=1:
            if nome == '' or nome.isspace():
                print('O nome não pode ficar em branco ou conter apenas espaços. Por favor, digite um nome válido.')
            elif '0' in nome or '1' in nome or '2' in nome or '3' in nome or '4' in nome or '5' in nome or '6' in nome or '7' in nome or '8' in nome or '9' in nome or '!' in nome or '@' in nome or '#' in nome or '$' in nome or '%' in nome or '¨' in nome or '&' in nome or '*' in nome or '(' in nome or ')' in nome or '_' in nome or '+' in nome or '=' in nome or '[' in nome or ']' in nome or '{' in nome or '}' in nome or '/' in nome or '?' in nome or ':' in nome or '<' in nome or '>' in nome or '|' in nome:
                print("O nome não pode conter números ou caracteres especiais. Digite um nome válido.")
            elif len(nome)<=2:
                print("O nome deve ter no mínimo 2 caracteres. Digite um nome válido.")
                          
            nome = input('Nome...............: ').strip()

                
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
   
    edv=input('EDV...........: ')
    edv=validar_edv(edv)
    
    celular=input('Celular............: ') 
    celular=validar_celular(celular)
    
    email=input('e-mail pessoal.....: ')
    email = validar_email(email)
        
        
    contato=[nome,edv,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')


def procurar (agd):
    if len(agd) == 0:
        print('Nenhum contato cadastrado ainda.')
        return

    encontrado = False
    while not encontrado:
        nome = input('Digite o nome a procurar: ')
        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Contato não encontrado. Tente novamente...')
        else:
            encontrado = True
            print('\nContato encontrado:')
            print('Nome.......:', agd[posicao][0])
            print('Edv........:', agd[posicao][1])
            print('Celular....:', agd[posicao][2])
            print('e-mail.....:', agd[posicao][3])
            
def listar (agd):
    if len(agd) == 0:
        print('Nenhum contato cadastrado ainda.')
        return

    else:
        print('\nCONTATOS CADASTRADOS:\n')

    pos = 0
    while pos < len(agd):
        print('\nContato encontrado:')
        print('Nome.......:', agd[pos][0])
        print('Edv........:', agd[pos][1])
        print('Celular....:', agd[pos][2])
        print('e-mail.....:', agd[pos][3])
        print('-' * 50)
        pos += 1

def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Edv........:', agd[posicao][1])
    print('Celular....:', agd[posicao][2])
    print('e-mail.....:', agd[posicao][3])

    resposta=umTexto('Deseja realmente excluir? (S ou N) ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')



lista=[]

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('|                      Cadastro Pessoal                       |')
    print('|                                                             |')
    print('|  1- Cadastrar                                               |')
    print('|  2- Procurar                                                |')
    print('|  3- Listar                                                  |')
    print('|  4- Excluir                                                 |')
    print('|  5- Sair                                                    |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

 
    opcao = int(input("Opção: "))
    if opcao==1:
        cadastrar(lista)
    elif opcao==2:
        procurar(lista)
    elif opcao==3:
        listar(lista)
    elif opcao==4:
        excluir(lista)
    else: 
        deseja_terminar_o_programa = True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')
x = 10

print(abs(x))
x = 10

print(abs(x))
x = 10

print(abs(x))
x = 10 