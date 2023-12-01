SPELLED_DIGITS = [
    'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine',
]
VALUES = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
    'nine': 9,
}

def is_digit_or_spelled(word):
    if word[0].isdigit():
        return True
    for sd in SPELLED_DIGITS:
        if word.startswith(sd):
            return True
    return False

def to_value(word):
    if word[0].isdigit():
        return word[0]
    for sd in SPELLED_DIGITS:
        if word.startswith(sd):
            return str(VALUES[sd])
        
    raise ValueError('Not a digit or spelled digit')

def main():
    sum_calibration = 0

    with open('input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            left = 0
            right = len(line) - 1

            while not is_digit_or_spelled(line[left:]):
                left += 1
            while not is_digit_or_spelled(line[right:]):
                right -= 1

            sum_calibration += int(to_value(line[left:]) + to_value(line[right:]))

    print(sum_calibration)

if __name__ == '__main__':
    main()
