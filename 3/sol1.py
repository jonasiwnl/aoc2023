def main():
    sum_of_parts = 0

    grid = []

    with open('input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line)

        r, c = len(grid), len(grid[0])

        for y, row in enumerate(grid):
            num_buffer = ''
            num_buffer_start = 0
            for x, ch in enumerate(row + '.'):
                if x < c and ch.isnumeric():
                    if num_buffer:
                        num_buffer += ch
                    else:
                        num_buffer = ch
                        num_buffer_start = x
                else:
                    if num_buffer:
                        valid = False
                        for cx in range(num_buffer_start - 1, x + 1):
                            for cy in range(y - 1, y + 2):
                                if cx >= 0 and cx < c and cy >= 0 and cy < r and \
                                    not grid[cy][cx].isalnum() and \
                                    not grid[cy][cx] == '.' and not grid[cy][cx] == '\n':

                                    valid = True

                        if valid:
                            sum_of_parts += int(num_buffer)
                    num_buffer = ''

    print(sum_of_parts)

if __name__ == '__main__':
    main()
