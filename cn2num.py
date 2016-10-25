CN_NUM = {
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
CN_UNIT = {
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


def cn2dig(cn):
    lcn = list(cn)
    unit = 0  # 当前的单位
    ldig = []  # 临时数组

    while lcn:
        cndig = lcn.pop()

        if cndig in CN_UNIT:
            unit = CN_UNIT.get(cndig)
            if unit == 10000:
                ldig.append('w')  # 标示万位
                unit = 1
            elif unit == 100000000:
                ldig.append('y')  # 标示亿位
                unit = 1
            elif unit == 1000000000000:  # 标示兆位
                ldig.append('z')
                unit = 1

            continue

        else:
            dig = CN_NUM.get(cndig)

            if unit:
                dig *= unit
                unit = 0

            ldig.append(dig)


    if unit == 10:  # 处理10-19的数字
        ldig.append(10)


    ret = 0
    tmp = 0
    print(ldig)
    while ldig:
        x = ldig.pop()

        if x == 'w':
            tmp *= 10000
            ret += tmp
            tmp = 0

        elif x == 'y':
            tmp *= 100000000
            ret += tmp
            tmp = 0

        elif x == 'z':
            tmp *= 1000000000000
            ret += tmp
            tmp = 0

        else:
            tmp += x

    ret += tmp
    return ret

    # ldig.reverse()
    # print ldig
    # print CN_NUM[u'七']


if __name__ == '__main__':
    print(cn2dig('一万一千一百零一'))
    # test_dig = ['九',
    #             '十一',
    #             '一百二十三',
    #             '一千二百零三',
    #             '一万一千一百零一',
    #             '十万零三千六百零九',
    #             '一百二十三万四千五百六十七',
    #             '一千一百二十三万四千五百六十七',
    #             '一亿一千一百二十三万四千五百六十七',
    #             '一百零二亿五千零一万零一千零三十八',
    #             '一千一百一十一亿一千一百二十三万四千五百六十七',
    #             '一兆一千一百一十一亿一千一百二十三万四千五百六十七',
    #             ]
    #
    # for a in test_dig:
    #     print(cn2dig(a))
