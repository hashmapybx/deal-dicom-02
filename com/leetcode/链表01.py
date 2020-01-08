# -*- coding: utf-8 -*-
"""
Create Time: 2019/11/27 上午10:42
Author: ybx
"""

'''
先定义一个链表结构

'''

class ListNode(object):
    # 这个是单向链表
    def __init__(self, val):
        self.val = val
        self.next = None # 指定

    def __str__(self):
        return str(self.val)

class Solution(object):
    def reverserList(self, head: ListNode) -> ListNode:
        '''
        翻转链表的操作 迭代前节点prev   缓存当前节点current的下一个节点  把当前节点的.next指向prev
        :param head:
        :return:
        '''

        current = head
        prev = None
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev

    # 翻转的方法二
    def reverse2(self, head:ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            current.next, prev, current = prev, current, current.next
        return prev

    def sum(self, m:int, n:int) -> int:
        return m+n

    # 判断链表里面是否有环 设置快慢指针 慢指针每次移动一个位置 快指针每次移动两个位置 如果是存在环的那么肯定是会相遇的
    def hasCircle(self, head:ListNode) -> bool:
        slow = fast = head

        while slow and fast and head.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


    # 如何找到链表中的入环节点呢?
    def detectCycle(self, head: ListNode) ->  ListNode:
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                first_meet = head
                while slow!= first_meet:
                    slow = slow.next
                    first_meet = first_meet.next
                return first_meet
        return None



if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)

    s = Solution()
    res = s.sum(1,2)
    print(res)

    # 翻转链表结构操作
    res2 = s.reverse2(a)
    print(res2)
    print(res2.next)
    print(res2.next.next)


