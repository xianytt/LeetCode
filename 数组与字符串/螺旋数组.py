# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        def cyc(row, column, ri, ci, case):
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
                    re.append(matrix[ri][i])
                row -= 1
                ri += 1
                ci = endci - 1
                case = (case+1) % 4
                cyc(row, column, ri, ci, case)
            elif case == 1:
                endri = ri + row
                for i in range(ri, endri):
                    re.append(matrix[i][ci])
                column -= 1
                ci -= 1
                ri = endri - 1
                case = (case+1) % 4
                cyc(row, column, ri, ci, case)

            elif case == 2:
                endci = ci - column
                for i in range(ci, endci, -1):
                    re.append(matrix[ri][i])
                row -= 1
                ri = ri - 1
                ci = endci + 1
                case = (case+1) % 4
                cyc(row, column, ri, ci ,case)

            else:
                endri = ri - row
                for i in range(ri, endri, -1):
                    re.append(matrix[i][ci])
                column -= 1
                ri = endri + 1
                ci += 1
                case = (case+1) % 4
                cyc(row, column, ri, ci, case)

        re = []
        row = len(matrix)
        if row <= 1:
            return matrix
        column = len(matrix[0])
        cyc(row, column, 0, 0, 0)
        return re



if __name__ == "__main__":
    solu = Solution()
    print(solu.spiralOrder([
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]))
    print(solu.spiralOrder([[1, 2, 3, 4], [0, 12, 13, 5], [0, 11, 14, 6], [10, 9, 8, 7]]))
    