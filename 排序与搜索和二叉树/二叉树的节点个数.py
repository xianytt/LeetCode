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
    def getNodeNumRec(self, root):
        '''
        获取二叉树的节点个数
        :param root:
        :return:   根节点 + 左叉树的节点个数 + 右叉树的节点个数（节点为空）
        '''
        if root == None:
            return 0
        return 1 + self.getNodeNumRec(root.left) + self.getNodeNumRec(root.right)
if __name__ == "__main__":
    tree2 = TreeNode(2)
    tree1 = TreeNode(1)
    tree1.right = tree2
    tree3 = TreeNode(3)
    tree3.left = tree1
    tree4 = TreeNode(4)
    tree3.right = tree4
    solu = Solution()
    print(solu.getNodeNumRec(tree3))
    