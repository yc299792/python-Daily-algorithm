# 57.输入一个整数,计算整数二进制中1的个数
# 注：当出现错误时，添加while true  try except试试
while True:
    try:
        a=int(input())
        print(bin(a).count("1"))
    except:
        break
############################################################################################################
# 58.一个DNA序列由A/C/G/T四个字母的排列组合组成。G和C的比例（定义为GC-Ratio）是序列中G和C两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，这个比例非常重要。因为高的GC-Ratio可能是基因的起始点。
# 给定一个很长的DNA序列，以及要求的最小子序列长度，研究人员经常会需要在其中找出GC-Ratio最高的子序列。
while True:
    try:
        a, b = input(), int(input())
        maxStr, maxCnt = a[:b], a[:b].count("C") + a[:b].count("G")
        for i in range(0, len(a) - b):
            if a[i:i + b].count("C") + a[i:i + b].count("G") > maxCnt:
                maxCnt = a[i:i + b].count("C") + a[i:i + b].count("G")
                maxStr = a[i:i + b]
        print(maxStr)
    except:
        break
############################################################################################################
# 59.输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
while True:
    try:
        a=input()
        char,space,number,other=0,0,0,0
        for i in a:
            if i==" ":space+=1
            elif i.isnumeric():
                number+=1
            elif i.isalpha():char+=1
            else:other+=1
        print(char)
        print(space)
        print(number)
        print(other)
    except:
        break
############################################################################################################
# 60.字符串排序
while True:
    try:
        a = input()
        # res是最终返回的字符串的列表形式，char是提取的英文字母。
        res, char = [False] * len(a), []
        # 经过这个循环，把相应的非英文字母及其位置存储到了res中。并且把英文字母提取出来了。
        for i, v in enumerate(a):
            if v.isalpha():
                char.append(v)
            else:
                res[i] = v
        # 使用lambda表达式排序，暴力有效。
        char.sort(key=lambda c: c.lower())
        # 将char中对应的字符填到res中。
        for i, v in enumerate(res):
            if not v:
                res[i] = char[0]
                char.pop(0)
        print("".join(res))
    except:
        break
############################################################################################################
# 61.有一只兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，问每个月的兔子总数为多少？
#第一个月一只，第二个月一只，第三个月两只。然后符合且波纳契数列
while True:
    try:
        a=int(input())
        arr=[1,1]
        while len(arr)<a:
            arr.append(arr[-1]+arr[-2])
        print(arr[-1])
    except:
        break
############################################################################################################
# 62.有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？
# 注：通过数学分析，最后获得的饮料数是总空瓶数整除2 。
while True:
    try:
        a = int(input())
        if a != 0:
            print(a // 2)

    except:
        break
############################################################################################################
# 63.密码验证合格:
## 1.长度超过8位
## 2.包括大小写字母.数字.其它符号,以上四种至少三种
# 3.不能有相同长度超2的子串重复
# 注： re.findall 的简单用法（返回string中所有与pattern相匹配的全部字串，返回形式为数组）
import re
import sys
for i in sys.stdin.readlines():
    print("OK" if len(i.strip())>8 and sum([1 if re.search(r"[A-Z]",i.strip()) else 0,1 if re.search(r"[a-z]",i.strip()) else 0,1 if re.search(r"[0-9]",i.strip()) else 0,1 if re.search(r"[^0-9a-zA-Z]",i.strip()) else 0])>2 and sum(map(lambda c:i.strip().count(i.strip()[c:c+3])>1,range(1,len(i.strip())-3)))==0 else "NG")
############################################################################################################
# 64.简单密码破解
# 他是这么变换的，大家都知道手机上的字母： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，

d = {
    "abc": 2,
    "def": 3,
    "ghi": 4,
    "jkl": 5,
    "mno": 6,
    "pqrs": 7,
    "tuv": 8,
    "wxyz": 9,

}
while True:
    try:
        a, res = input(), ""
        for i in a:
            if i.isupper():
                if i != "Z":
                    res += chr(ord(i.lower()) + 1)
                else:
                    res += "a"
            elif i.islower():
                for j in d.keys():
                    if i in j:
                        res += str(d[j])
                        break
            else:
                res += i
        print(res)

    except:
        break
############################################################################################################
# 65.计算最少出列多少位同学，使得剩下的同学排成合唱队形
# 算法：动态规划
# 用到概念：递增子序列
# -*- coding:utf-8 -*-
def middle(b, target):  # b为排序数组，所以能进行二分查找，pos返回当前的target在b数组中是第几大的数，也就是前面有多少是有序的
    low = 0
    high = len(b) - 1
    pos = len(b)
    while (low < high):
        mid = (low + high) / 2
        if (b[mid] < target):
            low = mid + 1
        else:
            high = mid
            pos = high
    return pos


def deal(array, res):
    b = [9999] * len(array)
    b[0] = array[0]
    res = res + [1]
    for i in range(1, len(array)):
        pos = middle(b, array[i])
        res = res + [pos + 1]  # 前面有几个比当前数小的值
        b[pos] = array[i]  # 让数组b有序，且每个位置上的数都变成遍历到的最小值
    return res


while True:
    try:
        n = int(input())
        a = input().split(' ')
        array = map(int, a)
        dp1 = []
        dp2 = []
        dp1 = deal(array, dp1)
        array.reverse()
        dp2 = deal(array, dp2)
        dp2.reverse()
        a = max(dp1[i] + dp2[i] for i in range(n))
        print(n - a + 1)
    except:
        break
############################################################################################################
# 66.请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。
# 输入：多行字符串。每行一个IP地址和掩码，用~隔开。
# 输出:统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

# -*- coding: utf-8 -*-

import re


def isLegalIP(IP):
    if not IP or IP == "":
        return False

    pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    match = pattern.match(IP)
    if not match:
        return False

    nums = IP.split(".")
    for num in nums:
        n = int(num)
        if n < 0 or n > 255:
            return False

    return True


def CatagoryIP(IP):
    if not IP or IP == "":
        return False
    nums = IP.split(".")
    # A
    if 126 >= int(nums[0]) >= 1:
        return "A"
    # B
    if 191 >= int(nums[0]) >= 128:
        return "B"
    # C
    if 223 >= int(nums[0]) >= 192:
        return "C"
    # D
    if 239 >= int(nums[0]) >= 224:
        return "D"
    # E
    if 255 >= int(nums[0]) >= 240:
        return "E"

    return False


def isPrivateIP(IP):
    if not IP or IP == "":
        return False

    nums = IP.split(".")
    if int(nums[0]) == 10:
        return True
    if int(nums[0]) == 172:
        if 31 >= int(nums[1]) >= 16:
            return True
    if int(nums[0]) == 192 and int(nums[1]) == 168:
        return True

    return False


def isLegalMaskCode(Mask):
    if not Mask or Mask == "":
        return False
    if not isLegalIP(Mask):
        return False

    binaryMask = "".join(map(lambda x: bin(int(x))[2:].zfill(8), Mask.split(".")))
    indexOfFirstZero = binaryMask.find("0")
    indexOfLastOne = binaryMask.rfind("1")
    if indexOfLastOne > indexOfFirstZero:
        return False
    return True


try:
    A, B, C, D, E, Err, P = [0, 0, 0, 0, 0, 0, 0]
    while True:
        s = input()
        IP, Mask = s.split("~")

        if not isLegalIP(IP) or not isLegalMaskCode(Mask):
            Err += 1
        else:
            if isPrivateIP(IP):
                P += 1
            cat = CatagoryIP(IP)
            if cat == "A":
                A += 1
            if cat == "B":
                B += 1
            if cat == "C":
                C += 1
            if cat == "D":
                D += 1
            if cat == "E":
                E += 1

except:
    print(A, B, C, D, E, Err, P)
###################################################################################################################
# 67.蛇形矩阵
while True:
    try:
        n, curNum = int(input()), 1
        res = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i + 1):
                res[i - j][j] = curNum
                curNum += 1
        for i in res:
            print(" ".join(map(str, (filter(lambda i: i != 0, i)))))
    except:
        break
