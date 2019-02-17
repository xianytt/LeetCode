# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个整数序列，a0, a1, a2, …… , an（项可以为负数），求其中加和（sum）最大的连续子序列。
    例如： [-2，1，-2，3，10，-4，7，2，5，-2，1]的加和连续最大子序列为[3,10,-4,7,2,5]
'''
class Solution(object):
    def sum(self, li):
        result = 0
        try:
            for i in li:
                result += i
        except:
            print('列表中存在非数字')
        else:
            print(result)

    def findresult(self, li):
        subresults = []
        flag = False
        for i in li:
            if flag and i < 0:
                flag = False
            elif flag:
                subresults[-1].append(i)
            elif i > 0:
                flag = True
                subresults.append([i])
        return sorted(subresults, key=lambda x: sum(x), reverse=True)[0]

if __name__ == "__main__":
    li = [-2, 1,-2,3,10,-4,7,2,5,-2,1]
    s =Solution()
    s.sum(li)
    print(s.findresult(li))



'''
链接：https://www.nowcoder.com/questionTerminal/afe7c043f0644f60af98a0fba61af8e7
来源：牛客网

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] arg) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean flag = true;

        while(true) {
            try {
                String s = br.readLine();
                if (s == null) break;
                if (flag) {
                    int n = Integer.valueOf(s);
                    if (n == 0) break;
                } else {
                    String[] nums = s.split(" ");
                    count(nums);
                }
                flag = !flag; 
            } catch (IOException e) {}
        }
    }

    static void count(String[] nums) {
        int a = 0, left = 0, length = 0, max = Integer.MIN_VALUE, sum = 0;
        for (int i = 0; i < nums.length; i++) { // 遍历一遍
            sum += Integer.valueOf(nums[i]); // 累加求和
            if (sum >= max) { // 出现新的最大数，记录起点、长度和最大值
                left = a;
                length = i - a + 1;
                max = sum;
            }

            if (sum < 0) { // 累加值为负数时，后面的数和负数相加一定会变得更小，所以。。。
                sum = 0; // sum 清零，重新累加
                a = i + 1; // 重新定位起始点，开始一个新的子串（当新子串的sum>max时，把a赋值给left）
            } 
        }
        System.out.println(max + " " + nums[left] + " " + nums[left + length - 1]);
    }
}
'''