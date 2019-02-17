# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''


class SoreList():
    def insert_sort(self, solu):
        '''
        :param solu: 插入排序，时间复杂度：O(n^2),稳定
        :return:
        '''
        count = len(solu)
        for i in range(1, count):
            key = solu[i]
            j = i -1
            while j >= 0:
                if solu[j] > key:
                    solu[j+1] = solu[j]
                    solu[j] = key
                j -= 1
        return solu
    def shell_sort(self, solu):
        '''
        :param solu: 希尔排序，时间复杂度O(n^1.3~2),不稳定
        :return:
        '''
        count = len(solu)
        step = 2
        group = count // step
        while group > 0:
            for i in range(0, group):
                j = i + group
                while j < count:
                    k = j - group
                    key = solu[j]
                    while k >= 0:
                        if solu[k] > key:
                            solu[k + group] = solu[k]
                            solu[k] = key
                        k -= group
                    j += group
            group //= step
        return solu
    def bubble_sort(self, solu):
        '''
        :param solu: 冒泡排序，O(n^2)
        :return:
        '''
        count = len(solu)
        for i in range(count-1):
            for j in range(i+1, count):
                if solu[i] > solu[j]:
                    solu[i], solu[j] = solu[j], solu[i]
        return solu
    def quick_sort(self, solu, left, right):
        '''
        :param solu:快速排序，O(nlgn)~O(n^2),不稳定
        :return:
        '''
        if left >= right:
            return solu
        key = solu[left]
        low = left
        higt = right
        while left < right:
            while left < right and solu[right] >= key:
                right -= 1
            solu[left] = solu[right]
            while left < right and solu[left] <= key:
                left += 1
            solu[right] = key
        self.quick_sort(solu, low, left-1)
        self.quick_sort(solu, left+1, higt)
        return solu
    def select_sort(self, solu):
        '''
        选择排序，O(n^2),不稳定
        :param solu:
        :return:
        '''
        count = len(solu)
        for i in range(0, count-1):
            min = i
            for j in range(i+1, count):
                if solu[j] < solu[min]:
                    min = j
            if min != i:
                solu[min], solu[i] = solu[i], solu[min]
        return solu


    '''
    归并排序， O(nlgn),稳定
    '''
    def merge(self, left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result
    def merge_sort(self, solu):
        if len(solu) <= 1:
            return solu
        num = len(solu) // 2
        left = self.merge_sort(solu[:num])
        right = self.merge_sort(solu[num:])
        return self.merge(left, right)

if __name__ == "__main__":
    solu = [3,1,5,4,8,19,13,6,2]
    s = SoreList()
    print('插入排序:{}'.format(s.insert_sort(solu)))
    print('希尔排序：{}'.format(s.shell_sort([3,1,5,4,8,19,13,6,2])))
    print('冒泡排序：{}'.format(s.bubble_sort([3,1,5,4,8,19,13,6,2])))
    print('快速排序：{}'.format(s.quick_sort([3, 1, 5, 4, 8, 19, 13, 6, 2], 0, 8)))
    print('选择排序:{}'.format(s.select_sort([3,1,5,4,8,19,13,6,2])))
    print('归并排序:{}'.format(s.merge_sort([3, 1, 5, 4, 8, 19, 13, 6, 2])))

    