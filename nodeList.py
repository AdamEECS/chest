#!/usr/bin/env python
# encoding=utf-8

"""
输入为两个list，数据结构如下面ListNode所示，输出为两链表对应位的和，例如：
l1: 3->4->2 l2: 3->6->4, output: 6->0->7
1. 每个节点只有一个非负整数
2. 超过10的向下一个节点进位
3. l1, l2可能不一样长, 对应节点没有的视为0
4. 下面给出基本测试用例，面试者需自行设计测试用例，保证代码无bug
TestCase：
1. l1: 1->1->1 l2: 2->2->2, output: 3->3->3
2: l1: 1->2->3 l2: 4->5,    output: 5->7->3
3: l1: 1       l2: 9->9,    output: 0->0->1
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        self._all = 'ListNode: ' + str(self.val)
        self._next = self.next
        while self._next is not None:
            self._all += '->' + str(self._next.val)
            self._next = self._next.next
        return self._all


class Solution(object):
    @staticmethod
    def to_do(l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        l3 = ListNode(0)
        pre = l3
        carry = 0
        while l1 is not None or l2 is not None or carry == 1:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            c = l1.val + l2.val + carry
            if c >= 10:
                carry = 1
                c -= 10
            else:
                carry = 0
            pre.val = c
            if l1.next is not None or l2.next is not None or carry == 1:
                pre.next = ListNode(0)
            pre = pre.next
            l1 = l1.next
            l2 = l2.next
        return l3


def test():
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)

    l2 = ListNode(2)
    l2.next = ListNode(2)
    l2.next.next = ListNode(2)

    l3 = ListNode(1)
    l3.next = ListNode(2)
    l3.next.next = ListNode(3)

    l4 = ListNode(4)
    l4.next = ListNode(5)

    l5 = ListNode(1)

    l6 = ListNode(9)
    l6.next = ListNode(9)

    l7 = ListNode(3)
    l7.next = ListNode(4)
    l7.next.next = ListNode(2)

    l8 = ListNode(3)
    l8.next = ListNode(6)
    l8.next.next = ListNode(4)

    l = [(l1, l2), (l3, l4), (l5, l6), (l7, l8)]

    for l1, l2 in l:
        print('l1:', l1)
        print('l2:', l2)
        l3 = Solution.to_do(l1, l2)
        print('l3:', l3)
        print('')


def main():
    test()


if __name__ == '__main__':
    main()
