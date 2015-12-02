from cash_desk import *


a = Bill(10)
b = Bill(5)
c = Bill(10)

int(a) # 10
str(a) # "A 10$ bill"
print(a) # A 10$ bill

print(a == b) # False
print(a == c) # True

money_holder = {}

money_holder[a] = 1 # We have one 10% bill
print(money_holder)

if c in money_holder:
    money_holder[c] += 1

print(money_holder)
print(money_holder) # { "A 10$ bill": 2 }

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

for bill in batch:
    print(bill)

# A 10$ bill
# A 20$ bill
# A 50$ bill
# A 100$ bill



values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total()) # 390
desk.inspect()

# We have a total of 390$ in the desk
# We have the following count of bills, sorted in ascending order:
# 10$ bills - 2
# 20$ bills - 1
# 50$ bills - 1
# 100$ bills - 3