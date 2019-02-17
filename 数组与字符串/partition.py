#encoding = 'utf-8'
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

    返回 s 所有可能的分割方案。

    示例:

    输入: "aab"
    输出:
    [
      ["aa","b"],
      ["a","a","b"]
    ]


'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []  #存放匹配到的正则表达式
        s_length = len(s)
        for i in range(s_length):
            j = i+1;
            while(j<=s_length):
                if(self.palindrome(s[i:j])):
                    print('-----')
                    result.append(s[i:j])
                print(s[i:j])
                j += 1;
        return result;
        # print(s[1:4])
        # print(type(s[1]))
    def palindrome(self, s):
        j = len(s)-1;
        for i in range(len(s)):
            if i>=j :    #i>=j说明没有出现不一样的
                return True;

            if s[i]!=s[j]:   #出现字符不匹配
                return False
            else:
                j-=1;


if __name__ == "__main__":
    s = Solution()
    result = s.partition('aab')
    print(result)
    # if(s.palindrome('a4a')):
    #     print('yes')