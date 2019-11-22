# 15.输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
a=int(input())
print(bin(a).replace("0b","").count("1"))
############################################################################################################
# 16.正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。
def gcd(a, b):
    """最大公约数."""
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    """最小公倍数."""
    return a * b // gcd(a, b)  #//表示整数除法
while True:
    try:
        a,b=map(int,input().split())
        print(lcm(a,b))
    except:
        break
############################################################################################################
# 开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
import re
while True:
    try:
        ss = input().split(';')
        x=0
        y=0
        for i in ss:
            a = re.match(r'^([ADWS])(\d+)$',i)
            if a:
                if a.group(1) == 'A':
                    x-=int(a.group(2))
                if a.group(1) == 'W':
                    y += int(a.group(2))
                if a.group(1) == 'D':
                    x+=int(a.group(2))
                if a.group(1) == 'S':
                    y-=int(a.group(2))
        print("{},{}".format(x,y))
    except:
        break
############################################################################################################
# 19.从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值
a=input().split()
fu=[]
zheng=[]
for i in a:
    if int(i)<0:
        fu.append(int(i))
    else:
        zheng.append(int(i))
print(len(fu))
print(round(sum(zheng)/len(zheng),1))
############################################################################################################
# 20.Redraiment是走梅花桩的高手。Redraiment总是起点不限，从前到后，往高的桩子走，但走的步数最多，不知道为什么？你能替Redraiment研究他最多走的步数吗
# 最长上升子序列
import bisect

while True:
    try:
        a, b = int(input()), map(int, input().split())
        q = []
        for v in b:
            pos = bisect.bisect_left(q, v)
            if pos == len(q):
                q.append(v)
            else:
                q[pos] = v
        print(len(q))

    except:
        break
############################################################################################################
# 21.输入一个字符串，对字符中的各个英文字符，数字，空格进行统计（可反复调用）按照统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASII码由小到大排序输出
while True:
    try:
        from collections import defaultdict

        dd, s, res = defaultdict(list), input(), ""
        for i in set(s):
            dd[s.count(i)].append(i)
        for i in sorted(dd.keys(), reverse=True):
            res += "".join(sorted(dd[i], key=ord))
        print(res)

    except:
        break
############################################################################################################
# 22.输入整型数组和排序标识，对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）
############################################################################################################
while True:
    try:
        a=int(input())
        b=map(int,input().split())
        c=int(input())
        if c==0:
            print(" ".join(map(str,sorted(b,reverse=False))))
        if c==1:
            print(" ".join(map(str,sorted(b,reverse=True))))
    except:
        break
############################################################################################################
# 23.功能:等差数列 2，5，8，11，14。。。。
#
# 输入:正整数N >0
#
# 输出:求等差数列前N项和
while True:
    try:
        a = int(input())
        print(3 * a * (a - 1) // 2 + 2*a)
    except:
        break
############################################################################################################
# 24.自守数是指一个数的平方的尾数等于该数自身的自然数。例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n以内的自守数的个数
while True:
    try:
        a, res = int(input()), 0
        for i in range(0, a + 1):
            if str(i ** 2).endswith(str(i)):
                res += 1
        print(res)
    except:
        break
############################################################################################################
# 26.首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。
while True:
    try:
        a, nums, pos, neg = int(input()), map(int, input().split()), [], 0
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg += 1
        print(str(neg) + " 0" if not pos else str(neg) + " " + "{0:.1f}".format(sum(pos) / len(pos)))

    except:
        break
