import re

def calibrate(line):
    number = ""
    numbers = []
    for c in line:
        if c.isnumeric():
            numbers.append(c)
            continue
        else:
            number += c

        if result := re.search(r"(zero)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)+", number):
            for i, group in enumerate(result.groups()):
                if group:
                    numbers.append(str(i))
                    number = number[-1]
                    break

    return int("".join([numbers[0],numbers[-1]]))

if __name__ == '__main__':
    total = sum(list(map(calibrate, open("input.txt", "r").readlines())))
    print("total", total)

