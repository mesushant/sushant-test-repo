from calc import Calculator
import unittest

class TestCalc(unittest.TestCase):
	def setUp(self):
		print "Setting up"
		self.c = Calculator() 
	
	def tearDown(self):
		pass
	
	def test_add(self):
		self.assertEqual(self.c.add(5,5), 10)
		self.assertEqual(self.c.add(15,5), 20)
		
	def test_sub(self):
		self.assertEqual(self.c.sub(5,5), 0)
		self.assertEqual(self.c.sub(15,5), 10)
		
		
 
if __name__ == '__main__':
    unittest.main()