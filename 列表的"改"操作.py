
"""列表的"改"操作"""

"""
    如果想要修改列表中的元素，有两种常见的方式：
一、为指定索引的元素赋予一个新值（一次只修改一个元素）
    《图解Python》
"""
L = [3, 4, 5, 6, 7]

L[2] = 8
print(L)        # [3, 4, 8, 6, 7]

"""
二、为指定的切片赋予一个新值（一次至少修改一个元素）
"""
L[1:4] = [1, 9, 2]
# L[1:4] = (1, 9, 2)    # 等号右边也可以是元组
print(L)        # [3, 1, 9, 2, 7]

L[1:2] = [5]    # [3, 5, 9, 2, 7]
print(L)
"""
    等号左右的元素个数可以不同。
    此时，列表中其它元素的索引也会随之改变。
"""
L[1:4] = [1, 8]
print(L)        # [3, 1, 8, 7]
