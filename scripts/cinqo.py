from master import read_file


def read_crates(content, crates=3, multimove=False):
    crates_content = [[] for _ in range(crates)]
    loading = True
    for line in content:
        splitted = line.split(' ')
        if loading:
            if splitted[1] == '1':
                loading = False
                for crate in crates_content:
                    crate.reverse()
                continue
            if len(splitted) == crates:
                for stack, char in enumerate(splitted):
                    crates_content[stack].append(char[1])
            else:
                is_char = False
                for counter, char in enumerate(line):
                    if is_char:
                        position = counter // 4
                        crates_content[position].append(char)
                        is_char = False
                    if char == '[':
                        is_char = True
        else:
            if len(splitted) > 1:
                if multimove:
                    crates_to_move = [crates_content[int(splitted[3]) - 1].pop() for reps in range(int(splitted[1]))]
                    crates_to_move.reverse()
                    for reps in range(int(splitted[1])):
                        crates_content[int(splitted[5]) - 1].append(crates_to_move[reps])
                else:
                    for reps in range(int(splitted[1])):
                        crates_content[int(splitted[5]) - 1].append(crates_content[int(splitted[3]) - 1].pop())
    return ''.join([crate.pop() for crate in crates_content])


if __name__ == '__main__':
    print(read_crates(read_file('../inputs/cinqo.txt'), 9, False))
    print(read_crates(read_file('../inputs/cinqo.txt'), 9, True))
