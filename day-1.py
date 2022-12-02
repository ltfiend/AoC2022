#!/usr/bin/python3


with open('day-1.input') as f:
    lines = f.readlines()
input = tuple(line.rstrip('\n') for line in lines)


def calculateTotal():
    elfn = 0
    elft = []
    total = 0
    for i in range(len(input)):
        if input[i] == "":
            # print(f"{elfn} -- {total}")
            elft.insert(elfn, total)
            total = 0
            elfn += 1
        else:
            total += int(input[i])
    elft.insert(elfn, total)
    return elft


def topThree(elft):
    elft.sort(reverse=True)
    total = elft[0] + elft[1] + elft[2]
    print(f"The total of the top three is is {total}")


def topCalories(elft):
    elft.sort(reverse=True)
    print(f"The elf with the most calories is carrying: {elft[0]}")


def topCaloriesWithElfN(elft):
    highelf = 0
    highcount = 0
    for i in range(len(elft)):
        if elft[i] > highcount:
            highcount = elft[i]
            highelf = i
    print(f"The elf with the most calories is carrying: {highcount} and is elf number {highelf}")


def main():
    elft = calculateTotal()
    # make sure to do this before the sort.
    topCaloriesWithElfN(elft)
    topThree(elft)
    topCalories(elft)


main()

# print(f"The answer is Elf #{highelf} with {highcount} calories\n")
