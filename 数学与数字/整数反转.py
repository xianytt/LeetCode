# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
      整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # x是个位数
        if (x // 10) == 0:
            return x
        str_x = str(x)
        x = ""
        if str_x[0] == '-':
            x = x + '-'
        x = x + str_x[len(str_x) - 1::-1].lstrip("0").rstrip("-")
        x = int(x)
        # 溢出判断
        if -2**31<x<2**31-1:
            return x
        else:
            return 0



if __name__ == "__main__":
    solu = Solution()
    print(solu.reverse(123))
    print(solu.reverse(-123))
    print(solu.reverse(1534236469))
    