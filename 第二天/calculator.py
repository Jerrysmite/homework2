# 使用说明：须在程序同一目录下放置名为“test.txt”的文件，文件内为需要计算的式子
# 格式为“1 + 1”

import re
file = open('test.txt', 'r')
content = file.read()
string = content
a = []
a = re.findall("\d+\.?\d*", string)
a = list(map(int,a))
num1 = a[0]
num2 = a[1]
if '+' in string :
    print("result=")
    print(num1+num2)
if  '-' in string :
    print("result=")
    print(num1-num2)
if '*' in string :
    print("result=")
    print(num1*num2)
if '/' in string :
    print("result=")
    print(num1/num2)
