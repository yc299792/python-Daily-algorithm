class Sort(object):

    def bubble_sort(self, li):
        """
            最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
            最坏时间复杂度：O(n2)
            稳定性：稳定
        """
        for i in range(len(li) - 1):
            for j in range(len(li) - i - 1):
                if li[j] > li[j + 1]:
                    li[j], li[j + 1] = li[j + 1], li[j]
        return li

    def selection_sort(self, alist):
        """
        最优时间复杂度：O(n2)
        最坏时间复杂度：O(n2)
        稳定性：不稳定（考虑升序每次选择最大的情况）
        :return:
        """

        n = len(alist)

        # 需要进行n-1次选择操作

        for i in range(n - 1):

            # 记录最小位置
            min_index = i

            # 从i+1位置到末尾选择出最小数据

            for j in range(i + 1, n):
                if alist[j] < alist[min_index]:
                    min_index = j

            # 如果选择出的数据不在正确位置，进行交换
            if min_index != i:
                alist[i], alist[min_index] = alist[min_index], alist[i]

    def insert_sort(self, alist):
        """
        最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
        最坏时间复杂度：O(n2)
        稳定性：稳定
        :return:
        """

        # 从第二个位置，即下标为1的元素开始向前插入

        for i in range(1, len(alist)):

            # 从第i个元素开始向前比较，如果小于前一个元素，交换位置

            for j in range(i, 0, -1):

                if alist[j] < alist[j - 1]:
                    alist[j], alist[j - 1] = alist[j - 1], alist[j]

    def quick_sort(self, alist, start, end):

        """
        最优时间复杂度：O(nlogn)
        最坏时间复杂度：O(n2)
        稳定性：不稳定
        :param alist:
        :param start:
        :param end:
        :return:
        """

        # 递归的退出条件

        if start >= end:
            return

        # 设定起始元素为要寻找位置的基准元素

        mid = alist[start]

        # low为序列左边的由左向右移动的游标

        low = start

        # high为序列右边的由右向左移动的游标

        high = end

        while low < high:

            # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动

            while low < high and alist[high] >= mid:
                high -= 1

            # 将high指向的元素放到low的位置上

            alist[low] = alist[high]

            # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动

            while low < high and alist[low] < mid:
                low += 1

            # 将low指向的元素放到high的位置上

            alist[high] = alist[low]

        # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置

        # 将基准元素放到该位置

        alist[low] = mid

        # 对基准元素左边的子序列进行快速排序

        self.quick_sort(alist, start, low - 1)

        # 对基准元素右边的子序列进行快速排序

        self.quick_sort(alist, low + 1, end)

    def shell_sort(self, alist):
        """
        最优时间复杂度：根据步长序列的不同而不同
        最坏时间复杂度：O(n2)
        稳定想：不稳定
        :param alist:
        :return:
        """
        n = len(alist)
        # 初始步长

        gap = n / 2
        while gap > 0:

            # 按步长进行插入排序
            for i in range(gap, n):
                j = i
                # 插入排序
                while j >= gap and alist[j - gap] > alist[j]:
                    alist[j - gap], alist[j] = alist[j], alist[j - gap]
                    j -= gap
            # 得到新的步长
            gap = gap / 2

    def _merge(self, li, low, mid, high):
        i = low
        j = mid + 1
        ltmp = []
        while i <= mid and j <= high:
            if li[i] < li[j]:
                ltmp.append(li[i])
                i += 1
            else:
                ltmp.append(li[j])
                j += 1
        while i <= mid:
            ltmp.append(li[i])
            i += 1
        while j <= high:
            ltmp.append(li[j])
            j += 1
        li[low:high + 1] = ltmp

    def mergesort(self, li, low, high):
        """
        最优时间复杂度：O(nlogn)
        最坏时间复杂度：O(nlogn)
        稳定性：稳定
        :param li:
        :param low:
        :param high:
        :return:
        """
        if low < high:
            mid = (low + high) // 2
            self.mergesort(li, low, mid)
            self.mergesort(li, mid + 1, high)
            self._merge(li, low, mid, high)

    def _sift(self, data, low, high):
        i = low
        j = 2 * i + 1
        tmp = data[i]
        while j <= high:  # 只要没到子树的最后
            if j + 1 <= high and data[j] < data[j + 1]:  # 如果有右孩子且比左孩子大
                j += 1  # 就把j指向右孩子
            if tmp < data[j]:  # 如果领导不能干
                data[i] = data[j]  # 小领导上位
                i = j
                j = 2 * i + 1
            else:
                break
        data[i] = tmp

    def heap_sort(self, data):
        """
        堆排序
        :param data:
        :return:
        """
        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            self._sift(data, i, n - 1)
        for i in range(n - 1, -1, -1):
            data[0], data[i] = data[i], data[0]
            self._sift(data, 0, i - 1)
