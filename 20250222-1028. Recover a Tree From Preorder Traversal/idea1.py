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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dv = self.readDepthAndValue(traversal)
        index = 1
        def dfs(node, depth):
            nonlocal dv, index
            if(index >= len(dv)):
                return
            tDepth, val = dv[index]
            if(tDepth>depth):
                    node.left = TreeNode(val)
                    index += 1
                    dfs(node.left, depth + 1)
            
            if(index >= len(dv)):
                return
            tDepth, val = dv[index]
            if(tDepth>depth):
                    index += 1
                    node.right = TreeNode(val)
                    dfs(node.right, depth + 1)
        if(len(dv) == 0):
            return None
        depth, val = dv[0]
        if(depth != 0):
            return None
        root = TreeNode(val)
        dfs(root, 0)
        return root




    def readDepthAndValue(self, traversal)-> List[Tuple[int, int]]:
        ret = []
        index = 0
        while(index < len(traversal)):
            depth = 0
            value = 0
            while(index < len(traversal) and traversal[index] == '-'):
                index += 1
                depth += 1
            while(index < len(traversal) and traversal[index] != '-' ):
                chr = traversal[index]
                index+=1
                value = value * 10 + int(chr)

            ret.append((depth, value))
        return ret

s = Solution()
print(s.readDepthAndValue('1-2--3--4-5--6--7'))

root = s.recoverFromPreorder('1-2--3--4-5--6--7')
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
        q.append(node.left)
        q.append(node.right)
    return ret
        
print(treeToList(root))