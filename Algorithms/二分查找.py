def binary_search(arr_list,n):
    """二分查找python实现"""
    low,high = 0,len(arr_list)-1

    while low <= high:
        # 注意使用//代表取整，Python2中可以使用/
        mid = (low +high) // 2

        if arr_list[mid] > n:
            high = mid
            continue
        elif arr_list[mid] < n:
            low = mid
            continue
        else:
            return mid

    return False

if __name__ == '__main__':
    arr = [1,3,5,7,9]

    assert binary_search(arr,1) == 0
    assert binary_search(arr,3) == 1
    assert binary_search(arr,2) == False


