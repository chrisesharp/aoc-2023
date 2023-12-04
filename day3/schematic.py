import re
import math

def parse(schematic):
    numbers = {}
    for y, line in enumerate(schematic):
        for number in re.finditer(r"(\d+)", line):
            if number:
                coords = (y, number.start(), number.end())
                part_num = numbers.get(number.group(0), [])
                part_num.append(coords)
                numbers[number.group()] = part_num
    return numbers

def is_attached(coords, schematic):
    (y, start, end) = coords
    width = len(schematic[0]) - 1
    depth = len(schematic) - 1
    search_area = [
        get_slice(start, end, width, schematic[y - 1]) if y > 0 else "."*(end - start + 2),
        get_slice(start, end, width, schematic[y]),
        get_slice(start, end, width, schematic[y + 1]) if y < depth else "."*(end - start + 2)
    ]
    attached = False
    gear_coord = None
    for delta, row in enumerate(search_area):
        if attachments := re.search(r"[^\d\.]", row):
            attached = True
            if attachments.group() == '*':
                gear_coord = (y + delta, start + attachments.span()[0])
    return (attached, gear_coord)

def get_slice(start, end, width, line):
    result = line[start - 1:end] if start > 0 else "." + line[start:end]
    result += line[end] if end < width else "."
    return result

def gear_ratio(parts):
    return math.prod(parts) if len(parts) == 2 else 0

def add_part_to_gear(number, gear, gears):
    parts = gears.get(gear,[])
    parts.append(int(number))
    gears[gear] = parts

if __name__ == '__main__':
    schematic = open("input.txt", "r").readlines()
    numbers = parse(schematic)
    gears = {}
    total = 0
    for number in numbers.keys():
        for coord in numbers[number]:
            (attached, gear) = is_attached(coord, schematic)
            if attached:
                total += int(number)
                if gear:
                    add_part_to_gear(number, gear, gears)
    print("Part 1: ", total)
    print("Part 2: ", sum([gear_ratio(parts) for parts in gears.values()]))