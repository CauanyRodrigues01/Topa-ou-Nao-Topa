import os
import time
from random import randint
import funções

funções.capa()

while True:
    opcao = funções.menu()
    os.system('cls')
    if opcao == '1':
        funções.dici = dict()  # Dicionário vazio para organizar as maletas
        funções.lista_valores = [10, 25, 50, 75, 100, 500, 1000, 10000, 25000, 50000, 500000, 1000000]  # valores das maletas
        funções.lista_vazia = []  # lista para descartar os valores já sorteados
        funções.imprimir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        funções.lista1 = [10, 25, 50, 75, 100, 500]
        funções.lista2 = [1000, 10000, 25000, 50000, 500000, 1000000]

        # INÍCIO DO SORTEIO DOS VALORES NAS MALETAS
        funções.sorteio()
        #COMEÇO DO JOGO
        contador = 1
        m = 0
        while m == 0:
            funções.uma_maleta()
            reserva = input('Escolha sua maleta para reserva: ')
            if int(reserva) > 0 and int(reserva) < 13:
                funções.maletas(int(reserva))
                dinheiro = funções.dici["maleta" + reserva]
                if dinheiro in funções.lista1:
                    funções.lista1.remove(dinheiro)
                elif dinheiro in funções.lista2:
                    funções.lista2.remove(dinheiro)
                m = 1
            else:
                print(f'{"---MALETA INEXISTENTE---":^113}')

        while True:
            # eliminar 4 primeiras maletas
            money = funções.escolha(7)

            res = str(input('>>>')).upper()
            if res == '2':
                # eliminar 3 maletas
                funções.uma_maleta()
                money = funções.escolha(4)

                res = str(input('>>>')).upper()
                if res == '2':
                    # eliminar 3 maletas
                    funções.uma_maleta()
                    money = funções.escolha(2)

                    res = str(input('>>>')).upper()
                    if res == '2':
                        # eliminar 1 maletas
                        funções.uma_maleta()
                        money = funções.escolha(1)

                        # DECISÃO FINAL
                        res = str(input('>>>')).upper()
                        if res == '2':
                            funções.escolhaf()
                            decisaof = (input('>>> '))
                            if decisaof == '2':
                                funções.parabens(dinheiro)
                                funções.premio_perdido(dinheiro,x='final')
                                break
                            elif decisaof == '1':
                                if len(funções.lista1) > len(funções.lista2):
                                    money=funções.lista1[0]
                                    funções.parabens(money)
                                elif len(funções.lista1) < len(funções.lista2):
                                    money=funções.lista2[0]
                                    funções.parabens(money)
                                funções.premio_perdido(dinheiro,x='final')
                                break

                        elif res == '1':
                            funções.parabens(money)
                            funções.premio_perdido(dinheiro,x='banqueiro')
                            break
                        elif res not in '12':
                            print('\033[93mInvalido! digite 1 ou 2')
                            time.sleep(2)
                    elif res == '1':
                        funções.parabens(money)
                        funções.premio_perdido(dinheiro,x='banqueiro')
                        break
                    elif res not in '12':
                        print('\033[93mInvalido! digite 1 ou 2')
                        time.sleep(2)
                elif res == '1':
                    funções.parabens(money)
                    funções.premio_perdido(dinheiro,x='banqueiro')
                    break
                elif res not in '12':
                    print('\033[93mInvalido! digite 1 ou 2')
                    time.sleep(2)
            elif res == '1':
                funções.parabens(money)
                funções.premio_perdido(dinheiro,x='banqueiro')
                break
            else:
                print('\033[93mInvalido! digite 1 ou 2')
                time.sleep(2)
    elif opcao == '2':
        funções.explicação()

    elif opcao == '3':
        funções.creditos()
    elif opcao == '4':
        print(f'\033[93m{" "*50}OBRIGADO POR JOGAR', end='')
        ret = '...'
        for y in ret:
            time.sleep(0.7)
            print(y, end='', flush= True)
        break
    else:
        print('\033[93mOPÇÃO INVÁLIDA, POR FAVOR DIGITE APENAS NÚMEROS')
        time.sleep(2)
