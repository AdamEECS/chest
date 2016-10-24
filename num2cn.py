MAP = ('零', '一', '二', '三', '四', '五', '六', '七', '八', '九')
CARRY = ('', '十', '百', '千')
S4 = 10 ** 4
S8 = 10 ** 8
S16 = 10 ** 16
MIN = 0
MAX = 10 ** 16 - 1


def to_cn4(num):
    if num < 10:
        return MAP[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num /= 10
        lst.append(num)
        c = len(lst)
        result = ''

        for i, v in enumerate(lst):
            if v != 0:
                result += CARRY[i] + MAP[int(v)]
                if i < c - 1 and lst[i + 1] == 0:
                    result += '零'

        return result[::-1].replace('一十', '十')


def to_cn8(num):
    if num < S4:
        return to_cn4(num)
    else:
        mod = S4
        high, low = num // mod, num % mod
        if low == 0:
            return to_cn4(high) + '万'
        else:
            if low < S4 / 10:
                return to_cn4(high) + '万零' + to_cn4(low)
            else:
                return to_cn4(high) + '万' + to_cn4(low)


def to_cn16(num):
    mod = S8
    high, low = num // mod, num % mod
    if low == 0:
        return to_cn8(high) + '亿'
    else:
        if low < S8 / 10:
            return to_cn8(high) + '亿零' + to_cn8(low)
        else:
            return to_cn8(high) + '亿' + to_cn8(low)


def to_cn(num):
    if type(num) != int:
        return '{} is not a integer.'.format(num)
    if num < MIN or num > MAX:
        return '{} out of range[{}, {})'.format(num, MIN, MAX)

    if num < S4:
        return to_cn4(num)
    elif num < S8:
        return to_cn8(num)
    else:
        return to_cn16(num)


if __name__ == '__main__':
    print(to_cn(123456789999))
