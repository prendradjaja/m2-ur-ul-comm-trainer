import random
from string import ascii_uppercase
from minus import minus

# todo: Doesn't just have to be a choice(LEFT) + choice(RIGHT) thing. you can also have targets in the M slice

LEFT = 'DLXR'
RIGHT = 'BJVT'

def main():
    while True:
        left = random.choice(LEFT)
        right = random.choice(RIGHT)
        letters = [left, right]
        random.shuffle(letters)
        pair = ''.join(letters)
        input(pair)

if __name__ == '__main__':
    main()
