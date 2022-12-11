from master import read_file


def check_pixel(value, crt):
    if value - 1 <= crt <= value + 1:
        return '#'
    else:
        return '.'


def next_cycle(value, cycle, crt, pixels):
    pixels += check_pixel(value, crt)
    crt = (crt + 1) % 40
    cycle += 1
    return cycle, crt, pixels


def new_cpu(instructions):
    cycle = value = 1
    crt = 0
    pixels = ''
    for instruction in instructions:
        if instruction == 'noop':
            cycle, crt, pixels = next_cycle(value, cycle, crt, pixels)
            continue
        cycle, crt, pixels = next_cycle(value, cycle, crt, pixels)
        cycle, crt, pixels = next_cycle(value, cycle, crt, pixels)
        value += int(instruction.split()[1])
    return pixels


if __name__ == '__main__':
    pixels = new_cpu(read_file('../inputs/dix.txt'))
    for i in range(0, len(pixels), 40):
        print(pixels[i:i+40])
