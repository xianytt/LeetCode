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
    def isSameRec(self, roota, rootb):
        if roota == None and rootb==None:
            return True
        if roota==None or rootb==None:
            return False
        if roota.val != rootb.val:
            return False
        return self.isSameRec(roota.left, rootb.left) and self.isSameRec(roota.right, rootb.right)




if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree7 = TreeNode(7)
    tree2.left = tree1
    tree3.left = tree2
    tree3.right = tree4
    tree5.left = tree3
    tree5.right = tree6
    tree6.right = tree7
    solu = Solution()
    print(solu.isSameRec(tree5, tree5))
    