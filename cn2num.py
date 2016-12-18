BASE = {
    '〇': 0,
    '一': 1,
    '二': 2,
    '三': 3,
    '四': 4,
    '五': 5,
    '六': 6,
    '七': 7,
    '八': 8,
    '九': 9,

    '零': 0,
    '壹': 1,
    '贰': 2,
    '叁': 3,
    '肆': 4,
    '伍': 5,
    '陆': 6,
    '柒': 7,
    '捌': 8,
    '玖': 9,

    '貮': 2,
    '两': 2,
}

CARRY = {
    '十': 10,
    '拾': 10,
    '百': 100,
    '佰': 100,
    '千': 1000,
    '仟': 1000,
    '万': 10000,
    '萬': 10000,
    '亿': 100000000,
    '億': 100000000,
    '兆': 1000000000000,
}

TRANS = {
    'w': 10000,
    'y': 100000000,
    'z': 1000000000000,
    10000: 'w',
    100000000: 'y',
    1000000000000: 'z',
}


def num_input(list_cn):
    unit = 0  # 当前的单位
    list_num = []  # 临时数组
    while list_cn:
        cn_item = list_cn.pop()
        if cn_item in CARRY:
            unit = CARRY.get(cn_item)
            if unit in (10000, 100000000, 1000000000000):
                list_num.append(TRANS.get(unit))
                unit = 1
            continue
        else:
            dig = BASE.get(cn_item)
            if unit:
                dig *= unit
                unit = 0
            list_num.append(dig)
    if unit == 10:  # 处理10-19的数字
        list_num.append(10)
    return list_num


def num_output(list_num):
    ret = 0
    tmp = 0
    while list_num:
        x = list_num.pop()
        if x in ('w', 'y', 'z'):
            tmp *= TRANS.get(x)
            ret += tmp
            tmp = 0
        else:
            tmp += x
    ret += tmp
    return ret


def cn2num(cn):
    list_cn = list(cn)
    list_num = num_input(list_cn)
    return num_output(list_num)


if __name__ == '__main__':
    test_dig = ['九',
                '十一',
                '一百二十三',
                '一千二百零三',
                '一万一千一百零一',
                '十万零三千六百零九',
                '一百二十三万四千五百六十七',
                '一千一百二十三万四千五百六十七',
                '一亿一千一百二十三万四千五百六十七',
                '一百零二亿五千零一万零一千零三十八',
                '一千一百一十一亿一千一百二十三万四千五百六十七',
                '一兆一千一百一十一亿一千一百二十三万四千五百六十七',
                ]

    for a in test_dig:
        print(cn2num(a))
