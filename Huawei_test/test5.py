# 27.将一个字符中所有出现的数字前后加上符号“*”，其他字符保持不变
while True:
    try:
        a, res, isNum = input(), "", False
        for i in a:

            if i.isdigit():
                if not isNum:
                    res = res + "*" + i
                else:
                    res += i
                isNum = True
            else:
                if isNum:
                    res = res + "*" + i
                else:
                    res += i
                isNum = False
        if a[-1].isdigit():
            res += "*"
        print(res)


    except:
        break
############################################################################################################
# 29.计票统计 输入：候选人的人数，第二行输入候选人的名字，第三行输入投票人的人数，第四行输入投票。输出：每行输出候选人的名字和得票数量。
from collections import Counter
while True:
    try:
        a=input()
        b=input().split()
        c=input()
        d=input().split()
        invalid=0
        cc = Counter(d)
        for i in b:
            print(i + " : " + str(cc[i]))
            invalid+=cc[i]
        print("Invalid : " + str(len(d)-invalid))
    except:
        break
############################################################################################################
# 30.编写一个函数，传入一个int型数组，返回该数组能否分成两组，使得两组中各元素加起来的和相等，并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），能满足以上条件，返回true；不满足时返回false。
while 1:
    try:
        n = input()
        l = input().split()
        sum1 = sum2 = 0
        ll = []
        for i in l:
            if int(i) % 5 == 0:
                sum1 += int(i)
            elif int(i) % 3 == 0:
                sum2 += int(i)
            else:
                ll.append(int(i))
        d_value = abs(sum1 - sum2)
        if not ll and d_value == 0:
            print('true')
        elif not ll and d_value != 0:
            print('false')
        else:
            s = set()
            for x in ll:
                tmp = list(s)
                for y in tmp:
                    s.add(x + y)
                s.add(x)
            for may_value in s:
                if d_value == abs((sum(ll) - may_value) - may_value):
                    print('true')
                    break
            else:
                print('false')
    except:
        break
############################################################################################################
# 31.在字符串中找出连续最长的数字字符串。输入：一个字符串。输出：字符串中最长的数字字符串和它的长度。如果有相同长度的串，则要一块儿输出，但是长度还是一串的长度
while True:
    try:
        a = input()
        maxLen, maxStrs, curLen, curStr = 0, [], 0, ""
        for i, v in enumerate(a):
            if v.isnumeric():
                curLen += 1
                curStr += v
                if curLen > maxLen:
                    maxLen = curLen
                    maxStrs = [curStr]
                elif curLen == maxLen:
                    maxStrs.append(curStr)
            else:
                curLen = 0
                curStr = ""
        print("".join(maxStrs) + "," + str(maxLen))
    except:
        break
############################################################################################################
# 37.功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
while True:
    try:
        res, a = 0, bin(int(input())).replace("0b", "")
        for i in range(1, len(a) + 1):
            if "1" * i in a:
                res = i
            else:
                break
        print(res)
    except:
        break
############################################################################################################
# 39.找出给定字符串中大写字符(即'A'-'Z')的个数
import sys
for a in sys.stdin:
    count=0
    for i in a:
        if i.isupper():
            count+=1
    print(count)
############################################################################################################
# 41.字符串匹配：判断短字符串中的所有字符是否在长字符串中全部出现
while True:
    try:
        a,b=set(input()),set(input())
        print ("true" if a&b==a else "false")
    except:
        break
############################################################################################################
# 42.将两个整型数组按照升序合并，并且过滤掉重复数组元素
while True:
    try:
        a, b, c, d = input(), list(map(int, input().split())), input(), list(map(int, input().split()))
        print("".join(map(str, sorted(list(set(b + d))))))

    except:
        break
############################################################################################################
# 43.计算字符串的相似度
def editDistance(str1, str2):
    len1, len2 = len(str1) + 1, len(str2) + 1
    dp = [[0 for i in range(len2)] for j in range(len1)]
    for i in range(len1):
        dp[i][0] = i
    for j in range(len2):
        dp[0][j] = j
    for i in range(1, len1):
        for j in range(1, len2):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]))
    return dp[-1][-1]


while True:
    try:
        print("1/" + str(editDistance(input(), input()) + 1))
    except:
        break
############################################################################################################
# 44.请设计一个算法完成两个超长正整数的加法。
while True:
    try:
        a = input()
        b = input()
        print(str(int(a) + int(b)))
    except:
        break
############################################################################################################
# 45.计算两个字符串的最大公共字串的长度，字符不区分大小写
def find_lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]  # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax = 0  # 最长匹配的长度
    p = 0  # 最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return mmax  # 返回最长子串及其长度


while True:
    try:
        a, b = input(), input()
        print(find_lcsubstr(a, b))
    except:
        break
############################################################################################################
# 51.实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
from collections import defaultdict
while True:
    try:
        a = input()
        dd = defaultdict(int)
        for i in a:
            dd[i] += 1
        for i in dd:
            if dd[i] == min(dd.values()):
                a = a.replace(i, "")
        print(a)
    except:
        break
############################################################################################################
# 52. 中级对字符串中的所有单词进行倒排。（非构成单词的字符均视为单词间隔符）注：Python isalnum() 方法检测字符串是否由字母和数字组成。
#
# list.reverse() 函数用于反向列表中元素。
s = input()
for i in s:
    if not i.isalnum():
        s = s.replace(i, ' ')
s = s.split()
s.reverse()
new_s = ' '.join(s)
print(new_s)
############################################################################################################
# 53.输出7有关数字的个数，包括7的倍数，还有包含7的数字（如17，27，37...70，71，72，73...）的个数（一组测试用例里可能有多组数据，请注意处理）
while True:
    try:
        a=int(input())
        res=0
        for i in range(7,a+1):#右边是开区间
            if "7" in str(i) or i%7==0:
                res+=1
        print(res)
    except:
        break

############################################################################################################
# 54.输入n个整数，输出其中最小的k个。输入说明 
# 1 输入两个整数 
# 2 输入一个整数数组注：Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
while True:
    try:
        count=int(input().split()[1])
        array=list(map(int,input().strip().split()))
        print(" ".join(map(str,sorted(array)[:count])))
    except:
        break
############################################################################################################
# 55.找出字符串中第一个只出现一次的字符（通过率30%）
while True:
    try:
        s=input()
        for i in s:
            if s.count(i)==1:
                print(i)
                break
            else:
                print(-1)
    except:
        break
while True:
    try:
        from collections import Counter

        a = input()
        c = list(map(lambda c: c[0], list(filter(lambda c: c[1] == 1, Counter(a).most_common()))))
        if not c: print(-1)
        for i in a:
            if i in c:
                print(i)
                break

    except:
        break

############################################################################################################
# 56. 任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对

import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
while True:
    try:
        num, start = int(input()) // 2, 1
        if num % 2 == 1:
            start = 0
        for i in range(start, num, 2):
            a, b = num + i, num - i
            if isPrime(a) and isPrime(b):
                print(b)
                print(a)
                break
    except:
        break
