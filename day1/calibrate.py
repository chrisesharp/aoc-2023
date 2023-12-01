import re

num_map = [ r"(zero)", r"(one)", r"(two)", r"(three)", r"(four)", r"(five)", r"(six)", r"(seven)", r"(eight)", r"(nine)" ]
def calibrate(line):
    number = ""
    numbers = []
    for c in line:
        if c.isnumeric():
            numbers.append(c)
            continue
        else:
            number += c

        for i, regex in enumerate(num_map):
            if re.search(regex, number):
                numbers.append(str(i))
                number = number[-1]
                break

    return int("".join([numbers[0],numbers[-1]]))

if __name__ == '__main__':
    total = sum(list(map(calibrate, open("input.txt", "r").readlines())))
    print("total", total)

