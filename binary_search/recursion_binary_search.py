#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description: 递归实现二分查找
def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
          return True
        else:
          if item<alist[midpoint]:
            return binary_search(alist[:midpoint],item)
          else:
            return binary_search(alist[midpoint+1:],item)


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binary_search(testlist, 3))
    print(binary_search(testlist, 13))