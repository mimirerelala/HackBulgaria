import operator
from batchBill import BillBatch

class CashDesk:

    def __init__(self):
        self.__desk = []
        pass

    def take_money(self, money):
        if type(money) is Bill:
            self.__desk.append(money)
        else:
            for bill in money:
                self.__desk.append(bill)
        return

    def total(self):
        total = [bill._amount for bill in self.__desk]
        return "We have a total of {}$ in the desk".format(sum(total))

    def inspect(self):
        print("We have the following count of bills, sorted in ascending order:")
        inspect_result = {}
        total = [bill._amount for bill in self.__desk]
        for number in total:
            if number in inspect_result:
                inspect_result[number] += 1
            else:
                inspect_result[number] = 1

        sorted_inspect_result = sorted(inspect_result.items(), key = operator.itemgetter(0))
        for key in range(len(sorted_inspect_result)):
            (note, amount) = sorted_inspect_result[key]
            print("{}$ bills - {}".format(note, amount))
