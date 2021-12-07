from utils import read_all


def fuel_cost(steps):
    if steps in cache:
        return cache[steps]

    if steps == 0:
        return 0

    if steps == 1:
        return 1

    cost = steps + fuel_cost(steps-1)
    cache[steps] = cost
    return cost


def calculate1(crabs, pos):
    return sum(abs(crab - pos) for crab in crabs)


def calculate2(crabs, pos):
    return sum(fuel_cost(abs(crab - pos)) for crab in crabs)


def part1(crabs):
    [first, *_rest, last] = crabs
    return min([calculate1(crabs, pos) for pos in range(first, last)])


def part2(crabs):
    [first, *rest, last] = crabs
    return min([calculate2(crabs, pos) for pos in range(first, last)])


if __name__ == '__main__':
    cache = {}
    crab_input = read_all(7)
    # crab_input = "16,1,2,0,4,2,7,1,2,14"
    crabs = sorted(int(crab) for crab in crab_input.split(","))

    print(part1(crabs), part2(crabs))
