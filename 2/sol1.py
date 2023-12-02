MAX_AMTS = {
    'blue': 14,
    'green': 13,
    'red': 12,
}

def main():
    valid_sum = 0

    with open('input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split(':')
            invalid = False
            for game in parts[1].split(';'):
                for reveal in game.split(','):
                    reveal = reveal.strip()
                    reveal = reveal.split(' ')
                    if int(reveal[0]) > MAX_AMTS[reveal[1]]:
                        invalid = True
                        break

                if invalid:
                    break
            
            if not invalid:
                valid_sum += int(parts[0].split(' ')[1])


    print(valid_sum)

if __name__ == '__main__':
    main()
