import re

def calibrate(line):
    number_word = ""
    numbers = []
    for c in line:
        if c.isnumeric():
            numbers.append(c)
            continue
        else:
            number_word += c

        if result := re.search(r"(zero)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)+", number_word):
            for i, group in enumerate(result.groups()):
                if group:
                    numbers.append(str(i))
                    number_word = number_word[-1]
                    break

    return int(numbers[0] + numbers[-1])

if __name__ == '__main__':
    total = sum(list(map(calibrate, open("input.txt", "r").readlines())))
    print("total", total)

