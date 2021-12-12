from utils import read_day_lines


class OctopusesGarden:
    def __init__(self, octopi):
        self.width = len(octopi[0])
        self.height = len(octopi)
        self.octopi = [list(map(int, line.strip())) for line in octopi]
        self.flashes = 0

    def __str__(self) -> str:
        return "\n".join(["".join(map(str, row)) for row in self.octopi])

    def step(self):
        self.increment_all()
        self.resolve_flashes()

    def increment_all(self):
        for point in self.all_points():
            self.increment(point)

    def resolve_flashes(self):
        remaining = self.to_flash()
        if len(remaining) > 0:
            for point in remaining:
                self.flashes += 1
                self.set_value(point, 0)
                self.flash_around(point)
            self.resolve_flashes()

    def to_flash(self):
        return [point for point in self.all_points() if self.value_at(point) > 9]

    def flash_around(self, point):
        for neighbour in self.get_neighbours(point):
            if self.value_at(neighbour) != 0:
                self.increment(neighbour)

    def increment(self, point):
        x, y = point
        self.octopi[x][y] += 1

    def value_at(self, point):
        x, y = point
        return self.octopi[x][y]

    def set_value(self, point, value):
        x, y = point
        self.octopi[x][y] = value

    def get_neighbours(self, point):
        x, y = point
        candidates = [
            (x-1, y+1), (x, y+1), (x+1, y+1),
            (x-1, y), (x+1, y),
            (x-1, y-1), (x, y-1), (x+1, y-1)
        ]

        return list(filter(lambda point: self.in_bounds(point), candidates))

    def in_bounds(self, point):
        x, y = point
        if x >= 0 and x < self.height:
            if y >= 0 and y < self.width:
                return True
        return False

    def all_points(self):
        return [(i, j) for i in range(self.width) for j in range(self.height)]

    def all_values(self):
        return [octopus for row in self.octopi for octopus in row]


def part1(lines):
    octopi = OctopusesGarden(lines)
    for _ in range(100):
        octopi.step()
    return octopi.flashes


def part2(lines):
    octopi = OctopusesGarden(lines)
    step = 0
    while True:
        step += 1
        octopi.step()
        if all(map(lambda value: value == 0, octopi.all_values())):
            return step


if __name__ == '__main__':
    lines = read_day_lines(11)
    print(part1(lines), part2(lines))
