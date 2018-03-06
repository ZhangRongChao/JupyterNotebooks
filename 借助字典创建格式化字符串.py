
"""借助字典创建格式化字符串"""

"""
一、使用百分号作为占位符
    《图解Python》
"""
phonebook = {'张三': '13333333333',
             '李四': '14444444444',
             '王五': '15555555555',
             '赵六': '16666666666'}
# 王五的号码：15555555555，张三的号码：13333333333
print('王五的号码：%s，张三的号码：%s' % (phonebook['王五'], phonebook['张三']))
"""
    当字符串中的占位符是百分号，并且占位符对应的实际值来自某个字典的value时，可以把所有的实际值
改写为字典，同时根据字典的value对应的key在占位符%的后面添加：(字典的key)。其中，
字典的key会被添加一对引号，因此，如果字典的key是字符串，需要去掉字典的key自带的引号。
"""
# 王五的号码：15555555555，张三的号码：13333333333
print('王五的号码：%(王五)s，张三的号码：%(张三)s' % phonebook)

price = 68.88
book = '《数据结构与算法》'
print(vars())
print('花了%(price).2f，买了一本书：%(book)s' % vars())

"""
二、调用方法format_map并使用花括号作为占位符
    《图解Python》
"""
phonebook = {'张三': '13333333333',
             '李四': '14444444444',
             '王五': '15555555555',
             '赵六': '16666666666'}
# 王五的号码：15555555555，张三的号码：13333333333
print('王五的号码：{}，张三的号码：{}'.format(phonebook['王五'], phonebook['张三']))
"""
    当字符串中的占位符是花括号，并且占位符对应的实际值来自某个字典的value时，可以调用方法format_map
并把该字典直接作为方法的参数，同时根据字典的value在花括号中指定对应的key：{字典的key}。其中，
字典的key会被添加一对引号，因此，如果字典的key是字符串，需要去掉字典的key自带的引号。
"""
# 王五的号码：15555555555，张三的号码：13333333333
print('王五的号码：{王五}，张三的号码：{张三}'.format_map(phonebook))


data = {'title': '我的主页', 'text': '欢迎来到我的主页!'}

template = '''
<html>
    <head>
        <title>{title}</title>
    </head>
    
    <body>
        <h1>{title}</h1>
        <p>{text}</p>
    </body>
</html>
'''

print(template.format_map(data))
"""
<html>
    <head>
        <title>我的主页</title>
    </head>
    
    <body>
        <h1>我的主页</h1>
        <p>欢迎来到我的主页!</p>
    </body>
</html>
"""
