# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        result = [0 for i in range(len(num1)-1)]
        len_num2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        #处理进位
        carry = [0 for i in range(len(num1)+len(num2))]
        for l2 in range(len_num2):
            i = l2
            result.append(0)
            for n1 in num1:
                if carry[i] != 0:
                    # 判断之前是否有进位的情况，清空已经处理的进位
                    result[i] += carry[i]
                    carry[i] = 0
                mul = int(num2[l2])*int(n1)
                #判断按位相乘的积是否是个位数
                if mul>9:
                    carry[i+1] += mul//10
                result[i] += (mul%10)
                # 判断结果是否是个位数
                if result[i] > 9:
                    carry[i+1] += result[i]//10
                    result[i] = result[i] % 10
                i += 1
        if carry[len(result)] != 0:  #判断最高位是否还有进位
            result.append(carry[len(result)])
        p = ''.join(str(i) for i in result)
        p = p[::-1]
        return p




if __name__ == "__main__":
    solu = Solution()
    print(solu.multiply("2", "3"))  #6
    print(solu.multiply("723", "10"))  #7230
    print(solu.multiply("111", "94"))  #10434
    print(solu.multiply("234", "673"))  #157482
    print(solu.multiply("234", "73"))  #17082
    print(solu.multiply("111", "43"))  #4773
    print(solu.multiply("243", "4"))   #97
    print(solu.multiply("97", "4773"))   #462981
    