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
    max_len = len(schematic[0]) - 1
    max_depth = len(schematic) - 1
    top = get_slice(start, end, max_len, schematic[y - 1]) if y > 0 else "."*(end - start + 2)
    middle = get_slice(start, end, max_len, schematic[y])
    bottom = get_slice(start, end, max_len, schematic[y + 1]) if y < max_depth else "."*(end - start + 2)
    search_area = [top, middle, bottom]
    attached = False
    gear_coord = None
    for i in range(0, 3):
        attachments = re.search(r"[^\d\.]", search_area[i])
        if attachments:
            attached = True
            if attachments.group() == '*':
                (g_start, _) = attachments.span()
                gear_coord = (y + i, g_start + start)
    return (attached, gear_coord)

def get_slice(start, end, max_len, line):
    result = line[start - 1:end] if start > 0 else "." + line[start:end]
    result += line[end] if end < max_len else "."
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