import unittest
from roulette import play_roulette

# Alle testene gikk gjennom. Ingen feil

class test_play_roulette(unittest.TestCase):
    def test_3(self):
        self.assertEqual(play_roulette(3), "P03 PR PO P1-18")
    
    def test_8(self):
        self.assertEqual(play_roulette(8), "P08 PB PE P1-18")
    
    def test_34(self):
        self.assertEqual(play_roulette(34), "P34 PR PE P19-36")
    
    def test_37(self):
        self.assertEqual(play_roulette(37), "P0")

    def test_39(self):
        self.assertEqual(play_roulette(39), "ERR")

if __name__ == "__main__":
    unittest.main()