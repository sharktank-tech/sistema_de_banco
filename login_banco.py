from time import sleep

print("Olá, Escolha uma das opções \n1 - SALDO \n2 - SAQUE \n3 - DEPOSITO")
op_saldo = '1','saldo', 'SALDO', 'Saldo'
op_saque = '2','saque', 'SAQUE', 'Saque'
op_deposito = '3','deposito', 'DEPOSITO', 'Deposito'


while True:
    try:
        entrada = input("Entre com uma opção: ")
        if entrada in op_saldo:
            banco = open('banco', 'r')
            sleep(0.9)
            print('Processando...')
            sleep(1)
            print('seu saldo é:', banco.read())
            banco.close()
            break
        if entrada in op_saque:
            entrada2 = (input('Quanto deseja sacar? '))
            banco = open('banco', 'w')
            print('processando...')
            sleep(2)
            banco.write(entrada2)
            sleep(1)
            print('Saque realizado com sucesso!')
            banco.close()
            break

        if entrada in op_deposito:
            entrada3 = input('Quanto deseja depositar? ')
            banco = open('banco', 'w')
            print('Processando...')
            sleep(2)
            banco.write(entrada3)
            sleep(1)
            print('deposito realizado com sucesso!')
            banco.close()
            break

    except ValueError:
        print("Opção invalida! Digite uma opção valida")

