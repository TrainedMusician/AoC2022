from master import read_file


def get_priority(content):
    score = 0
    priorities = {}
    for i, item in enumerate('abcdefghijklmnopqrstuvwxyz'):
        priorities[item] = i + 1
        priorities[item.upper()] = i + 27
    for rucksack in content:
        uno = set(rucksack[:len(rucksack) // 2])
        dos = set(rucksack[len(rucksack) // 2:])
        for i in uno:
            if i in dos:
                print('Yay! %d' % priorities[i])
                score += priorities[i]
    return score


def get_badges(content):
    score = 0
    priorities = {}
    current_group = []
    for i, item in enumerate('abcdefghijklmnopqrstuvwxyz'):
        priorities[item] = i + 1
        priorities[item.upper()] = i + 27
    for rucksack in content:
        current_group.append(rucksack)
        if len(current_group) == 3:
            uno = set(current_group[0])
            dos = set(current_group[1])
            tres = set(current_group[2])
            for i in uno:
                if i in dos and i in tres:
                    # print('Yay %s\t%d' % (i, priorities[i]))
                    score += priorities[i]
            current_group = []
        # current_group = []
    return score


if __name__ == '__main__':
    # print(get_priority(read_file('../inputs/tres.txt')))
    print(get_badges(read_file('../inputs/tres.txt')))
