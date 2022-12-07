#!/usr/bin/python3


def main():
    counter = 0
    dupe = 0

    with open('day-6.input') as f:
        lines = f.readlines()
    input = tuple(line.replace('\n', ' ') for line in lines)

    for li in input:
        for i in li:
            chars = [li[counter:counter+14]]
            for x in range(14):
                checkchar = chars[0][0]
                chars[0] = chars[0][1:]
                if checkchar in chars[0]:
                    print("yep")
                    dupe = 1
                print(f"type - {type(chars)} - chars - {chars}")
            if (dupe == 0):
                print(counter+14)
                quit()
            else:
                print('reset')
                counter += 1
                dupe = 0
                continue


main()
