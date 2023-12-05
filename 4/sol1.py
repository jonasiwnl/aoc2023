def main():
    sum_points = 0

    with open('input', 'r') as f:
        lines = f.readlines()

        winners = set()
        for line in lines:
            if line == '\n':
              break

            parts = line.split('|')
            for n in parts[0].split(':')[1].split():
                if n.isnumeric():
                    winners.add(n)

            points = 0
            for n in parts[1].split():
                if n in winners:
                    if points == 0:
                        points = 1 
                    else:
                        points *= 2

            sum_points += points
            winners.clear()

    print(sum_points)

if __name__ == '__main__':
    main()
