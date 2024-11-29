import unittest

class Quest3:
    def _exists(self, layers, num):
        for layer in layers:
            if num in layer:
                return True
    
    def _to_int(self, char):
        return int(char) if char.isdigit() else 0
            
    def part1(self, input):
        input = input.replace('#', '1')
        layers = input.splitlines()
        layers = [[self._to_int(char) for char in line] for line in layers]
        cur_num = 1
        while(self._exists(layers, cur_num)):
            for y in range(1, len(layers)-1):
                for x in range(1,len(layers[0])-1):
                    if(layers[y-1][x] >= cur_num 
                       and layers[y+1][x] >= cur_num 
                       and layers[y][x-1] >= cur_num 
                       and layers[y][x+1] >= cur_num):
                        layers[y][x] = cur_num + 1
            cur_num += 1

        total_count = sum(c for layer in layers for c in layer)
        return total_count 
    
    def part2(self, input):
        return self.part1(input)
    
    def part3(self, input):
        input = input.replace('#', '1')
        layers = input.splitlines()
        layers.insert(0, '.' * len(layers[0]))
        layers.append('.' * len(layers[0]))
        layers = ['.' + line + '.' for line in layers]

        layers = [[self._to_int(char) for char in line] for line in layers]
        prev_sum = -1
        cur_sum = sum(c for layer in layers for c in layer)
        cur_num = 1
        while(cur_sum != prev_sum):
            prev_sum = cur_sum
            for y in range(1, len(layers)-1):
                for x in range(1,len(layers[0])-1):
                    if(layers[y-1][x] >= cur_num 
                       and layers[y-1][x-1] >= cur_num
                       and layers[y-1][x+1] >= cur_num
                       and layers[y][x-1] >= cur_num 
                       and layers[y][x+1] >= cur_num
                       and layers[y+1][x] >= cur_num 
                       and layers[y+1][x-1] >= cur_num
                       and layers[y+1][x+1] >= cur_num
                       and layers[y][x] != 0):
                        layers[y][x] = cur_num + 1
                        cur_sum += 1
            cur_num += 1

        return cur_sum 
    
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

    def test_part3(self):
        input = """..........
..###.##..
...####...
..######..
..######..
...####...
.........."""
        result = self.quest.part3(input)
        self.assertEqual(result, 29)

if __name__ == '__main__':
    unittest.main()