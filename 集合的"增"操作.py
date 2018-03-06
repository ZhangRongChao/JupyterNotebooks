
"""集合的"增"操作"""

"""
    如果想要往集合中添加元素，常见的方式有两种：
（1）调用方法add（一次只添加一个元素）
"""
s = {3, 4, 5, 6, 7}
s.add(8)
print(s)    # {4, 3, 5, 7, 6, 8}
"""
    集合中已经存在的元素不会被添加。
"""
s.add(8)
print(s)    # {4, 3, 5, 7, 6, 8}

"""
（2）调用方法update（一次至少添加一个元素）
"""
s = {3, 4, 5, 6, 7}
s.update({2, 8})
# s.update([2, 8])
# s.update((2, 8))
print(s)    # {4, 3, 5, 2, 8, 7, 6}
"""
    集合中已经存在的元素不会被添加。
"""
s.update({2, 8})
print(s)    # {4, 3, 5, 2, 8, 7, 6}
