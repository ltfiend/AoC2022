#!/usr/bin/python3

# Part 1
# length = 4
# Part 2
length = 14


def main():
    counter = 0
    dupe = 0

    with open('day-6.input') as f:
        lines = f.readlines()
    input = tuple(line.replace('\n', ' ') for line in lines)

    for li in input:  # unnecessary but it's part of my default start
        for i in li:  # could use range and dump the counter variable
            chars = li[counter:counter+length]
            for x in range(length):
                checkchar = chars[0]
                chars = chars[1:]
                if checkchar in chars:
                    dupe = 1
                # print(f"type - {type(chars)} - chars - {chars}")
            if (dupe == 0):
                print(f"The answer is {counter+length}")
                quit()
            else:
                counter += 1
                dupe = 0
                continue


main()
