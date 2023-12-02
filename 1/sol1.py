def main():
    sum_calibration = 0

    with open('input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            left = 0
            right = len(line) - 1

            while not line[left].isdigit():
                left += 1
            while not line[right].isdigit():
                right -= 1

            sum_calibration += int(line[left] + line[right])

    print(sum_calibration)

if __name__ == '__main__':
    main()
