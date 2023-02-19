import unittest
from custom import *

class Test(unittest.TestCase):
    def test_registry_add(self):
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
    
    def test_registry_first(self):
        reg = PlayerRegistry()
        player_1 = Player("alice", 35)
        player_2 = Player("bob", 33)
        
        reg.add(player_1)
        reg.add(player_2)

        first = reg.first()

        self.assertEqual("alice", first.name)
        self.assertEqual(35, first.age)
    
    def test_registry_merge(self):
        reg_a = PlayerRegistry()
        reg_b = PlayerRegistry()

        player_1 = Player("alice", 35)
        player_2 = Player("bob", 33)
        player_3 = Player("carol", 37)
        player_4 = Player("denis", 38)
        
        reg_a.add(player_1)
        reg_a.add(player_2)

        reg_b.add(player_3)
        reg_b.add(player_4)

        reg_a.merge(reg_b)

        self.assertEqual(4, len(reg_a.players()))
    
    def test_winners_check(self):
        reg_a = PlayerRegistry()
        reg_b = PlayerRegistry()

        player_1 = Player("alice", 35)
        player_2 = Player("bob", 33)
        player_3 = Player("carol", 37)
        player_4 = Player("denis", 38)
        
        reg_a.add(player_1)
        reg_a.add(player_2)

        reg_b.add(player_3)
        reg_b.add(player_4)

        final_winners = winners(reg_a, reg_b)

        self.assertEqual("alice", final_winners[0].name)
        self.assertEqual(35, final_winners[0].age)
        self.assertEqual("carol", final_winners[1].name)
        self.assertEqual(37, final_winners[1].age)

    def test_race(self):
        reg = PlayerRegistry()
        player_1 = Player("alice", 35)
        player_2 = Player("bob", 33)
        
        reg.add(player_1)
        reg.add(player_2)


        race = Race(reg)
        
        self.assertEqual(2, len(race.player_registry().players()))
        
if __name__ == '__main__':
    unittest.main()