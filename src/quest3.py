import unittest

class Quest3:
    def _exists(self, layers, num):
        for layer in layers:
            if str(num) in layer:
                return True
    
    def _to_int(self, char):
        return int(char) if char.isdigit() else 0
            
    def part1(self, input):
        input = input.replace('#', '1')
        layers = input.splitlines()
        cur_num = 1
        while(self._exists(layers, cur_num)):
            for y in range(1, len(layers)-1):
                for x in range(1,len(layers[0])-1):
                    if(self._to_int(layers[y-1][x]) >= cur_num 
                       and self._to_int(layers[y+1][x]) >= cur_num 
                       and self._to_int(layers[y][x-1]) >= cur_num 
                       and self._to_int(layers[y][x+1]) >= cur_num):
                        layers[y] = layers[y][:x] + str(cur_num + 1) + layers[y][x+1:]
            cur_num += 1

        total_count = sum(int(c) for layer in layers for c in layer if c.isdigit())
        return total_count 
    
    def part2(self, input):
        return False
    
    def part3(self, input):
        return False
    
class TestQuest3(unittest.TestCase):
    def setUp(self):
        self.quest = Quest3()

    def test_part1(self):
        input = """..........
..###.##..
...####...
..######..
..######..
...####...
.........."""
        result = self.quest.part1(input)
        self.assertEqual(result, 35)

if __name__ == '__main__':
    unittest.main()