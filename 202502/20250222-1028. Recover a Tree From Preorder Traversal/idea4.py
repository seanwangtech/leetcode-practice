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
        index = 0
        def dfs(depth) -> Optional[TreeNode]:
            nonlocal dv, index
            if(index >= len(dv)):
                return None
            
            tDepth, val = dv[index]
            if(depth != tDepth):
                return None
            
            node = TreeNode(val)
            index += 1
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)
            return node
        return dfs(0)

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
        if(node.left is None and node.right is None):
            continue
        q.append(node.left)
        q.append(node.right)
    return ret
        
print(treeToList(root))