#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description: 单向链表（单链表）
from linked_list import LinkedListBase
from linked_list.node import SinglyLinkedListNode


class SinglyLinkedList(LinkedListBase):
    """ 单向链表 """
    def prepend(self, item):
        """ 在单链表头部添加元素 """
        node = SinglyLinkedListNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """ 在单链表尾部添加元素 """
        node = SinglyLinkedListNode(item)
        # 判断是否为空链表
        if not self._head:
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """ 指定位置添加元素 """
        if index == 0:
            self.prepend(item)
        elif index >= self.length():
            self.append(item)
        else:
            node = SinglyLinkedListNode(item)
            cur = self._head
            i = 0
            while i < index - 1:   # 遍历获取索引位置的前一个节点
                i += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """ 删除指定值的所有节点 """
        cur = self._head
        pre = None  # 游标所指当前节点的上一个节点
        while cur:
            if cur.item == item:
                if not pre:     # 表示第一个节点
                    self._head = cur.next
                else:
                    pre.next = cur.next
                # break     # 这里通过循环终止，只删除满足条件索引最小的节点
            else:
                pre = cur
            cur = cur.next


if __name__ == '__main__':
    link_list = SinglyLinkedList()
    link_list.prepend(1)
    link_list.prepend(2)
    link_list.prepend(3)
    print(link_list.is_empty())
    link_list.travel()
    link_list.append(4)
    link_list.insert(2, 5)
    link_list.insert(0, 6)
    link_list.travel()
    link_list.remove(5)
    link_list.travel()
    print(link_list.length())
    print(link_list.search(3))
    print(link_list.search(4))
