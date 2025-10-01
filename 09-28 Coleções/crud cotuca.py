def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Matheus Luciano - RA:25341                                  |')
    print('| Matheus Mota de Abreu - RA:25342                            |')
    print('| Pedro Isac - RA: 25567                                      |')
    print('|                                                             |')
    print('| Versão 2.0 de 22/abril/2025                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

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
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def validação_aniversario(aniversario):
    while True:
        if len(aniversario) != 5:
            print('O aniversário deve ter exatamente 5 caracteres no formato dd/mm.')
        elif aniversario[2] != '/':
            print('A barra "/" deve estar na posição 3.')
        else:
            dia = aniversario[0:2]
            mes = aniversario[3:5]

            if not (dia.isdigit() and mes.isdigit()):
                print('O dia e o mês devem ser números.')
            else:
                dia = int(dia)
                mes = int(mes)

                if not (1 <= mes <= 12):
                    print('Mês inválido. Informe um mês entre 01 e 12.')
                else:
                    dias_no_mes = {
                        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
                        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
                    }

                    if not (1 <= dia <= dias_no_mes[mes]):
                        print(f'Dia inválido para o mês {mes:02d}.')
                    else:
                        return aniversario 
        aniversario = input('Aniversário (dd/mm): ')
    
    
def validar_end(endereco):
    while True:
        endereco=endereco.strip()
        if len(endereco)<5:
            print("O endereço deve ter ao mínimo 5 caracteres, digite um endereço válido")
        
        elif '!' in endereco or '@' in endereco or '#' in endereco or '$' in endereco or '%' in endereco or '¨' in endereco or '&' in endereco or '*' in endereco or '(' in endereco or ')' in endereco or '_' in endereco or '+' in endereco or '=' in endereco or '[' in endereco or ']' in endereco or '{' in endereco or '}' in endereco or '/' in endereco or '?' in endereco or ':' in endereco or '<' in endereco or '>' in endereco or '|' in endereco:
            print("O endereço não pode conter caracteres especiais, digite um endereço válido")
        
        else:
            return endereco
            
        endereco=input('Endereço...........: ')
        
def validar_telefone(telefone):
    while True:
        telefone=telefone.strip()
        if len(telefone) == 0:
            break
        elif len(telefone) != 9:
            print('O telefone deve ser deixado em branco ou ter exatamente 9 caracteres nesse formato 9999-9999, digite um válido')
        elif telefone[4] != '-' :
            print('O telefone deve seguir esse formato 9999-9999.')
        else:
            pos = 0
            valido = True
            while pos < len(telefone):
                if pos in [4]:  
                    if telefone[pos] != '-':
                        valido = False
                else:
                    if not (telefone[pos] >= '0' and telefone[pos] <= '9'):
                        valido = False
                pos += 1

            if valido:
                return telefone
            else:
                print('O telefone deve seguir esse formato 9999-9999.')
                
        telefone=input('Telefone...........: ')
        
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
            elif len(nome)<=1:
                print("O nome deve ter no mínimo 2 caracteres. Digite um nome válido.")
                          
            nome = input('Nome...............: ').strip()

                
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario = input('Aniversário (dd/mm): ')
    aniversario = validação_aniversario(aniversario)
    
    endereco=input('Endereço...........: ')
    endereco=validar_end(endereco)
    
    
    telefone=input('Telefone...........: ') 
    telefone=validar_telefone(telefone)
    
    celular=input('Celular............: ')
    celular=validar_celular(celular)
    
    email=input('e-mail pessoal.....: ')
    email = validar_email(email)
        
        
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
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
            print('Aniversário:', agd[posicao][1])
            print('Endereço...:', agd[posicao][2])
            print('Telefone...:', agd[posicao][3])
            print('Celular....:', agd[posicao][4])
            print('e-mail.....:', agd[posicao][5])
3
def atualizar (agd):      
    if len(agd) == 0:
        print('Nenhum contato cadastrado ainda.')
        return

    encontrado = False
    while not encontrado:
        nome = input('Digite o nome do contato a ser atualizado: ')
        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Contato não encontrado. Tente novamente...')
        else:
            encontrado = True
            contato = agd[posicao]

            opcoes = ['Atualizar Aniversário',
                      'Atualizar Endereço',
                      'Atualizar Telefone',
                      'Atualizar Celular',
                      'Atualizar E-mail',
                      'Finalizar Atualizações']
            
            finalizar = False
            while not finalizar:
                print('\nContato atual:')
                print('Nome.......:', contato[0])
                print('Aniversário:', contato[1])
                print('Endereço...:', contato[2])
                print('Telefone...:', contato[3])
                print('Celular....:', contato[4])
                print('e-mail.....:', contato[5])
                
                escolha = int(opcaoEscolhida(opcoes))
                
                if escolha == 1:
                    novo = input('Novo aniversário (dd/mm): ')
                    novo = validação_aniversario(novo)
                    contato[1] = novo
                    print('Aniversário atualizado com sucesso.')
                    
                elif escolha == 2:
                    novo = input('Novo endereço: ')
                    novo = validar_end(novo)
                    contato[2] = novo
                    print('Endereço atualizado com sucesso.')
                    
                elif escolha == 3:
                    novo = input('Novo telefone: ')
                    novo = validar_telefone(novo)
                    contato[3] = novo
                    print('Telefone atualizado com sucesso.')
                    
                elif escolha == 4:
                    novo = input('Novo celular: ')
                    novo = validar_celular(novo)
                    contato[4] = novo
                    print('Celular atualizado com sucesso.')
                    
                elif escolha == 5:
                    novo = input('Novo e-mail: ')
                    novo = validar_email(novo)
                    contato[5] = novo
                    print('E-mail atualizado com sucesso.')
                    
                elif escolha == 6:
                    finalizar = True
                    print('Atualizações finalizadas.')
            
            
    

def listar (agd):
    if len(agd) == 0:
        print('Nenhum contato cadastrado ainda.')
        return

    else:
        print('\nCONTATOS CADASTRADOS:\n')

    pos = 0
    while pos < len(agd):
        print('Nome.......:', agd[pos][0])
        print('Aniversário:', agd[pos][1])
        print('Endereço...:', agd[pos][2])
        print('Telefone...:', agd[pos][3])
        print('Celular....:', agd[pos][4])
        print('e-mail.....:', agd[pos][5])
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
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(cadastrar), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: # opcao==6
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')