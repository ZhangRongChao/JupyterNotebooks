
"""函数的调用之实参的传递"""

"""
    前面的课程中学习过："变量相当于标签。对于赋值语句: 变量 = 对象，相当于给对象贴了一个标签，
标签名就是变量名。"
    调用函数时把实参传递给形参从而用实参初始化形参，本质上执行了赋值语句：形参 = 实参对象，
相当于给实参对象贴了一个标签，标签名就是形参名。
    如果实参对象是可变类型，在函数体内对形参对象的任何修改其实就是对实参对象的修改。
"""
def f(arg1, arg2):
    print('初始化形参后：arg1 =', arg1, 'arg2 =', arg2)
    arg1 = arg1 * 2
    arg2.append(4)
    print('修改形参后：arg1 =', arg1, 'arg2 =', arg2)

i = 10
L = [1, 2, 3]
print('调用函数前：i =', i, 'L =', L) # 调用函数前：i = 10 L = [1, 2, 3]

f(i, L)
# 初始化形参后：arg1 = 10 arg2 = [1, 2, 3]
# 修改形参后：arg1 = 20 arg2 = [1, 2, 3, 4]

print('调用函数后：i =', i, 'L =', L) # 调用函数后：i = 10 L = [1, 2, 3, 4]

"""
    《图解Python》

    当实参对象是可变类型时，如果希望在函数体内对形参对象的任何修改不影响实参对象，
可以在调用函数时传递实参对象的值拷贝。
"""
i = 10
L = [1, 2, 3]
print('调用函数前：i =', i, 'L =', L) # 调用函数前：i = 10 L = [1, 2, 3]

f(i, L[:])
# 初始化形参后：arg1 = 10 arg2 = [1, 2, 3]
# 改形参后：arg1 = 20 arg2 = [1, 2, 3, 4]

print('调用函数后：i =', i, 'L =', L) # 调用函数后：i = 10 L = [1, 2, 3]

"""
    《图解Python》
"""
