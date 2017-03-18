import unittest
import search

class TestSeachMethods(unittest.TestCase):
	
	def setUp(self):
		self.src = search.Search("https://api.sandbox.amadeus.com/v1.2/") 
		
		
	def test_getRequestURL(self):
		param = {"location" : "DUB", "currency": "EUR"}
		url = self.src.getRequestURL(param)
		self.assertEqual(url, "https://api.sandbox.amadeus.com/v1.2/?location=DUB&currency=EUR", "Not the correct URL created")

if __name__ == '__main__':
	unittest.main()