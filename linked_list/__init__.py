#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
class LinkedListBase(object):
    def __init__(self):
        self._head = None  # 头节点

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """ 遍历链表 """
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next
        print("")   # 换行

    def prepend(self, item):
        pass

    def append(self, item):
        pass

    def insert(self, index, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


from . import singly_linked_list
from . import double_linked_list
