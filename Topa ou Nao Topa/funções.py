from random import randint
import os
import time

dici = dict()  # Dicionário vazio para organizar as maletas
lista_valores = [10, 25, 50, 75, 100, 500, 1000, 10000, 25000, 50000, 500000, 1000000]  # valores das maletas
lista_vazia = []  # lista para descartar os valores já sorteados
imprimir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1 = [10, 25, 50,75, 100, 500]
lista2 = [1000, 10000, 25000, 50000, 500000, 1000000]
lista_final = []

def capa():
    #função que cria um arquivo com a interface da capa do jogo
    # (encoding='utf-8') É o código para avisar ao python que será utilizado caracteres da tebela ASCII
    capa=open('capa.txt','w',encoding='utf-8')
    #(capa.write) #comando para escrever no arquivo
    capa.write('''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║                       _____                                                                          ║      
        ║                      |_   _|   ___    _ __     __ _      ___    _   _                                ║
        ║                        | |    / _ \  | '_ \   / _` |    / _ \  | | | |                               ║
        ║                        | |   | (_) | | |_) | | (_| |     (_) | | |_| |                               ║
        ║                        |_|    \___/  | .__/   \__,_|    \___/   \__,_|                               ║
        ║                                      |_|                                                             ║
        ║                        _   _                     _____                           __                  ║
        ║                       | \ | |   __ _    ___     |_   _|   ___    _ __     __ _  |__ \                ║
        ║                       |  \| |  / _` |  / _ \      | |    / _ \  | '_ \   / _` |    ) |               ║
        ║                       | |\  | | (_| | | (_) |     | |   | (_) | | |_) | | (_| |   / /                ║
        ║                       |_| \_|  \__,_|  \___/      |_|    \___/  | .__/   \__,_|  |_|                 ║
        ║                                                                 |_|              (_)                 ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
    capa.close()

    arq=open('capa.txt','r',encoding='utf-8')
    #(arq.read()) comando para ler o arquivo
    #print(arq.read())
    for linha in arq:
        print(linha, end='')
        time.sleep(0.1)
    print()
    print(f"{'PRESSIONE ENTER PARA COMEÇAR':^113}")
    fechar = input()
    arq.close()

def creditos():
    #função que cria um arquivo com a interface da capa do jogo
    # (encoding='utf-8') É o código para avisar ao python que será utilizado caracteres da tebela ASCII
    creditos=open('creditos.txt','w',encoding='utf-8')
    creditos.write('''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                               ___                  _   _   _                                         ║
        ║                              / __|  _ _   ___   __| | (_) | |_   ___   ___                           ║
        ║                             | (__  | '_| / -_) / _` | | | |  _| / _ \ (_-<                           ║
        ║                              \___| |_|   \___| \__,_| |_|  \__| \___/ /__/                           ║
        ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
        ║    Alunos:                                                                                           ║
        ║       CAUANY NUNES RODRIGUES                                                                         ║
        ║       MARIA EDUARDA VIANA CORDEIROS DOS SANTOS                                                       ║
        ║       PEDRO LÔBO NASCIMENTO                                                                          ║
        ║                                                                                                      ║
        ║    Orientador:                                                                                       ║
        ║       MARCOS VINICIUS CANTIDIANO MARQUES DE ANDRADE                                                  ║
        ║       MIRNA CARELLI OLIVEIRA MAIA                                                                    ║
        ║       ELAINE CRISTINA JUVINO DE ARAUJO                                                               ║
        ║                                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
    creditos.close()

    arq=open('creditos.txt','r',encoding='utf-8')
    print(arq.read())
    print(f"{'PRESSIONE ENTER PARA VOLTAR AO MENU':^104}")
    fechar = input()
    arq.close()

def explicação():
    #função que cria um arquivo com a interface da capa do jogo
    # (encoding='utf-8') É o código para avisar ao python que será utilizado caracteres da tebela ASCII
    explicação=open('explicação.txt','w',encoding='utf-8')
    explicação.write(f'''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                    ___   _  _   ___   _____   ___   _   _    ___    ___    ___   _                   ║
        ║                   |_ _| | \| | / __| |_   _| | _ \ | | | |  / __|  / _ \  | __| / __|                ║
        ║                    | |  | .` | \__ \   | |   |   / | |_| | | (__  | (_) | | _|  \__ \                ║
        ║                   |___| |_|\_| |___/   |_|   |_|_\  \___/   \___|  \___/  |___| |___/                ║
        ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
        ║   O Jogo funciona da seguinte forma:                                                                 ║
        ║       O jogador deverá escolher uma maleta misteriosa no começo do jogo, a qual não será revelada,   ║
        ║   esta maleta conterá o valor que ele receberá ao fim do jogo caso recuse as ofertas do banqueiro.   ║
        ║   A partir disso, ele deverá abrir maletas, que contém os valores que o jogador está deixando de     ║
        ║   ganhar, após 4 maletas, o banqueiro fará a primeira oferta baseada nos valores que ainda restarem  ║
        ║   em jogo, cabe ao jogador aceitar ou ceder à tentadora oferta. Em caso de recusa, o jogo prossegue  ║
        ║   com voltas periódicas do banqueiro com mais ofertas que podem aumentar ou diminuir de acordo       ║
        ║   com a situação do jogo.                                                                            ║
        ║       Quando restarem apenas 2 maletas em jogo, contando com a escolhida pelo jogador, o banqueiro   ║
        ║   fará a última oferta, caso recuse o jogador terá direito de escolher a maleta misteriosa, ou a     ║
        ║   última que sobrar sobre a mesa. Você Topa ou Não Topa?                                             ║
        ║                                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
    explicação.close()

    arq=open('explicação.txt','r',encoding='utf-8')
    print(arq.read())
    print(f"{'PRESSIONE ENTER PARA VOLTAR AO MENU':^104}")
    fechar = input()
    arq.close()

def maletas(escolha):
    os.system('cls')
    a = escolha
    if len(lista1)+len(lista2) == 12:
        for p in range(len(imprimir)):
            if imprimir[p] == a:
                imprimir[p] = '###'
    else:
        for i in range(len(imprimir)):
            if imprimir[i] == a:
                lista_final.append(imprimir[i])
                imprimir[i] = dici['maleta' + str(a)]
    print(f"""\033[93m
        {'-' * 104}
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║          _               _               _               _               _               _           ║
        ║    _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _     ║
        ║   |             | |             | |             | |             | |             | |             |    ║
        ║   |{imprimir[0]:^13}| |{imprimir[1]:^13}| |{imprimir[2]:^13}| |{imprimir[3]:^13}| |{imprimir[4]:^13}| |{imprimir[5]:^13}|    ║
        ║   |             | |             | |             | |             | |             | |             |    ║
        ║   |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _|    ║
        ║                                                                                                      ║    
        ║          _               _               _               _               _               _           ║
        ║    _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _     ║
        ║   |             | |             | |             | |             | |             | |             |    ║
        ║   |{imprimir[6]:^13}| |{imprimir[7]:^13}| |{imprimir[8]:^13}| |{imprimir[9]:^13}| |{imprimir[10]:^13}| |{imprimir[11]:^13}|    ║
        ║   |             | |             | |             | |             | |             | |             |    ║
        ║   |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _|    ║
        ║                                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝""")
    print(f"{'Valores restantes: ':>8}{lista_valores}")

def uma_maleta():
    os.system('cls')
    print(f"""\033[93m
        {'-' * 104} 
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║          _               _               _               _               _               _           ║
        ║    _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _     ║
        ║   |             | |             | |             | |             | |             | |             |    ║
        ║   |{imprimir[0]:^13}| |{imprimir[1]:^13}| |{imprimir[2]:^13}| |{imprimir[3]:^13}| |{imprimir[4]:^13}| |{imprimir[5]:^13}|    ║
        ║   |             | |             | |             | |             | |             | |             |    ║
        ║   |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _|    ║
        ║                                                                                                      ║    
        ║          _               _               _               _               _               _           ║
        ║    _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _   _ _ _|_|_ _ _     ║
        ║   |             | |             | |             | |             | |             | |             |    ║
        ║   |{imprimir[6]:^13}| |{imprimir[7]:^13}| |{imprimir[8]:^13}| |{imprimir[9]:^13}| |{imprimir[10]:^13}| |{imprimir[11]:^13}|    ║
        ║   |             | |             | |             | |             | |             | |             |    ║
        ║   |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _| |_ _ _ _ _ _ _|    ║
        ║                                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝""")
    print(f"{'Valores restantes: ':>8}{lista_valores}")

def banqueiro(lista1, lista2):
    os.system('cls')
    sorteio1 = ['650', '950', '2.200', '6.400', '11.000']
    sorteio2 = ['0', '55', '100', '300', '550']
    sorteio3 = ['15.000', '25.000', '40.000', '90.000', '150.000']
    num = randint(0, 4)
    if len(lista1) == len(lista2):
        quantia = sorteio1[num]
    elif len(lista2) > len(lista1):
        quantia = sorteio2[num]
    elif len(lista1) > len(lista2):
        quantia = sorteio3[num]
    #Manipulação de string
    x=f'''
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║                                          topa ou não topa?                                           ║
        ║                                                                                                      ║
        ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
        ║                                      AcEiTa PaRaR o JoGo PoR                                         ║
        ║                                                                                                      ║
        ║══════════════════════════════════════════  {quantia:^7} REAIS? ═══════════════════════════════════════════║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║           _          ___   ___   __  __               ___        _  _     _      ___                 ║
        ║          / |        / __| |_ _| |  \/  |             |_  )      | \| |   /_\    / _ \                ║
        ║          | |   __   \__ \  | |  | |\/| |              / /   __  | .` |  / _ \  | (_) |               ║
        ║          |_|        |___/ |___| |_|  |_|             /___|      |_|\_| /_/ \_\  \___/                ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝'''
    print(x.upper())
    print(f"{'Valores restantes: ':>42}{lista_valores}")
    return (quantia)

def menu():
    os.system('cls')
    print(f'''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                   __    __    ___   __      _     __      _     __      ___    ___                   ║
        ║                  | _ \ | _ \ | __| | _ \   / \   | _ \   / \   |   \   / _ \  |__ \                  ║
        ║                  |  _/ |   / | _|  |  _/  / _ \  |   /  / _ \  | |) | | (_) |   /_/                  ║
        ║                  |_|   |_|_\ |___| |_|   /_/ \_\ |_|_\ /_/ \_\ |___/   \___/   (_)                   ║ 
        ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
        ║                                                                                                      ║
        ║                      ──────────────────                      ──────────────────                      ║
        ║                         1 - INICIAR                            2 - EXPLICAÇÃO                        ║
        ║                      ──────────────────                      ──────────────────                      ║
        ║                                                                                                      ║
        ║                      ──────────────────                      ──────────────────                      ║
        ║                         3 - CRÉDITOS                              4 - SAIR                           ║
        ║                      ──────────────────                      ──────────────────                      ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
    print(f'{"Opção escolhida: ":^30}')
    opcao = (input('>>>\033[m'))
    return (opcao)

def escolha(n):
    while len(lista1) + len(lista2) > n:
        x = input('Descarte uma maleta: ')
        maletas(int(x))
        if int(x) < 1 or int(x) > 12:
            print('---maleta inexistente---')
        else:
            x = dici["maleta" + x]
            if x in lista1:
                lista1.remove(x)
                lista_valores.remove(x)
            elif x in lista2:
                lista2.remove(x)
                lista_valores.remove(x)
            else:
                print('---maleta já descartada---')
    #time.sleep(2)
    valor = banqueiro(lista1, lista2)
    return (valor)

def sorteio():
    b=0
    a = 'maleta'
    # loop para sorteio
    while len(dici) < 12:  # PROPOSTA DE COLOCAR NUMA FUNÇÃO PARA PREENCHER MALETAS. JOGA NO OUTRO ARQUIVO E IMPORTA
        var = lista_valores[randint(0, 11)]
        #manipulação de string
        if var not in lista_vazia:
            b += 1
            c = str(b)
            dici[a + c] = var
            lista_vazia.append(var)

def parabens(money):
    os.system('cls')
    #manipulação de string
    var='VOCÊGANHOU'
    print(f'''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                     ___     _     ___     _     ___   ___   _  _   ___     _   _   _                 ║
        ║                    | _ \   /_\   | _ \   /_\   | _ ) | __| | \| | / __|   | | | | | |                ║
        ║                    |  _/  / _ \  |   /  / _ \  | _ \ | _|  | .` | \__ \   |_| |_| |_|                ║
        ║                    |_|   /_/ \_\ |_|_\ /_/ \_\ |___/ |___| |_|\_| |___/   (_) (_) (_)                ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                                     {var[:4]} {var[4:]} {money:^7} REAIS                                        ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')

def escolhaf():
    os.system('cls')
    for r in range(len(imprimir)):
        imprimir[r] = str(imprimir[r])
    for e in range(len(imprimir)):
        if len(imprimir[e])<=2 and imprimir[e] not in lista_final:
            finalmente = imprimir[e]
    for g in range(len(imprimir)):
        if imprimir[g] == '###':
            finalmente1 = imprimir[g]
    print(f'''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║                                            DECISÃO FINAL                                             ║
        ║                                                                                                      ║ 
        ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
        ║                                     VOCÊ ESCOLHE DESCARTAR...                                        ║
        ║                                                                                                      ║
        ║                      {'1 - PARA':^13}                         {'2 - PARA':^13}                             ║
        ║                                                                                                      ║
        ║                            _                                     _                                   ║
        ║                      _ _ _|_|_ _ _                         _ _ _|_|_ _ _                             ║
        ║                     |             |                       |             |                            ║
        ║                     |{finalmente1:^13}|                       |{finalmente:^13}|                            ║
        ║                     |             |                       |             |                            ║
        ║                     |_ _ _ _ _ _ _|                       |_ _ _ _ _ _ _|                            ║
        ║                   ───────────────────                   ───────────────────                          ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')

def premio_perdido(reserva,x):
    if x == 'banqueiro':
        print(f'''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║                                    OLHE O QUE VOCÊ PERDEU!                                           ║
        ║                                                                                                      ║
        ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                                          M A L E T A                                                 ║
        ║                                         R E S E R V A                                                ║
        ║                                               _                                                      ║
        ║                                         _ _ _|_|_ _ _                                                ║
        ║                                        |             |                                               ║
        ║                                        |{reserva:^13}|                                               ║
        ║                                        |             |                                               ║
        ║                                        |_ _ _ _ _ _ _|                                               ║
        ║                                      ──────────────────                                              ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
    elif x == 'final':
        if len(lista1) > len(lista2):
            print(f'''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║                                    OLHE O QUE VOCÊ PERDEU!                                           ║
        ║                                                                                                      ║ 
        ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                       M A L E T A                           M A L E T A                              ║
        ║                      R E S E R V A                        R E S T A N T E                            ║
        ║                            _                                     _                                   ║
        ║                      _ _ _|_|_ _ _                         _ _ _|_|_ _ _                             ║
        ║                     |             |                       |             |                            ║
        ║                     |{reserva:^13}|                       |{lista1[0]:^13}|                            ║
        ║                     |             |                       |             |                            ║
        ║                     |_ _ _ _ _ _ _|                       |_ _ _ _ _ _ _|                            ║
        ║                   ──────────────────                     ──────────────────                          ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
        elif len(lista1) < len(lista2):
            print(f'''\033[93m
        ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                                      ║
        ║                                    OLHE O QUE VOCÊ PERDEU!                                           ║
        ║                                                                                                      ║ 
        ║¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯║
        ║                                                                                                      ║
        ║                                                                                                      ║
        ║                        M A L E T A                           M A L E T A                             ║
        ║                       R E S E R V A                        R E S T A N T E                           ║
        ║                            _                                     _                                   ║
        ║                      _ _ _|_|_ _ _                         _ _ _|_|_ _ _                             ║
        ║                     |             |                       |             |                            ║
        ║                     |{reserva:^13}|                       |{lista2[0]:^13}|                            ║
        ║                     |             |                       |             |                            ║
        ║                     |_ _ _ _ _ _ _|                       |_ _ _ _ _ _ _|                            ║
        ║                   ──────────────────                     ──────────────────                          ║
        ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝''')
    fechar = input("PRESSIONE ENTER PARA VOLTAR AO MENU")
