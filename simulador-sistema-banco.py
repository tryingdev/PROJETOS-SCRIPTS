class Conta:
    def __init__(self, saldo):
        self.saldo = saldo
        self.tipo_conta = "corrente"
        print(f"\nBem vindo a sua conta {self.tipo_conta}")
        print(f"Seu saldo atual é de {self.saldo} reais")

    def Escolha(self):
        opcao = int(input('\nDigite "1" para DEPÓSITO ou "2" para SAQUE: '))
        if opcao == 1:
            return c.Deposito()
        elif opcao == 2:
            return c.Saque()

    def Saque(self):
        if self.saldo <= 0:
            print('\nVocê não tem dinheiro suficiente para o saque!')
            return c.Escolha()
        else:
            print('\nSeu saldo atual é {}'.format(self.saldo))
            valor_saque = float(input("\nDigite o valor do saque: "))
            self.saldo = self.saldo - valor_saque
            print('\nSaldo atualizado {:.2f} R$'.format(self.saldo))
            return c.PosProcedimento()

    def Deposito(self):
        print('\nSeu saldo atual é {} reais'.format(self.saldo))
        valor_deposito = float(input("\nDigite o valor do depósito: "))
        self.saldo = self.saldo + valor_deposito
        print('\nSaldo atualizado {:.2f} R$'.format(self.saldo))
        return c.PosProcedimento()

    def PosProcedimento(self):
        pos_opcao = input('\nDeseja realizar  outro procedimento ?(S/N) ')
        if pos_opcao == 'S':
            return c.Escolha()
        else:
            print('OK, até mais')
            exit()


c = Conta(0)
c.Escolha()