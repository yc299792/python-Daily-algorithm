def dynamic_primes(w, p):
    """动态规划之背包问题"""
    m = len(w)
    n = 4
    dp = [[0 for col in range(n + 1)] for j in range(m)]

    x = []  # 装入物体
    v = 0  # 总价值

    # 根据状态转移方程计算放入背包中物体的最大价值
    for i in range(1, m):
        for j in range(1, n + 1):
            if j >= w[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + p[i])
            else:
                dp[i][j] = dp[i - 1][j]
    j = n
    #逆向判断应该放入背包中的物品
    for i in range(m - 1, 0, -1):
        if dp[i][j] > dp[i - 1][j]:
            x.append(i)
            j = j - w[i]  # 取剩余容量，继续遍历

    v = dp[m-1][n]
    return x,v


if __name__ == "__main__":
    w = [0, 1, 4, 3, 1]  # 物品重量
    p = [0, 1500, 3000, 2000, 2000]  # 价格
    x,v = dynamic_primes(w,p)

