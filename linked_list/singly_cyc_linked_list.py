#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description: 单向循环链表
from linked_list import LinkedListBase
from linked_list.node import SinglyLinkedListNode


class SinglyCycLinkedList(LinkedListBase):
    """ 单向循环链表 """
    def length(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur is self._head:
                break
        return count

    def travel(self):
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next
            if cur is self._head:
                break
        print("")

    def prepend(self, item):
        node = SinglyLinkedListNode(item)
        if self.is_empty():
            self._head = node
            self._head.next = self._head
        else:
            node.next = self._head
            cur = self._head
            while cur:
                cur = cur.next
                if cur.next is self._head:
                    break
            cur.next = node
            self._head = node
            # node.next = self._head
            # cur = self._head
            # while cur.next is not self._head:
            #     cur = cur.next
            # cur.next = node
            # self._head = node

    def append(self, item):
        node = SinglyLinkedListNode(item)
        if not self._head:
            self._head = node
        else:
            node.next = self._head
            if not self._head.next:
                self._head.next = node
            else:
                cur = self._head
                while cur:
                    cur = cur.next
                    if cur.next is self._head:
                        break
                cur.next = node

    def insert(self, index, item):
        if index == 0:
            self.prepend(item)
        elif index >= self.length():
            self.append(item)
        else:
            node = SinglyLinkedListNode(item)
            cur = self._head
            i = 0
            while i < index - 1:  # 遍历获取索引位置的前一个节点
                i += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur:
            if cur.item == item:
                if not pre:     # 删除第一个
                    _cur = cur  # 移动游标，检索最后一个节点
                    while _cur:
                        _cur = _cur.next
                        if _cur.next is self._head:
                            break
                    _cur.next = cur.next
                    self._head = cur.next
                else:
                    pre.next = cur.next
                    pre = cur
                    # break     # 这里通过循环终止，只删除满足条件索引最小的节点
            else:
                pre = cur
            cur = cur.next
            if cur.next is self._head:
                break

    def search(self, item):
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
            if cur.next is self._head:
                break
        return False


if __name__ == '__main__':
    link_list = SinglyCycLinkedList()
    link_list.prepend(1)
    link_list.prepend(2)
    link_list.prepend(3)
    link_list.prepend(4)
    # print(link_list.length())
    link_list.travel()
    link_list.append(6)
    link_list.append(7)
    link_list.insert(2, 8)
    link_list.insert(0, 9)
    link_list.travel()
    # print(link_list.length())
    # link_list.remove(5)
    link_list.remove(9)
    link_list.remove(3)
    link_list.travel()
    print(link_list.length())
    print(link_list.search(3))
    print(link_list.search(4))