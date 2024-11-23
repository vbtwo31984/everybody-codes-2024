import unittest

class Quest2:
    def _runic_words(self, input):
        return input[6:].split(",")

    def part1(self, input):
        lines = input.splitlines()
        runic_words = self._runic_words(lines[0])
        inscription = lines[2]
        word_counts = {word: inscription.count(word) for word in runic_words}
        total = sum(word_counts.values())
        return total
        
    def part2(self, input):
        lines = input.splitlines()
        runic_words = self._runic_words(lines[0])
        runic_words += [word[::-1] for word in runic_words]
        inscriptions = lines[2:]

        total = 0
        for inscription in inscriptions:
            found = [False] * len(inscription)
            for i in range(len(inscription)):
                for word in runic_words:
                    if inscription[i:i+len(word)] == word:
                        for j in range(len(word)):
                            found[i+j] = True
            num_found = found.count(True)
            total += num_found

        return total
        
    def part3(self, input):
        return False

class TestQuest2(unittest.TestCase):
    quest = Quest2()
    def test_part1(self):
        input = """WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE"""
        result = self.quest.part1(input)
        self.assertEqual(result, 4)

    def test_part2(self):
        input = """WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ"""
        result = self.quest.part2(input)
        self.assertEqual(result, 42)

#     def test_part3(self):
#         input = """WORDS:THE,OWE,MES,ROD,RODEO

# HELWORLT
# ENIGWDXL
# TRODEOAL"""
#         result = self.quest.part3(input)
#         self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()