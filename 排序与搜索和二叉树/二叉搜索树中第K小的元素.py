# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
    给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 先广度优先遍历
        width = [root]
        val = [root.val]
        i = 0
        while i < len(width):
            cur = width[i]
            if cur.left is not None:
                width.append(cur.left)
                val.append(cur.left.val)
            if cur.right is not None:
                width.append(cur.right)
                val.append(cur.right.val)
            i += 1
        val.sort()
        return val[k - 1]

    def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                k -= 1
                if k == 0:
                    return root.val
                else:
                    root = root.right


if __name__ == "__main__":
    tree2 = TreeNode(2)
    tree1 = TreeNode(1)
    tree1.right = tree2
    tree3 = TreeNode(3)
    tree3.left = tree1
    tree4 = TreeNode(4)
    tree3.right = tree4
    solu = Solution()
    print(solu.kthSmallest(tree3, 2))
    