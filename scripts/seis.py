from master import read_file


def find_start(content, length=4):
    for i in range(length, len(content[0]) + 1):
        current_marker = content[0][i - length:i]
        if len(set(current_marker)) == length:
            print('%d\t%s' % (i, current_marker))
            return i


if __name__ == '__main__':
    print(find_start(read_file('../inputs/seis.txt')))
    print(find_start(read_file('../inputs/seis.txt'), 14))
