# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class Solution(object):
    def solution(self, l):
        # l = sorted(l, key=lambda l:len(str(l)))
        l.sort(key=lambda x:len(str(x)), reverse=True)
        print(l)
if __name__ == "__main__":
    s = Solution()
    s.solution([4,2222,66])