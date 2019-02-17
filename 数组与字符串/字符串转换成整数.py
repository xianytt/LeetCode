# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

去除左边的空格
判断去除之后的字符串长度是否为0，是返回0，不是转到3
判断字符串长度为1的字符串是否为数值，不是返回0，是返回该数字（一个数字不不可能不在该[−231, 231 − 1]区间）
判断第一个非空字符串是否为数字或是符号位，不是返回0，是则一直判断到第一个非数字字符。
返回找到的结果，并判断是否为空白或是符号位，是返回0.不是转到6
取整结果并判断结果是否在该区间[−231, 231 − 1]

'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #取出左边的空格
        str = str.lstrip()
        result = ""
        #判断第一个是否是数字或是-
        if len(str) == 0:
            return 0
        if len(str) == 1:
            if self.isNum(str):
                return int(str)
            else:
                return 0
        if self.isNum(str[0]) or str[0] == '-' or str[0] == '+':
            if str[0] != '+':
                result += str[0]

            for s in str[1:]:
                # 判断是否为数值
                if self.isNum(s):
                    result += s
                    continue
                # 找到非数字结尾
                else:
                    break

        if result == '' or result == '-':
            return 0
        result = int(result)
        if result <= -2147483648:
            return -2147483648
        elif result >= 2147483648:
            return 2147483647
        else:
            return result

    def isNum(self, str):
        if str.isdigit():
            return True
        else:
            return False
if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("1+"))
