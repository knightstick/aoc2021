import math
from utils import read_day_lines


class HeightMap:
    def __init__(self, height_map):
        self.width = len(height_map[0])
        self.height = len(height_map)
        self.height_map = height_map

    def value_at(self, point):
        return self.height_map[point[0]][point[1]]

    def get_neighbours(self, point):
        x, y = point
        neighbours = []
        if x-1 >= 0:
            neighbours.append((x-1, y))
        if x+1 < self.height:
            neighbours.append((x+1, y))
        if y-1 >= 0:
            neighbours.append((x, y-1))
        if y+1 < self.width:
            neighbours.append((x, y+1))
        return neighbours

    def get_all_neighbours(self, a_set):
        all_neighbours = set()
        for point in a_set:
            all_neighbours = all_neighbours.union(self.get_neighbours(point))
        return all_neighbours

    def low_points(self):
        return [(i, j) for j in range(
            self.width) for i in range(self.height) if self.low_point((i, j))]

    def low_point(self, point):
        value = self.value_at(point)
        return all(
            map(
                lambda neighbour: self.value_at(neighbour) > value,
                self.get_neighbours(point)))

    def risks(self):
        return map(lambda point: self.value_at(point) + 1, self.low_points())

    def basins(self):
        return [self.basin(point) for point in self.low_points()]

    def basin(self, point):
        return self.__basin_recur__(set([point]))

    def __basin_recur__(self, current_set):
        new_points = [neighbour for neighbour in self.get_all_neighbours(
            current_set) if neighbour not in current_set and self.value_at(neighbour) != 9]
        if len(new_points) == 0:
            return current_set

        current_set.update(new_points)
        return self.__basin_recur__(current_set)


def part1(height_map):
    return sum(height_map.risks())


def part2(height_map):
    return math.prod(sorted(map(len, height_map.basins()), reverse=True)[0:3])


if __name__ == '__main__':
    lines = read_day_lines(9)
    the_height_map = HeightMap(
        [list(map(int, line.strip())) for line in lines])
    print(part1(the_height_map), part2(the_height_map))
