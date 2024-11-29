from src.quest1 import Quest1

quest = Quest1()

with open('input/01_01.txt') as f:
    input = f.read()
print("Part 1:", quest.part1(input))

with open('input/01_02.txt') as f:
    input = f.read()
print("Part 2:", quest.part2(input))

with open('input/01_03.txt') as f:
    input = f.read()
print("Part 3:", quest.part3(input))