flag = 's'
while flag != 'n':
    escolha = input('Escolha a operação:\n(1)Soma\n(2)Subtração\n(3)Multiplicação\n(4)Divisão\n')
    primeiroNumero = int(input('Informe o primeiro numero:'))
    segundoNumero = int(input('Informe o segundo numero:'))
    print('Seu resultado:')
    
    if escolha =='1':
        print(primeiroNumero + segundoNumero)
    elif escolha == '2':
        print(primeiroNumero - segundoNumero)
    elif escolha == '3':
        print(primeiroNumero * segundoNumero)
    elif escolha == '4':
        print(primeiroNumero / segundoNumero)
    else:
        print('Escolha uma opção valida!')

    flag = input('Repetir operação?s/n\n')
