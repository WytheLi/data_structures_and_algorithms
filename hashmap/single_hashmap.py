#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : willi
# @Email   : willi168@163.com
# @Description: Hashmap | 链表散列
import hashlib
import six


class SimpleHashMap(object):
    """
    使用“链地址法”的结构，实现一个简单的hash_map
    实现了__setitem__、 __getitem__方法，使我们的对象也可像dict一样进行添加、读取

    """
    def __init__(self, length=10):
        self.length = length
        self.items_x = [[] for i in range(self.length)]

    def _safe_data(self, data):
        """
        格式化data
        将data转换二进制格式输出
        :param data:
        :return:
        """
        # python3、python2版本兼容
        if six.PY3:
            if isinstance(data, bytes):
                return data
            elif isinstance(data, str):
                return data.encode()
            else:
                raise Exception("data type error, is string or bytes")
        else:
            if isinstance(data, str):
                return data
            elif isinstance(data, unicode):
                return data.encode()
            else:
                raise Exception("data type error, is string or bytes")

    def _get_hash_value(self, data):
        hash_obj = hashlib.md5()
        hash_obj.update(self._safe_data(data))
        hash_value = hash_obj.hexdigest()
        return hash_value

    def _hash(self, key):
        """
        计算该key在items哪个list中
        :param key:
        :return:
        """
        if isinstance(key, str):
            hash_value = self._get_hash_value(key)
            return int(hash_value, 16) % self.length
        elif isinstance(key, int):
            return key % self.length
        else:
            raise Exception("data type error, is string or int")

    def _exists(self, key1, key2):
        """
        比较两个key是否相等
        该处key值为str|int型（不可变数据类型）时的比对
        针对不同类型的key需重新实现
        :param key1:
        :param key2:
        :return:
        """
        return key1 == key2

    def _insert(self, key, value):
        index = self._hash(key)
        if self.items_x[index]:
            for item in self.items_x[index]:
                if self._exists(key, item[0]):
                    # 存在key，更新value
                    self.items_x[index].remove(item)
                    break
        self.items_x[index].append((key, value))
        return True

    def _get(self, key):
        index = self._hash(key)
        if self.items_x[index]:
            for item in self.items_x[index]:
                if self._exists(key, item[0]):
                    return item[1]
        # 不存在key, 则抛出KeyError异常
        raise KeyError

    def __setitem__(self, key, value):
        return self._insert(key, value)

    def __getitem__(self, key):
        return self._get(key)


if __name__ == '__main__':
    hash_map = SimpleHashMap()
    hash_map[1] = 30000
    hash_map['dljajfkdahfkaddjafkjadfkjas'] = 'aaa'
    print(hash_map.items_x)
    print(hash_map[1])
