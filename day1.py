def read_day_lines(day):
    with open(f"./inputs/day{day}.txt") as f:
        return f.readlines()


def part1():
    sonar_sweeps = [int(line) for line in read_day_lines(1)]
    increases = -1
    current = 0
    for sweep in sonar_sweeps:
        if sweep > current:
            increases += 1
        current = sweep
    return increases


def part2():
    sonar_sweeps = [int(line) for line in read_day_lines(1)]
    increases = -1
    current = 0
    for i in range(len(sonar_sweeps) - 2):
        total = sum(sonar_sweeps[i:i+3])
        if total > current:
            increases += 1
        current = total
    return increases


if __name__ == '__main__':
    print(part1())
    print(part2())
