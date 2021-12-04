def read_day_lines(day):
    with open(f"./inputs/day{day}.txt") as f:
        return [line.strip() for line in f.readlines()]


def read_all(day):
    with open(f"./inputs/day{day}.txt") as f:
        return f.read()
