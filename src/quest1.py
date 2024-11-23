import unittest

class Quest1:
    def _num_potions(self,creature):
        if creature == "B":
            return 1
        elif creature == "C":
            return 3
        elif creature == "D":
            return 5
        else:
            return 0
        
    def _num_potions_in_pair(self, pair: str):
        addition = 2
        if 'x' in pair:
            addition = 0
        return self._num_potions(pair[0]) + self._num_potions(pair[1]) + addition
    
    def _num_potions_in_triple(self, triple: str):
        count = triple.count('x')
        extra = 0
        if(count == 0):
            extra = 6
        elif(count == 1):
            extra = 2
        return self._num_potions(triple[0]) + self._num_potions(triple[1]) + self._num_potions(triple[2]) + extra
        
    def part1(self, input):
        result = sum(map(self._num_potions, input))
        return result
        
    def part2(self, input):
        pairs = [input[i:i+2] for i in range(0, len(input), 2)]
        updated = list(map(self._num_potions_in_pair, pairs))

        result = sum(updated)
        return result
        
    def part3(self, input):
        triples = [input[i:i+3] for i in range(0, len(input), 3)]
        updated = list(map(self._num_potions_in_triple, triples))

        result = sum(updated)
        return result

class TestQuest1(unittest.TestCase):
    quest = Quest1()
    def test_part1(self):
        result = self.quest.part1("ABBAC")
        self.assertEqual(result, 5)

    def test_part2(self):
        result = self.quest.part2("AxBCDDCAxD")
        self.assertEqual(result, 28)

    def test_part3(self):
        result = self.quest.part3("xBxAAABCDxCC")
        self.assertEqual(result, 30)

if __name__ == '__main__':
    unittest.main()