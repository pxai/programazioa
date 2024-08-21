import unittest
import kalkulagailua

class TestStringMethods(unittest.TestCase):
    def test_batu(self):
        kal = kalkulagailua.Kalkulagailua()
        self.assertEqual(kal.batu(40, 2), 42)

    def test_kendu(self):
        kal = kalkulagailua.Kalkulagailua()
        self.assertEqual(kal.kendu(40, 2), 38)

    def test_biderkatu(self):
        kal = kalkulagailua.Kalkulagailua()
        self.assertEqual(kal.biderkatu(40, 2), 80)

    def test_zatitu(self):
        kal = kalkulagailua.Kalkulagailua()
        self.assertEqual(kal.zatitu(40, 2), 20)

if __name__ == '__main__':
    unittest.main()