from bill import Bill
class BillBatch():

    def __init__(self, bill_list):
        self._bills = bill_list
        self._total = 0
        for bill in bill_list:
            self._total += bill._amount

    def __len__(self):
        return len(self._bills)

    def total(self):
        return self._total

    def __getitem__(self, index):
        return self._bills[index]


