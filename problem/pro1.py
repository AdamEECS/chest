def func1():
    from itertools import permutations
    import json
    l = [0, 1, 2, 3]
    r = ['{}{}{}'.format(a, b, c) for a, b, c in permutations(l, 3)]
    print(json.dumps(r, indent=4))


def func2(length=6):
    import random
    a = [chr(i) for i in range(97, 97 + 26)]
    b = [chr(i) for i in range(65, 65 + 26)]
    c = [chr(i) for i in range(48, 48 + 10)]
    d = [chr(i) for i in range(33, 33 + 15)]
    e = [a, b, c, d]
    f = list(map(random.choice, e))
    while len(f) < length:
        f.append(random.choice(random.choice(e)))
    random.shuffle(f)
    f = ''.join(f)
    print(f)


def func3():
    import random
    s = ' '.join([str(random.randint(0, 9)) for i in range(100)])
    print(s)
    with open('test.txt', 'w+') as f:
        f.write(s)

if __name__ == '__main__':
    func1()
    func2(10)
    func3()
