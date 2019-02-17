# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>1:
            if num%4:
                return False
            else:
                num //=4
        return True if num==1 else False

if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfFour(0))
    print(s.isPowerOfFour(1))
    print(s.isPowerOfFour(2))
    print(s.isPowerOfFour(8))