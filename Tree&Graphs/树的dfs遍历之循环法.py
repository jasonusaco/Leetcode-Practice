class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def InOrder(root):
        if root:
            #递归左子
            InOrder(root.left)

            print(root.val)

            #递归右子
            InOrder(root.right)

    def PostOrder(root):
        if root:
            PostOrder(root.left)
            PostOrder(root.right)
            print(root.val)

    def PreOrder(root):
        if root:
            print(root.val)
        PreOrder(root.left)
        preOrder(root.right)
