SPELLED_DIGITS = {
    'o': {
        'n': {
            'e': {
                '#': '1', 
            },
        },
    },
    't': {
        'w': {
            'o': {
                '#': '2',
            },
        },
        'h': {
            'r': {
                'e': {
                    'e': {
                        '#': '3',
                    },
                },
            },
        },
    },
    'f': {
        'o': {
            'u': {
                'r': {
                    '#': '4',
                },
            },
        },
        'i': {
            'v': {
                'e': {
                    '#': '5',
                },
            },
        },
    },
    's': {
        'i': {
            'x': {
                '#': '6',
            },
        },
        'e': {
            'v': {
                'e': {
                    'n': {
                        '#': '7',
                    },
                },
            },
        },
    },
    'e': {
        'i': {
            'g': {
                'h': {
                    't': {
                        '#': '8',
                    },
                },
            },
        },
    },
    'n': {
        'i': {
            'n': {
                'e': {
                    '#': '9',
                },
            },
        },
    },
}

def find_value(word: str, left: bool) -> str:
    i = 0 if left else len(word) - 1
    while True:
        if word[i].isdigit():
            return word[i]
        
        trie = SPELLED_DIGITS
        j = i
        while j < len(word) and word[j] in trie:
            trie = trie[word[j]]
            if '#' in trie: return trie['#']
            j += 1

        i += 1 if left else -1

def main():
    sum_calibration = 0

    with open('input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            sum_calibration += int(find_value(line, True) + find_value(line, False))

    print(sum_calibration)

if __name__ == '__main__':
    main()

