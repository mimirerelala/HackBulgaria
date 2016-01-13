from bankAccount import BankAccount

account = BankAccount("Rado", 0, "$")
print(account)#'Bank account for Rado with balance of 0$'
account.deposit(1000)
account.balance()#1000
print(str(account))#'Bank account for Rado with balance of 1000$'
print(int(account))#1000
print(account.history())#['Account was created', 'Deposited 1000$', 'Balance check -> 1000$', '__int__ check -> 1000$']
print(account.withdraw(500))#True
print(account.balance())#500
print(account.history())#['Account was created', 'Deposited 1000$', 'Balance check -> 1000$', '__int__ check -> 1000$', '500$ was withdrawed', 'Balance check -> 500$']
print(account.withdraw(1000))#False
print(account.balance())#500
print(account.history())#['Account was created', 'Deposited 1000$', 'Balance check -> 1000$', '__int__ check -> 1000$', '500$ was withdrawed', 'Balance check -> 500$', 'Withdraw for 1000$ failed.', 'Balance check -> 500$']
rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
print(rado.transfer_to(ivo, 500))#True
print(rado.balance())#500
print(ivo.balance())#500
print(rado.history())#['Account was created', 'Transfer to Ivo for 500BGN', 'Balance check -> 500BGN']
print(ivo.history())#['Account was created', 'Transfer from Rado for 500BGN', 'Balance check -> 500BGN']
