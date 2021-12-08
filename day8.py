from utils import read_day_lines
import itertools


def part1():
    lines = read_day_lines(8)
    outs = [map(len, output.split(" "))
            for [_, output] in map(lambda line: line.split(" | "), lines)]
    return len([digit for digit in itertools.chain(
        *outs) if digit in [2, 4, 3, 7]])


def find_digit(candidate, encoding):
    for k, v in encoding.items():
        if v == candidate:
            return k


def output_value(pair):
    (ins, outs) = pair

    encoding = {}
    for candidate in ins:
        if len(candidate) == 2:
            encoding[1] = candidate
        elif(len(candidate)) == 4:
            encoding[4] = candidate
        elif(len(candidate)) == 3:
            encoding[7] = candidate
        elif(len(candidate)) == 7:
            encoding[8] = candidate

    for candidate in ins:
        if len(candidate) == 6 and encoding[7].issubset(candidate) and encoding[4].issubset(candidate):
            encoding[9] = candidate
        elif len(candidate) == 6 and encoding[7].issubset(candidate):
            encoding[0] = candidate
        elif len(candidate) == 6:
            encoding[6] = candidate

    for candidate in ins:
        if len(candidate) == 5 and candidate.issubset(encoding[6]):
            encoding[5] = candidate
        elif len(candidate) == 5 and encoding[1].issubset(candidate):
            encoding[3] = candidate
        elif len(candidate) == 5:
            encoding[2] = candidate

    return int("".join(str(find_digit(candidate, encoding)) for candidate in outs))


def part2():
    readings = []
    for line in read_day_lines(8):
        [inn, out] = line.split(" | ")
        ins = list(map(set, inn.split(" ")))
        outs = list(map(set, out.split(" ")))
        readings.append((ins, outs))

    return sum(map(output_value, readings))


if __name__ == '__main__':
    print(part1(), part2())
