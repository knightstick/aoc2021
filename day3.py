from collections import defaultdict
from collections import Counter
from utils import read_day_lines


def count_bits(lines):
    bitnum = len(lines[0])
    return [Counter([line[i] for line in lines]) for i in range(bitnum)]


def find_gamma(bits_counter):
    gamma_list = []
    for counter in bits_counter:
        [(best_bit, _)] = counter.most_common(1)
        gamma_list.append(best_bit)
    return(int("".join(gamma_list), 2))


def toggle(char):
    return "0" if char == "1" else "1"


def find_epsilon(gamma):
    epsilon_list = [toggle(char) for char in list(f"{gamma:b}")]
    return(int("".join(epsilon_list), 2))


def oxygen_generator_rating(lines):
    values = list(map(list, lines))

    for i in range(len(lines[0])):
        if len(values) == 1:
            break
        bits = defaultdict(int)
        for value in values:
            bit = value[i]
            bits[bit] += 1

        best_bit = "1" if bits["1"] >= bits["0"] else "0"

        values = [value for value in values if value[i] == best_bit]

    return int("".join(values[0]), 2)


def co2_scrubber_rating(lines):
    values = list(map(list, lines))

    for i in range(len(lines[0])):
        if len(values) == 1:
            break
        bits = defaultdict(int)
        for value in values:
            bit = value[i]
            bits[bit] += 1

        best_bit = "0" if bits["1"] >= bits["0"] else "1"
        values = [value for value in values if value[i] == best_bit]

    return int("".join(values[0]), 2)


def part1():
    lines = [list(string) for string in read_day_lines(3)]
    gamma = find_gamma(count_bits(lines))
    epsilon = find_epsilon(gamma)
    return(gamma * epsilon)


def part2():
    lines = [list(string) for string in read_day_lines(3)]
    return (oxygen_generator_rating(lines) * co2_scrubber_rating(lines))


if __name__ == '__main__':
    print(part1(), part2())
