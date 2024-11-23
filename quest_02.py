from src.quest2 import Quest2

quest = Quest2()

with open('input/02_01.txt') as f:
    input = f.read()
print("Part 1:", quest.part1(input))

with open('input/02_02.txt') as f:
    input = f.read()
print("Part 1:", quest.part2(input))

with open('input/02_03.txt') as f:
    input = f.read()
print("Part 1:", quest.part3(input))