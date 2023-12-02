def main():
    sum_of_powers = 0

    with open('input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            min_green = -float('INF')
            min_blue = -float('INF')
            min_red = -float('INF')
            parts = line.split(':')
            for game in parts[1].split(';'):
                for reveal in game.split(','):
                    reveal = reveal.strip()
                    reveal = reveal.split(' ')

                    if reveal[1] == 'blue':
                        min_blue = max(min_blue, int(reveal[0]))
                    elif reveal[1] == 'green':
                        min_green = max(min_green, int(reveal[0]))
                    elif reveal[1] == 'red':
                        min_red = max(min_red, int(reveal[0]))

            sum_of_powers += min_red * min_green * min_blue

    print(sum_of_powers)

if __name__ == '__main__':
    main()
