from bill import Bill
import unittest


#Pishem testove kato naslediavam unittest.TestCase
#Pravim class koito zapochva s Test..
#vseki metod da zapochva s test. i vseki test e metod
#Testovete triabva da sa nezavisimi!!
#Ne e sigurno v kakva porednost se izvikvat




class TestBill(unittest.TestCase):

	def setUp(self):
		self.b = Bill(5)# za da moje da se dostup ot drugite funkcii :) 

	def test_bill_init(self):
		self.assertEqual(self.b._amount, 5)

	def test_bill_str(self):
		self.assertEqual(str(self.b), "A 5$ bill")

	def test_bill_int(self):
		self.assertEqual(int(self.b), 5)		

	def test_bill_eq(self):
		bill2 = Bill(10)
		bill3 = Bill(5)
		self.assertFalse(self.b == bill2)
		self.assertTrue(self.b == bill3)
		self.assertEqual(self.b, bill3)
		self.assertNotEqual(bill2, bill3)



if __name__=='__main__':
	unittest.main()

	#tova ste pusne vsichki testove, toest metodi zapochvasti s test
	#i koito naslediavat unittest.TestCase!!!