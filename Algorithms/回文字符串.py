#回文，英文palindrome，指一个顺着读和反过来读都一样的字符串，比如madam、我爱我，这样的短句在智力性、趣味性和艺术性上都颇有特色，中国历史上还有很多有趣的回文诗。

#那么，我们的第一个问题就是：判断一个字串是否是回文？


def is_palindrom1(str_temp):
    len_str = len(str_temp)
    m = len_str // 2 - 1
    if len_str % 2 == 0:
        n = m + 1
    else:
        n = m + 2

    print(m,n)
    while m >= 0:
        if str_temp[m] != str_temp[n]:
            return False
        m -= 1
        n += 1
    return True

def is_palindrom2(str_temp):

    return str_temp[::-1] == str_temp

if __name__ == '__main__':
    str1 = "abcdefg"
    str2 = "abfgh"
    # print(string_contain(str1,str2))
    print(is_palindrom2('abcaa'))
