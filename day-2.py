#!/usr/bin/python3

def printInput(input):
    for i in range(len(input)):
        print(f"test - {input[i]}")


def main():
    tsp1 = 0
    tsp2 = 0

    scoredict = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
    }

    part2scoredict = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
    }

    with open('day-2.input') as f:
        lines = f.readlines()
        input = tuple(line.rstrip('\n') for line in lines)

    # printInput(input)

    for i in range(len(input)):
        cheapway = input[i].replace("\n", "")
        tsp1 += scoredict[cheapway]
        tsp2 += part2scoredict[cheapway]

    print(f"The answer to part 1 is: {tsp1}")    
    print(f"The score is {tsp2}")


main()
