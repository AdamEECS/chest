import random

obj = {
    'a': 2,
    'b': 3,
    'c': 5,
}


def choice(d):
    return random.choice(''.join([k * v for k, v in d.items()]))


if __name__ == '__main__':
    for i in range(10):
        print(choice(obj))
