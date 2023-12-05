def parse_pt1(data):
    total = 0
    for line in data:
        (_, numbers) = line.split(":")
        wins = parse_card(numbers)
        if wins:
            total += pow(2, wins - 1)
    return total

def parse_pt2(data):
    i = 1
    j = 0
    cards = [data[0]]
    cache = {}
    while j < len(cards):
        card = cards[j]
        j += 1
        (id, numbers) = card.split(":")
        card_num = int(id.split()[1])
        cached = cache.get(card_num, None)
        if cached is None:
            wins = parse_card(numbers)
            cache[card_num]= wins
        else:
            wins = cached
        if wins:
            cards += data[card_num:card_num + wins]
        if (i < len(data)):
            cards.append(data[i])
            i += 1
    return len(cards)

def parse_card(numbers):
    (winning, have) = numbers.split("|")
    winners = set([int(n) for n in winning.split()])
    present = set([int(n) for n in have.split()])
    return len(winners.intersection(present))

if __name__ == '__main__':
    data = open("input.txt", "r").readlines()
    points = parse_pt1(data)
    print("Part 1: ", points)
    points = parse_pt2(data)
    print("Part 2: ", points)