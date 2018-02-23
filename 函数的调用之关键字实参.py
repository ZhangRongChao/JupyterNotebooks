
"""函数的调用之关键字实参"""

"""
    调用函数时，传递的实参的形式可以为："形参名=实参值"，从而用指定的实参值初始化指定名称的形参，
这样的实参称为关键字实参。
"""
def f(a, b, c):
    print('a =', a, 'b =', b, 'c =', c)

f(a = 2, b = 5, c = 8)  # a = 2 b = 5 c = 8

"""
    《图解Python》
"""

"""
    由于关键字实参中指定了形参名，所以实参和形参的匹配关系更加清晰，而且每个关键字实参
在所有关键字实参中的位置可以是任意的。
"""
f(b = 5, c = 8, a = 2)  # a = 2 b = 5 c = 8

"""
    《图解Python》
"""

f(c = 8, b = 5, a = 2)  # a = 2 b = 5 c = 8

"""
    调用函数时，可以组合使用位置实参和关键字实参。但是，位置实参必须位于关键字实参之前。
否则，无法根据位置来匹配位置实参和对应的形参。
"""
f(2, 5, c = 8)      # a = 2 b = 5 c = 8
# f(2, c = 8, 5)    # Positional argument after keyword argument
