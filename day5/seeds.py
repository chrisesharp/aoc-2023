import sys

def parse_input(data):
    header = data.pop(0).split(':')[1]
    seeds = [int(i) for i in header.split()]
    maps = {}
    for section in data:
        (source, dest, mappings) = parse_section(section.splitlines())
        maps[source] = {dest: mappings}
    return (seeds, maps)

def parse_section(section):
    (source, _, dest) = section.pop(0).split()[0].split('-')
    mappings = {}
    for line in section:
        (d, s, r) = line.split()
        mappings[int(s)] = (int(d), int(r))
    return (source, dest, mappings)

def follow_map(seed, mappings):
    key = 'seed'
    for _ in range(7):
        next_map_name = list(mappings[key].keys())[0]
        this_map = mappings[key]
        key = next_map_name
        seed = get_value(seed, this_map[next_map_name])
    return seed

def reverse_map(value, mappings):
    # Need to work through this
    keys = ['location', 'humidity', 'temperature', 'light','water', 'fertilizer', 'soil', 'seed']
    map_name = keys.pop(0)
    key = keys[0]
    print(f"map_name = {map_name}, key={key}")
    this_map = mappings[key]
    value = get_value(value, this_map[map_name])
    print("value:", value)
    print(mappings)

def get_value(key, mapping):
    keys = sorted(mapping.keys())
    while len(keys):
        next_key = keys.pop(0)
        next_value, next_range = mapping[next_key]
        if key < next_key:
            return key
        else:
            if key >= next_key and key <= next_key + next_range:
                delta = key - next_key
                return next_value + delta
    return key

if __name__ == '__main__':
    data = open("input.txt", "r").read()
    (seeds, maps) = parse_input(data.split("\n\n"))
    lowest = sys.maxsize
    for seed in seeds:
        location = follow_map(seed, maps)
        if location < lowest:
            lowest = location
    print("Part 1: ", lowest)
