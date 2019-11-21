# 4.• 连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
#    • 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
def printStr(string):
    if len(string) <= 8:
        print(string + "0" * (8 - len(string)))
    else:
        while len(string) > 8:
            print(string[:8])
            string = string[8:]
        print(string + "0" * (8 - len(string)))


a = input()
b = input()
printStr(a)
printStr(b)
############################################################################################################
# 5.写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）
# while True:
#     try:
#         print(int(input(),16))
#     except:
#         break

import sys
for line in sys.stdin:
    print(int(line,16))
############################################################################################################
# 6.功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）,最后一个数后面也要有空格
a=int(input())
def q(x):
    iszhi=1
    for i in range(2,int(x**0.5+2)):
        if x%i==0:
            iszhi=0
            print(str(i),end=" ")
            q(int(x/i))
            break
    if iszhi==1:
        print(str(x),end=" ")
q(a)
