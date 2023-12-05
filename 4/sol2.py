def main():
    scratchcards = 0

    with open('input', 'r') as f:
        lines = f.readlines()
        copies = [1 for _ in range(len(lines))]

        winners = set()
        for i, line in enumerate(lines):
            if line == '\n':
              break

            scratchcards += copies[i]

            parts = line.split('|')
            for n in parts[0].split(':')[1].split():
                if n.isnumeric():
                    winners.add(n)

            matches = 0
            for n in parts[1].split():
                if n in winners:
                    matches += 1

            for j in range(i + 1, i + 1 + matches):
                copies[j] += copies[i]

            winners.clear()

    print(scratchcards)

if __name__ == '__main__':
    main()
