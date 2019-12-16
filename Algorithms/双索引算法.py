# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
# 
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
# 
# 说明:
# 
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
# 
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#这种使用的是hash法，但是并没有使用数组的有序性
def twoSum(self, numbers: List[int], target: int) -> List[int]:
  # 定义一个数组存储值所对应的下标即用值做索引
  dict_hash = dict()
  size = len(numbers)
  for i in range(size):

      if dict_hash.get(target - numbers[i]):
          return [dict_hash[target - numbers[i]], i + 1]
      dict_hash[numbers[i]] = i + 1
  return []
    
 #使用双指针对撞法，因为数组是有序的
def twoSum(self, numbers: List[int], target: int) -> List[int]:

      #既然是有序数组，要不使用二分法，要不使用双指针对撞的方法
      l = 0
      r = len(numbers) - 1

      while l < r:

          if numbers[l] + numbers[r] == target:
              return [l+1,r+1]
          elif numbers[l] + numbers[r] < target:
              #既然是有序数组，那么比目标小证明只能让左边增加
              l += 1
          else:
              r -= 1

      return []
      
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#这里注意编码细节就可以了
def isPalindrome(self, s: str) -> bool:

    l = 0
    r = len(s) - 1

    while l < r:

        if not s[l].isalnum():
            l += 1
            continue

        if not s[r].isalnum():
            r -= 1
            continue

        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
    return True
    
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
#  
#
# 示例 1：
#
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 示例 2：
#
# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]

#这题比较简单
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    l = 0
    r = len(s) - 1

    while l < r:
         s[l],s[r] = s[r],s[l]

         l += 1
         r -= 1
         
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
# 说明:
# 元音字母不包含字母"y"。

#不区分大小写，注意对字符串是不能更改的

def reverseVowels(self, s: str) -> str:
    s = list(s)
    l = 0
    r = len(s) - 1
    dict_hash = {}
    dict_hash['a'] = 1
    dict_hash['e'] = 1
    dict_hash['i'] = 1
    dict_hash['o'] = 1
    dict_hash['u'] = 1

    while l < r:

        if not dict_hash.get(s[l].lower()):
            l += 1
            continue
        if not dict_hash.get(s[r].lower()):
            r -= 1
            continue

        s[l], s[r] = s[r], s[l]

        l += 1
        r -= 1
    return ''.join(s)




# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#  
#
# 示例:
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
#解题思路就是总是先固定住高度，因为高度是确定的就是两个木板中较低的那一个，然后就是游标是要移动更矮的那一边，因为只有这样才会让面积更大
 def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        res = 0

        while l < r:

            #取两端较低的代表高度
            h = min(height[l],height[r])
            #更新面积的较大值
            res = max(res,(r-l)*h)
            #让更矮那边的游标游动，因为决定面积的是矮木板的高度
            if height[l] <= height[r]:
                l += 1 
            else:
                 r -= 1
        return res
    
