from collections import defaultdict
from utils import read_day_lines


def step(fishies):
    new_fishies = defaultdict(int)
    resets = 0
    for value, count in fishies.items():
        if value == 0:
            resets += count
            new_fishies[8] += count
        else:
            new_fishies[value-1] = count
    new_fishies[6] += resets

    return new_fishies


def run(steps, fish_string):
    fish_list = list(map(int, fish_string.split(",")))
    fishies = defaultdict(int)
    for fish in fish_list:
        fishies[fish] += 1

    for _ in range(steps):
        fishies = step(fishies)
    return(sum(fishies.values()))


def part1():
    fish_string = read_day_lines(6)[0]
    # input = "3,4,3,1,2\n"
    return run(80, fish_string)


def part2():
    fish_string = read_day_lines(6)[0]
    # input = "3,4,3,1,2\n"
    return run(256, fish_string)


if __name__ == '__main__':
    print(part1(), part2())
