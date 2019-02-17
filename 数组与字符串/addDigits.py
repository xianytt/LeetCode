#encoding = 'utf-8'
'''
    @author:xianyt
    @date:2018/
    @func:给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
    总结：在python里一般都不用%/之类的来取位数，直接转换成字符串放进列表就行
'''


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0;
        for i in list(str(num)):
            sum += int(i);
        if sum<10:
            return sum;
        else:
            return self.addDigits(sum)




if __name__ == "__main__":
    # s = Solution()
    # print(s.addDigits(839))
    item = {}
    item['aaa'] = 1
    print(item['aaa'])