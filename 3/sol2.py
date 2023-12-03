class Solution:
    def __init__(self):
        self.grid = []
        self.included = set()

        with open('input', 'r') as f:
            lines = f.readlines()
            for line in lines:
                self.grid.append(line)

            self.r, self.c = len(self.grid), len(self.grid[0])

    def search_num(self, y: int, x: int) -> int:
        self.included.add((y, x))
        num_buffer = [self.grid[y][x]]

        dx = 1
        while x - dx >= 0 and self.grid[y][x - dx].isnumeric():
            self.included.add((y, x - dx))
            num_buffer.append(self.grid[y][x - dx])
            dx += 1

        num_buffer.reverse()
        dx = 1
        while x + dx < self.c and self.grid[y][x + dx].isnumeric():
            self.included.add((y, x + dx))
            num_buffer.append(self.grid[y][x + dx])
            dx += 1

        return int(''.join(num_buffer))

    def check_gear(self, y: int, x: int) -> int:
        first_gear = 0
        for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            ny, nx = y + dy, x + dx
            if ny >= 0 and ny < self.r and nx >= 0 and nx < self.c and \
                self.grid[ny][nx].isnumeric() and (ny, nx) not in self.included:

                if first_gear == 0:
                    first_gear = self.search_num(ny, nx)
                else:
                    return first_gear * self.search_num(ny, nx)

        return 0

    def solve(self):
        gear_ratio_sum = 0

        for y, row in enumerate(self.grid):
            for x, ch in enumerate(row + '.'):
                if ch != '*': continue
                gear_ratio_sum += self.check_gear(y, x)
                self.included.clear()

        print(gear_ratio_sum)

if __name__ == '__main__':
    Solution().solve()
