# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:在一个 m 行 n 列二维数组中， 每一行都按照从左到右递增的顺序排序每一列照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整

    实现思路：
        如果查找的数字小于最小的或者大于最大的即返回找不到
        从右上角开始检查，范围逐步往下缩减
        当这个数大于目标值则剔除该行
        当这个数小于目标值说明不在此列
'''
def find_num(nums, target, rows, cols):
    '''
    :param nums:   杨氏矩阵
    :param target:   要查找的数
    :param rows:   行数
    :param cols:    列数
    :return:   Ture/False
    '''
    if target<nums[0][0] or target>nums[rows-1][cols-1]:
        return False
    i = 0
    j = cols-1
    while i<rows or j<0:
        #如果右上角大于目标值则去除该行
        if target>nums[i][j]:
            i += 1
            continue
        #如果右上角小于目标值则去除该列
        elif target<nums[i][j]:
            j -= 1
            continue
            #如果找到了则返回下标
        elif target==nums[i][j]:
            return (i,j)
    # 没有找到
    return False


if __name__ == "__main__":
    nums = [[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]
    print(find_num(nums, 23, 5, 5))