from src.quest3 import Quest3

quest = Quest3()

with open('input/03_01.txt') as f:
    input = f.read()
print("Part 1:", quest.part1(input))

with open('input/03_02.txt') as f:
    input = f.read()
print("Part 2:", quest.part2(input))

with open('input/03_03.txt') as f:
    input = f.read()
print("Part 3:", quest.part3(input))