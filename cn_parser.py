import cn2num
import num2cn


def log(*args):
    print(*args)


class Stack(object):
    def __init__(self):
        self.array = []

    def push(self, element):
        self.array.append(element)

    def pop(self):
        n = self.array[-1]
        del self.array[-1]
        return n

    def pop_all(self):
        l = []
        while self.array:
            l.append(self.array.pop())
        return l

    def pop_limit(self, delimiter='['):
        l = []
        while self.array[-1] != delimiter:
            l.append(self.pop())
        l.reverse()
        self.pop()
        return l


def parsed_ast(tokens):
    s = Stack()
    for i in tokens:
        if i == '】':
            l = s.pop_limit(delimiter='【')
            s.push(l)
            continue
        s.push(i)
    return s.array[0]


def mut(l):
    s = 1
    for i in l:
        s *= i
    return s


def apply(op, oprands):
    if op == '加':
        return sum(oprands)
    elif op == '减':
        return oprands[0] - sum(oprands[1:])
    elif op == '乘':
        return mut(oprands)
    elif op == '除':
        return oprands[0] / mut(oprands[1:])
    else:
        return '操作符错误！'


def apply_all(expression):
    for i, exp in enumerate(expression):
        if type(exp) == list:
            expression[i] = apply_all(exp)
    if expression[0] in ['加', '减', '乘', '除']:
        return apply(expression[0], expression[1:])


keywords = ['加', '减', '乘', '除', '【', '】']


def main():
    tokens_str = input('听候调遣>>>')
    tokens = tokens_str.split(' ')
    tokens_inted = []
    for i in tokens:
        if i in keywords:
            tokens_inted.append(i)
        else:
            tokens_inted.append(cn2num.cn2num(i))
    parsed_tokens = parsed_ast(tokens_inted)
    result = apply_all(parsed_tokens)
    log('等于：', num2cn.to_cn(result))


if __name__ == '__main__':
    while True:
        main()
