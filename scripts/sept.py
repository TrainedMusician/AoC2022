from master import read_file


def find_sizes(content):
    sizes = {}
    current_dir = ''
    list_sizes = False
    for line in content:
        if list_sizes:
            splitted = line.split()
            if splitted[0] == 'dir':
                continue
            try:
                dir_size += int(splitted[0])
            except ValueError:
                sizes[current_dir] = dir_size
                current_dir_splitted = current_dir[:-1].split('/')
                for i in range(len(current_dir_splitted) - 1):
                    tmp_dir = '/'.join(current_dir_splitted[:(i + 1)]) + '/'
                    if tmp_dir not in sizes:
                        sizes[tmp_dir] = 0
                    sizes[tmp_dir] += dir_size
                list_sizes = False
        if line[:5] == '$ cd ':
            # change current_dir
            if line[5:] == '..':
                # move one back
                current_dir = '/'.join(current_dir[:-1].split('/')[:-1])
                if current_dir == '':
                    current_dir = '/'
            elif line[5:] == '/':
                current_dir += '/'
            else:
                current_dir += line[5:] + '/'
        elif line[:4] == '$ ls':
            # list sizes
            list_sizes = True
            dir_size = 0
    return sizes


if __name__ == '__main__':
    sizes = find_sizes(read_file('../inputs/sept.txt'))
    semi_total = 0
    for directory in sizes:
        if sizes[directory] < 100000:
            semi_total += sizes[directory]
    print(semi_total)