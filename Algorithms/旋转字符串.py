 # 给定一个字符串，要求把字符串前面的若干个字符移动到字符串的尾部，如把字符串“abcdef”前面的2个字符'a'和'b'移动到字符串的尾部，
# 使得原字符串变成字符串“cdefab”。请写一个函数完成此功能，要求对长度为n的字符串操作的时间复杂度为 O(n)，空间复杂度为 O(1)。

def reverse_string_part(str,left,right):
    """说明一下，python中的字符串是不可变类型，所以这种思想用列表来代替，当然也可以用新的变量存储字符串操作的值"""

    while left <= right:
        str[left],str[right] = str[right],str[left]
        left += 1
        right -= 1

def  reverse_string(str,n):
    m = len(str)
    reverse_string_part(str,0,n-1)
    reverse_string_part(str,n,m-1)
    reverse_string_part(str,0,m-1)


if __name__ == '__main__':
    str = ['a','b','c','d','e','f']
    reverse_string(str,2)
