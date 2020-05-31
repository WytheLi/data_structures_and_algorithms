#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description: 栈可以用顺序表实现，也可以用链表实现
class Stack(object):
    """ 栈 """
    def __init__(self):
        self.items = []     # 此处用顺序表实现

    def is_empty(self):
        return self.items is []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
        """ 查看栈顶元素 """
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
