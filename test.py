import unittest
from miner import hash

class TestMiner(unittest.TestCase):
    def testHashFunction(self):
        string = "teststring"
        thehash = hash(string.encode())
        self.assertEquals(thehash, '3c8727e019a42b444667a587b6001251becadabbb36bfed8087a92c18882d111')

if __name__ == '__main__':
    unittest.main()