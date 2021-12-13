import re
from utils import read_all


def parseXY(line):
    x, y = line.split(",")
    return (int(x), int(y))


class Paper:
    def __init__(self, coordlines) -> None:
        self.coords = set(map(parseXY, coordlines))
        self.width = max(map(lambda point: point[0], self.coords)) + 1
        self.height = max(map(lambda point: point[1], self.coords)) + 1

    def __str__(self) -> str:
        result = ""
        for y in range(self.height):
            for x in range(self.width):
                point = (x, y)
                if point in self.coords:
                    char = ("#")
                else:
                    char = (".")
                result += char
            result += ("\n")
        return result

    def fold(self, pair):
        match pair:
            case ("x", value):
                return self.foldx(value)
            case ("y", value):
                return self.foldy(value)
            case other:
                raise NotImplementedError(f"fold: {other}")

    def foldx(self, value):
        past_the_fold = [(x, y) for x, y in self.coords if x > value]
        for point in past_the_fold:
            x, y = point
            self.coords.remove(point)
            xdiff = x - value
            xvalue = value - xdiff
            self.coords.add((xvalue, y))
        self.width = value

    def foldy(self, value):
        below_the_fold = [(x, y) for x, y in self.coords if y > value]
        for point in below_the_fold:
            x, y = point
            self.coords.remove(point)
            ydiff = y - value
            yvalue = value - ydiff
            self.coords.add((x, yvalue))
        self.height = value

    def dots_count(self):
        return len(self.coords)


if __name__ == '__main__':
    input = read_all(13)

    coordstr, foldstr = input.strip().split("\n\n")
    paper = Paper(coordstr.split("\n"))

    folds = []
    for line in foldstr.split("\n"):
        [(axis, value)] = re.findall(r"fold along (\w)=(\d+)", line)
        folds.append((axis, int(value)))

    # Part 1
    [first, *rest] = folds
    paper.fold(first)
    print(paper.dots_count(), "\n")

    # Part 2
    for fold in rest:
        paper.fold(fold)

    print(paper)
