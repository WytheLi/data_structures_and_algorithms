#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description:
class SinglyLinkedListNode(object):
    """ 单链表节点 """
    def __init__(self, item):
        self.item = item    # 表元素
        self.next = None    # 下个节点链接域



class DoubleLinkedListNode(object):
    """ 双向链表节点 """
    def __init__(self, item):
        self.item = item
        self.next = None    # 前驱
        self.prev = None    # 后继