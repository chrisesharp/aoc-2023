import re

def is_possible(game, actuals) -> bool:
    (reds, greens, blues)  = actuals
    for iteration in game:
        if int(iteration.get("red", 0)) > reds or int(iteration.get("green", 0)) > greens or int(iteration.get("blue", 0)) > blues:
            return False
    return True

def power(game):
    reds = greens = blues = 0
    for iteration in game:
        reds = max(reds, int(iteration.get("red", 0)))
        greens = max(greens, int(iteration.get("green", 0)))
        blues = max(blues, int(iteration.get("blue", 0)))
    return reds * greens * blues

def parse(input_data):
    return list(map(get_scores, input_data))

def get_scores(line):
    return [get_cubes(i) for i in line.split(':')[1].split(';')]

def get_cubes(iteration):
    cubes = {}
    for group in re.findall(r"(\d+ \w+)+", iteration):
        (num, colour) = group.split()
        cubes[colour] = num
    return cubes

if __name__ == '__main__':
    games = parse(open("input.txt", "r").readlines())
    actuals = (12, 13, 14)
    possibles = [i+1 for i, x in enumerate(games) if is_possible(x, actuals)]
    print("Part 1: ", sum(possibles))
    powers = [power(g) for g in games]
    print("Part 2: ", sum(powers))
