# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class Solution(object):
    def spiralOrder(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def cyc(row, column, ri, ci, case, result):
            '''
            :param column:  列数
            :param ri:   #行的起点
            :param ci:   #列的起点
            :param case:   #方向
            :return:
            '''

            # 递归中断条件
            if row == 0 or column == 0:
                return
                # 从左往右：
            if case == 0:
                endci = ci + column
                for i in range(ci, endci):
                    if re[ri][i] == 0:
                        re[ri][i] = result
                        result += 1
                row -= 1
                ri += 1
                ci = endci - 1
                case = (case+1) % 4
                cyc(row, column, ri, ci, case, result)
            elif case == 1:
                endri = ri + row
                for i in range(ri, endri):
                    if re[i][ci] == 0:
                        re[i][ci] = result
                        result += 1
                column -= 1
                ci -= 1
                ri = endri - 1
                case = (case+1) % 4
                cyc(row, column, ri, ci, case, result)

            elif case == 2:
                endci = ci - column
                for i in range(ci, endci, -1):
                    if re[ri][i] == 0:
                        re[ri][i] = result
                        result += 1
                row -= 1
                ri = ri - 1
                ci = endci + 1
                case = (case+1) % 4
                cyc(row, column, ri, ci ,case, result)

            else:
                endri = ri - row
                for i in range(ri, endri, -1):
                    if re[i][ci] == 0:
                        re[i][ci] = result
                        result += 1
                    # print("{}+{} = {}".format(i, ci, re[i][ci]))
                column -= 1
                ri = endri + 1
                ci += 1
                case = (case+1) % 4
                cyc(row, column, ri, ci, case, result)


        if n == 0:
            return []
        if n == 1:
            return [[1]]
        re = []
        for i in range(n):
            re.append([0 for i in range(n)])
        cyc(n, n, 0, 0, 0, 1)
        return re



if __name__ == "__main__":
    solu = Solution()
    print(solu.spiralOrder(3))  #[[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print(solu.spiralOrder(4))
    