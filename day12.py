from collections import defaultdict
from typing import Counter
from utils import read_day_lines


class CaveSystem:
    def __init__(self, connection_strings, one_double=False) -> None:
        connections = defaultdict(set)
        for line in connection_strings:
            start, stop = line.split("-")
            connections[start].add(stop)
            connections[stop].add(start)
        self.connections = connections
        self.one_double = one_double

    def paths_from(self, start):
        return self.__paths_from__(start, [start])

    def __paths_from__(self, start, visited):
        if start == "end":
            return 1

        nexts = [connection for connection in self.connections[start]
                 if self.can_visit(connection, visited)]

        return sum(map(lambda next_stop: self.__paths_from__(next_stop, visited + [next_stop]), nexts))

    def can_visit(self, next_stop, visited):
        if next_stop == "start":
            return False
        if self.big_cave(next_stop):
            return True

        if next_stop in visited:
            if not self.one_double:
                return False
            visited_small_caves = filter(
                lambda elem: not self.big_cave(elem), visited)
            for _, count in Counter(visited_small_caves).items():
                if count > 1:
                    return False

        return True

    def big_cave(self, node):
        return node.upper() == node


def part1(lines):
    system = CaveSystem(lines)
    return system.paths_from("start")


def part2(lines):
    system = CaveSystem(lines, one_double=True)
    return system.paths_from("start")


if __name__ == '__main__':
    lines = read_day_lines(12)
    print(part1(lines), part2(lines))
