import unittest
from custom import *

class Test(unittest.TestCase):
    def test_registry(self):
        reg = PlayerRegistry()
        player_1 = Player("alice", 35)
        player_2 = Player("bob", 33)
        
        reg.add(player_1)
        reg.add(player_2)

        entries = reg.players()

        self.assertEqual("alice", entries[0].name)
        self.assertEqual(35, entries[0].age)
        self.assertEqual("bob", entries[1].name)
        self.assertEqual(33, entries[1].age)


if __name__ == '__main__':
    unittest.main()