from utils import read_day_lines


def part1():
    inputs = read_day_lines(2)
    location = (0, 0)
    for input in inputs:
        match input.split():
            case ["forward", x]:
                location = (location[0] + int(x), location[1])
            case ["up", x]:
                location = (location[0], location[1] - int(x))
            case ["down", x]:
                location = (location[0], location[1] + int(x))
            case something_else:
                raise RuntimeError(f"Unknown: {something_else}")

    return(location[0] * location[1])


def part2():
    inputs = read_day_lines(2)
    location = (0, 0)
    aim = 0
    for input in inputs:
        match input.split():
            case ["forward", x]:
                location = (location[0] + int(x), location[1] + (aim * int(x)))
            case ["up", x]:
                aim -= int(x)
            case ["down", x]:
                aim += int(x)
            case something_else:
                raise RuntimeError(f"Unknown: {something_else}")

    return(location[0] * location[1])


if __name__ == '__main__':
    print(part1(), part2())
