#!/usr/bin/python3

def findTheDupe(p1, p2):
    for x in p1:
        for y in p2:
            if x == y:
                return x
    return ("NA")


def findTheBadge(p1, p2, p3):
    for x in p1:
        for y in p2:
            for z in p3:
                if x == y == z:
                    return x
    return ("NA")


def letterScore(dupeitem):
    if (dupeitem.islower()):
        return (ord(dupeitem)-96)
    else:
        return (ord(dupeitem)-38)


def main():
    total1 = 0
    total2 = 0

    with open('day-3.input') as f:
        lines = f.readlines()
    sacks = tuple(line.rstrip('\n') for line in lines)

    for s in sacks:
        p1, p2 = s[:(len(s))//2], s[(len(s))//2:]
        dupeitem = findTheDupe(p1, p2)
        total1 += (letterScore(dupeitem))

    for x in range(0, len(sacks), 3):
        badge = findTheBadge(sacks[x], sacks[x+1], sacks[x+2])
        total2 += (letterScore(badge))

    print(total1)
    print(total2)

main()
