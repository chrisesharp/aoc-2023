def parse_pt1(data):
    total = 0
    for line in data:
        winners = set()
        present = set()
        (_, numbers) = line.split(":")
        (winning, have) = numbers.split("|")
        for num in winning.split():
            winners.add(int(num))
        for num in have.split():
            present.add(int(num))
        wins = len(winners.intersection(present))
        if wins:
            total += pow(2, wins - 1)
    return total

def parse_pt2(data):
    i = 1
    j = 0
    cards = [data[0]]
    while j < len(cards):
        card = cards[j]
        winners = set()
        present = set()
        (id, numbers) = card.split(":")
        card_num = int(id.split()[1])
        # print("Looking at ", j, card_num)
        (winning, have) = numbers.split("|")
        for num in winning.split():
            winners.add(int(num))
        for num in have.split():
            present.add(int(num))
        wins = len(winners.intersection(present))
        if wins:
            for c in data[card_num:card_num + wins]:
                # print("Adding copy of card ", c)
                cards.append(c)
        j += 1
        if (i < len(data)):
            # print("Adding card ", i+1)
            cards.append(data[i])
            i += 1
    return len(cards)

if __name__ == '__main__':
    data = open("input.txt", "r").readlines()
    points = parse_pt1(data)
    print("Part 1: ", points)
    points = parse_pt2(data)
    print("Part 2: ", points)