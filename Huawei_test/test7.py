# 68.购物车
def max_fun(N, m, v, p, q):
    res = [[0] * (N + 1) for _ in range(m + 1)]
    # 商品
    for i in range(1, m + 1):
        # 价格
        for j in range(10, N + 1, 10):
            # 为主件时
            if q[i - 1] == 0:  # 主件
                # res[i][j]= res[i-1][j]
                if v[i - 1] <= j:
                    res[i][j] = max(res[i - 1][j], res[i - 1][j - v[i - 1]] + v[i - 1] * p[i - 1])
            # 为配件时  q[i-1] != 0
            elif v[i - 1] + v[q[i - 1]] <= j:
                res[i][j] = max(res[i - 1][j],
                                res[i - 1][j - v[i - 1] - v[q[i - 1]]] + v[i - 1] * p[i - 1] + v[q[i - 1]] * p[
                                    q[i - 1]])
    print(res[m][int(N / 10) * 10])


N_m = input().split(' ')
N = int(N_m[0])
m = int(N_m[1])
v = []
p = []
q = []
for i in range(m):
    vpq = input().split(' ')
    v.append(int(vpq[0]))
    p.append(int(vpq[1]))
    q.append(int(vpq[2]))
max_fun(N, m, v, p, q)
###################################################################################################################
# 69.输入一个字符串,输出:返回有效密码串的最大长度(密码是对称的)
def longestPalindrome(s):
    if s == s[::-1]: return len(s)
    maxLen = 0
    for i in range(len(s)):
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
            maxLen += 2
            continue
        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            maxLen += 1
    return maxLen


while True:
    try:
        a = input()
        if a:
            print(longestPalindrome(a))

    except:
        break
###################################################################################################################
# 70.名字的漂亮程度：给出一个名字，该名字有26个字符串组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。给出多个名字，计算每个名字最大可能的“漂亮度”。
from collections import Counter

while True:
    try:
        a = int(input())
        for i in range(a):
            c, start, res = Counter(input()), 26, 0
            for j in c.most_common():
                res += j[1] * start
                start -= 1
            print(res)

    except:
        break
###################################################################################################################
# 70.查找和排序
def rank_record(inp_num, rank_rule):
    dic_name = []
    while (inp_num > 0):
        inp_name = input()
        dic_name.append(inp_name)
        inp_num -= 1
    inp_name_sort = sorted(dic_name, key=lambda a: int(a.split(' ')[1]), reverse=(rank_rule - 1))
    return inp_name_sort


while True:
    try:
        inp_num = int(input())
        rank_rule = int(input())
        for i in rank_record(inp_num, rank_rule):
            print(i)
    except:
        break
###################################################################################################################
# 举办一场8小时的聚会，时间段从12：00到20：00点，让来访的客人事先填写好到达的时间和离开的时间，为了掌握聚会期间座位的数目，需要先估计不同时间的最大客人数量。
#
# 到达和离开的时间，以整点计算，输入为整数，比如“12，18”表示该客人到达时间为12点后13点前，离开时间是17点后18点前
# 按小时区间统计客人的数量，需要统计[12,13)，[13,14)…[19,20)共8个时间段的最大客人数量
# 假设邀请的客人最多100个
# 题目给了一个样例：假设输入为[12,15)，[16,17)，[12,20)，输出为[12,13)：2，[13,14)：2，[14,15)：2，[15,16)：1，[16,17)：1，[17,18)：1，[18,19)：1，[19,20)：1
#         对样例进行分析发现，每个区间的最大客人数量是通过计算能够覆盖该区间的所有客人的时间区间的数量得到的，这样做是有道理的，因为题目要求我们计算的是每个时间段的最大客人数量，如果一个客人的时间区间包含了某个时间段，那么我们有理由认为这个客人会在这个时间段来访。以计算[12,13)时间段的最大客人数量为例，[12,15)区间能够覆盖[12,13)时间段，[16,17)区间不能覆盖，[12,20)区间能够覆盖，所以[12,13)区间的最大客人数量为2，其他的时间段以此类推
#-*-coding:utf-8-*-

# 定义按照时间区间统计每个时间区间内到达人数的函数
def count_by_time_interval(lower_bound, higher_bound, customer_time_list):
    """
    :param lower_bound: 区间下界
    :param higher_bound: 区间上界
    :param customer_time_list: 用户的时间列表
    :return: 区间上的最大可能人数
    """
    # 定义某时间区间可能的用户数量
    count = 0
    # 遍历
    for per_cum_list in customer_time_list:
        arrive = per_cum_list[0]        # 到达时间
        leave = per_cum_list[1]     # 最小离开时间
        if lower_bound >= arrive and higher_bound <= leave:
            count += 1
    # 打印
    print('[' + str(lower_bound) + ',' + str(higher_bound) + '):' + str(int(count)))
    # 返回值
    return count


# 主函数
if __name__ == '__main__':
    num_list = list(range(12, 21))      # 数字列表
    all_customer_list = [[12, 15], [16, 17], [12, 20]]      # 所有用户的到达-离开时间的列表
    # 遍历数字列表，统计每个区间上可能到达的顾客数量
    i = 0
    while i < 8:
        low_bound = num_list[i]  # 时间区间的下界
        high_bound = num_list[i + 1]  # 时间区间的上界
        count_by_time_interval(low_bound, high_bound, all_customer_list)
        i += 1
###################################################################################################################
# 背包问题
# 这里使用了图解中的吉他，音箱，电脑，手机做的测试，数据保持一致
w = [0, 1, 4, 3, 1]   #n个物体的重量(w[0]无用)
p = [0, 1500, 3000, 2000, 2000]   #n个物体的价值(p[0]无用)
n = len(w) - 1   #计算n的个数
m = 4   #背包的载重量

x = []   #装入背包的物体，元素为True时，对应物体被装入(x[0]无用)
v = 0
#optp[i][j]表示在前i个物体中，能够装入载重量为j的背包中的物体的最大价值
optp = [[0 for col in range(m + 1)] for raw in range(n + 1)]
#optp 相当于做了一个n*m的全零矩阵的赶脚，n行为物件，m列为自背包载重量

def knapsack_dynamic(w, p, n, m, x):
    #计算optp[i][j]
    for i in range(1, n + 1):       # 物品一件件来
        for j in range(1, m + 1):   # j为子背包的载重量，寻找能够承载物品的子背包
            if (j >= w[i]):         # 当物品的重量小于背包能够承受的载重量的时候，才考虑能不能放进去
                optp[i][j] = max(optp[i - 1][j], optp[i - 1][j - w[i]] + p[i])    # optp[i - 1][j]是上一个单元的值， optp[i - 1][j - w[i]]为剩余空间的价值
            else:
                optp[i][j] = optp[i - 1][j]

    #递推装入背包的物体,寻找跳变的地方，从最后结果开始逆推
    j = m
    for i in range(n, 0, -1):
        if optp[i][j] > optp[i - 1][j]:
            x.append(i)
            j = j - w[i]

    #返回最大价值，即表格中最后一行最后一列的值
    v = optp[n][m]
    return v

print('最大值为：' + str(knapsack_dynamic(w, p, n, m, x)))
print('物品的索引：',x)

#最大值为：4000
#物品的索引： [4, 3]
###################################################################################################################
def MaxVal2(memo , w, v, index, last):
    """
    得到最大价值
    w为widght
    v为value
    index为索引
    last为剩余重量
    """

    global numCount
    numCount = numCount + 1

    try:
        #以往是否计算过分支，如果计算过，直接返回分支的结果
        return memo[(index , last)]
    except:
        #最底部
        if index == 0:
            #是否可以装入
            if w[index] <= last:
                return v[index]
            else:
                return 0

        #寻找可以装入的分支
        without_l = MaxVal2(memo , w, v, index - 1, last)

        #如果当前的分支大于约束
        #返回历史查找的最大值
        if w[index] > last:
            return without_l
        else:
            #当前分支加入背包，剪掉背包剩余重量，继续寻找
            with_l = v[index] + MaxVal2(memo , w, v , index - 1, last - w[index])

        #比较最大值
        maxvalue = max(with_l , without_l)
        #存储
        memo[(index , last)] = maxvalue
        return maxvalue

w = [0, 1, 4, 3, 1]   # 东西的重量
v = [0, 1500, 3000, 2000, 2000]       # 东西的价值

numCount = 0
memo = {}
n = len(w) - 1
m = 4
print(MaxVal2(memo , w, v, n, m) , "caculate count : ", numCount)


# 4000 caculate count :  20
###################################################################################################################
# 题目的大概意思：一种双核CPU的两个核能够同时的处理任务，现在有n个已知数据量的任务需要交给CPU处理，假设已知CPU的每个核1秒可以处理1kb，每个核同时只能处理一项任务。n个任务可以按照任意顺序放入CPU进行处理，现在需要设计一个方案让CPU处理完这批任务所需的时间最少，求这个最小的时间
w = [0, 3072, 3072, 7168, 3072, 1024]  # 假设进入处理的的任务大小
w = map(lambda x:x/1024,w)  # 转化下
p = w  # 这题的价值和任务重量一致
n = sum(w)/2 +1 # 背包承重为总任务的一半

optp = [[0 for j in range(n+1)] for i in range(len(w))]

for i in range(1,len(p)):
    for j in range(1,n+1):
        if j >= p[i]:
            optp[i][j] = max(optp[i-1][j],p[i]+optp[i-1][j-w[i]])
        else:
            optp[i][j] = optp[i-1][j]


print(optp[-1][-1])
print(optp)

###################################################################################################################
###################################################################################################################
###################################################################################################################
