# _*_ coding:utf-8 _*_
'''
    @author:xianyt
    @date:2018/
    @func:
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution():
    def getDepthRec(self, root):
        '''
        二叉树的深度
        :param root:
        :return: 1 + max(左叉树的深度， 右叉树的深度)  --> 根节点为空
        '''
        if root == None:
            return 0
        return 1 + max(self.getDepthRec(root.left), self.getDepthRec(root.right))
if __name__ == "__main__":
    tree2 = TreeNode(2)
    tree1 = TreeNode(1)
    tree1.right = tree2
    tree3 = TreeNode(3)
    tree3.left = tree1
    tree4 = TreeNode(4)
    tree3.right = tree4
    solu = Solution()
    print(solu.getDepthRec(tree3))
    