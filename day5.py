from collections import Counter
from utils import read_day_lines


def full_line(start, stop):
    (x1, y1), (x2, y2) = start, stop
    if x1 == x2:
        if y1 > y2:
            return [(x1, i) for i in range(y2, y1 + 1)]
        else:
            return [(x1, i) for i in range(y1, y2 + 1)]
    elif y1 == y2:
        if x1 > x2:
            return [(i, y1) for i in range(x2, x1 + 1)]
        else:
            return [(i, y1) for i in range(x1, x2 + 1)]
    else:
        if x1 < x2:
            xs = range(x1, x2+1)
        else:
            xs = range(x1, x2 - 1, -1)

        if y1 < y2:
            ys = range(y1, y2 + 1)
        else:
            ys = range(y1, y2 - 1, -1)

        return list(zip(xs, ys))


def part1():
    input = read_day_lines(5)
    pairs = [line.split(" -> ") for line in input]
    points = [(list(map(int, start.split(","))), list(
        map(int, stop.split(",")))) for start, stop in pairs]
    hoz_or_vert = [(start, stop) for start, stop in points if start[0]
                   == stop[0] or start[1] == stop[1]]

    lines = [full_line((x1, y1), (x2, y2))
             for (x1, y1), (x2, y2) in hoz_or_vert]

    flat = [item for sublist in lines for item in sublist]

    counts = Counter(flat)

    result = 0
    for _point, count in counts.items():
        if count >= 2:
            result += 1

    return result


def part2():
    input = read_day_lines(5)
    pairs = [line.split(" -> ") for line in input]
    points = [(list(map(int, start.split(","))), list(
        map(int, stop.split(",")))) for start, stop in pairs]
    lines = [full_line(start, stop) for start, stop in points]
    flat = [item for sublist in lines for item in sublist]

    counts = Counter(flat)
    result = 0
    for _point, count in counts.items():
        if count >= 2:
            result += 1

    return result


if __name__ == '__main__':
    print(part1(), part2())
