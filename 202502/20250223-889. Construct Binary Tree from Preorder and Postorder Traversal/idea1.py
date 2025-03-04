# time complexity
# space complexity
from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = 0
        indexPost = 0
        def dfs()-> Optional[TreeNode]:
            
            nonlocal index, indexPost
            if postorder[indexPost] in preorder[:index]:
                return None 
            if(index < len(preorder)):
                valPre = preorder[index]
                index += 1
            else:
                return None
            
            node = TreeNode(valPre)
            
            if(node.val == postorder[indexPost]):
                indexPost += 1
                return node
                 
            node.left = dfs()
            node.right = dfs()
            indexPost += 1
            return node

        return dfs()
    
    def postOrderCheck(self, postorder:List[int], root) -> bool:
        index = 0
        matchSoFar = True
        def helper(node):
            if(node is None):
                return

            if(index<len(postorder)):
                val = postorder[index]
                index += 1
            else:
                return
            
            if(matchSoFar):
                postorder(node.left)
            if(matchSoFar):
                postorder(node.right)
            if(val == node.val):
                matchSoFar = True
            else:
                matchSoFar = False
            

s = Solution()

root = s.constructFromPrePost([1,2,4,5,3,6,7],[4,5,2,6,7,3,1])
# root = s.constructFromPrePost([3,4,1,2],[1,4,2,3])
# print(root.left.val)

def treeToList(root:TreeNode):
    q = deque()
    q.append(root)
    ret = []
    while q:
        node = q.popleft()
        if(node is None):
            ret.append(None)
            continue
        else:
            ret.append(node.val)
        if(node.left is None and node.right is None):
            continue
        q.append(node.left)
        q.append(node.right)
    return ret
        
print(treeToList(root))