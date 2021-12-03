from collections import defaultdict
from utils import read_day_lines


def count_bits(lines):
    bitnum = len(lines[0])
    bits = [defaultdict(int) for i in range(bitnum)]

    for i in range(bitnum):
        for line in lines:
            bit = line[i]
            bits[i][bit] += 1

    return bits, bitnum


def find_gamma(bits_counter, bitnum):
    gamma_string = ""
    for i in range(bitnum):
        gamma_string += "1" if bits_counter[i]["1"] > bits_counter[i]["0"] else "0"
    return(int(gamma_string, 2))


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
    lines = [list(string.strip()) for string in read_day_lines(3)]
    counted_bits, bitnum = count_bits(lines)
    gamma = find_gamma(counted_bits, bitnum)
    epsilon = find_epsilon(gamma)
    return(gamma * epsilon)


def part2():
    lines = [list(string.strip()) for string in read_day_lines(3)]
    return (oxygen_generator_rating(lines) * co2_scrubber_rating(lines))


if __name__ == '__main__':
    print(part1(), part2())
