from master import read_file


def find_ranges(content):
    overlap = 0
    for pair in content:
        uno, dos = pair.split(',')
        start_uno, end_uno = uno.split('-')
        start_dos, end_dos = dos.split('-')
        if (int(start_uno) <= int(start_dos) and int(end_uno) >= int(end_dos)) or (int(start_dos) <= int(start_uno) and int(end_dos) >= int(end_uno)):
            overlap += 1
    return overlap


def find_overlap(content):
    overlap = 0
    for pair in content:
        uno, dos = pair.split(',')
        start_uno, end_uno = uno.split('-')
        values = list(range(int(start_uno), int(end_uno) + 1))
        start_dos, end_dos = dos.split('-')
        values.extend(list(range(int(start_dos), int(end_dos) + 1)))
        # print('%d\t%d\t%s' % (len(values), len(set(values)), values))
        overlap += 1 * (len(values) - len(set(values))) > 0
    return overlap


if __name__ == '__main__':
    # print(find_ranges(read_file('../inputs/quatro.txt')))
    print(find_overlap(read_file('../inputs/quatro.txt')))