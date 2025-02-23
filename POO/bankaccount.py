class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
    def deposito(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Depósito exitoso. Nuevo saldo: {self.balance}")
        else:
            print("Cuenta inactiva. No se puede realizar el depósito.")
            
    def retirar(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Retiro exitoso. Nuevo saldo: {self.balance}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Cuenta inactiva. No se puede realizar el retiro.")
            
    def desactivate_account(self):
        self.is_active = False
        print("Cuenta desactivada.")
        
    def activate_account(self):
        self.is_active = True
        print("Cuenta activada.")

account = BankAccount("Daniel", 1000)
account.deposito(500)
account.retirar(200)
account.desactivate_account()
account.deposito(100)
account.activate_account()
account.deposito(100)