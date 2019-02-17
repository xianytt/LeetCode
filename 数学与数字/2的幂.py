# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        if n == 1:
            return True
        if n % 2:
            return False
        while n>1:
            if n%2:
                return False
            else:
                n //=2
        return True if n==1 else False

    def isPowerOfTwo(self, n):
        return n > 0 and not (n & n-1)
if __name__ == "__main__":
    solu = Solution()
    print(solu.isPowerOfTwo(16))
    print(solu.isPowerOfTwo(19))
    print(solu.isPowerOfTwo(1))
    print(solu.isPowerOfTwo(-231))