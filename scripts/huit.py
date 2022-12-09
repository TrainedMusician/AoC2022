import numpy as np


def convert_matrix(file_path, output_file):
    content = [' '.join(list(line)) for line in open(file_path).read().split('\n')]
    with open(output_file, 'w') as write_file:
        write_file.write('\n'.join(content))


def read_matrix(file_path):
    return np.loadtxt(file_path)


def count_trees(forest):
    min_tree = min(forest[0], forest[-1])
    trees = 0
    for value in forest[1:-1]:
        if value > min_tree:
            # print('%d\t%d' % (value, min_tree))
            min_tree = value
            trees += 1
    return trees


if __name__ == '__main__':
    print(convert_matrix('../inputs/huit.txt', '../inputs/converted.txt'))
    total = 0
    vertical, horizontal = read_matrix('../inputs/converted.txt').shape
    vertical *= 2
    horizontal = horizontal * 2 - 4
    total += vertical + horizontal
    print(total)
    print(np.apply_along_axis(count_trees, 1, read_matrix('../inputs/converted.txt')[1:, :]).sum())
    total += np.apply_along_axis(count_trees, 1, read_matrix('../inputs/converted.txt')[1:, :]).sum()
    print(total)
