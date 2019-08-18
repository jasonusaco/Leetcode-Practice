"""
主要就是集中情况的判断
情况1：如果当前节点有右子树，那么中序的下一个节点就是右子树的最左子节点
情况2：如果没有右子树，那么又分为两种情况
    小情况1：如果当前节点是父节点的左子节点，那么中序的下一个就是它的父节点
    小情况2：如果当前节点是父节点的右子节点，
    那么就要网上找父节点，然后找到父节点的左子节点，这就是中序的下一个
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self,pNode):
        if not pNode:
            return None
        #当前节点有右节点的时候
        if pNode.right:
            #node作为指针指向当前节点的右子节点
            node = pNode.right
            #遍历node的最左子节点
            while node.left:
                node = node.left
            return node
        #如果没有右子树
        else:
            #如果当前节点的下一个左子节点
            if pNode.next and pNode.next.left == pNode:
                return pNode.next
            else:
                node = pNode.next
                while node:
                    if node.next and node.next.left == node:
                        return node.next
                    else:
                        node = node.next
                return node
            
