#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description: 双向链表
from linked_list import LinkedListBase
from linked_list.node import DoubleLinkedListNode


class DoubleLinkedList(LinkedListBase):
    """ 双向链表 """
    def prepend(self, item):
        """ 头部添加元素 """
        node = DoubleLinkedListNode(item)
        if not self._head:
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        """ 尾部添加元素 """
        node = DoubleLinkedListNode(item)
        if not self._head:
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, index, item):
        node = DoubleLinkedListNode(item)
        if index == 0:
            self.prepend(item)
        elif index >= self.length():
            self.append(item)
        else:
            cur = self._head
            i = 0
            while i < index - 1:
                i += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node
            node.prev = cur

    def remove(self, item):
        cur = self._head
        pre = None
        while cur:
            if cur.item == item:
                if not pre:
                    self._head = None
                elif not cur.next:
                    pre.next = None
                else:
                    pre.next = cur.next
                    cur.next.prev = pre
            else:
                pre = cur
            cur = cur.next


if __name__ == '__main__':
    link_list = DoubleLinkedList()
    link_list.prepend(1)
    link_list.prepend(2)
    link_list.prepend(3)
    print(link_list.is_empty())
    link_list.travel()
    link_list.append(4)
    link_list.insert(2, 5)
    link_list.insert(0, 6)
    link_list.travel()
    # print(link_list.length())
    link_list.remove(5)
    link_list.travel()
    print(link_list.length())
    print(link_list.search(3))
    print(link_list.search(4))
