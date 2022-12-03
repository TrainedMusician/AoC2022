from master import read_file


def find_max(inventory, maximum=0):
    current_value = 0
    for i in inventory:
        if i:
            current_value += int(i)
        else:
            maximum = max(current_value, maximum)
            current_value = 0
    return maximum


def find_top(inventory, length=3):
    top_hoarders = []
    current_value = 0
    for i in inventory:
        if i:
            current_value += int(i)
        else:
            top_hoarders.append(current_value)
            if len(top_hoarders) > length:
                top_hoarders.remove(min(top_hoarders))
            current_value = 0
    return top_hoarders


if __name__ == '__main__':
    print(find_max(read_file('../inputs/un.txt')))
    print(sum(find_top(read_file('../inputs/un.txt'))))