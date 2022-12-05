#!/usr/bin/python3


def main():
    p1total = 0
    p2total = 0

    with open('day-4.input') as f:
        lines = f.readlines()
    input = tuple(line.rstrip('\n') for line in lines)

    for li in input:

        e1, e2 = li.split(',')
        e1s, e1e = e1.split('-')
        e2s, e2e = e2.split('-')

        # print(int(e1s), int(e1e), int(e2s), int(e2e))

        # Part 1

        if ((int(e1s)) <= (int(e2s))) and (int(e1e) >= int(e2e)):
            p1total += 1
        elif ((int(e1s)) >= (int(e2s))) and (int(e1e) <= int(e2e)):
            p1total += 1

        # Part 2

        if int(e1e) >= int(e2s) and int(e2e) >= int(e1s):
            p2total += 1

    print(p1total)
    print(p2total)


main()
