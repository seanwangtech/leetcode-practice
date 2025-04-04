from email.errors import NonPrintableDefect
from typing import *
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getMaxDepth(node) -> int:
            if node is None:
                return -1
            return max(getMaxDepth(node.left), getMaxDepth(node.right))+1
        maxDepth = getMaxDepth(root)
        path = []
        lcaCandiates = None
        def helper(node,depth=0):
            nonlocal maxDepth, lcaCandiates, path
            if node is None:
                return
            path.append(node)
            if (depth == maxDepth):
                if lcaCandiates is None:
                    lcaCandiates = [*path]
                else:
                    for i in range(len(lcaCandiates)-1, -1, -1):
                        if lcaCandiates[i] != path[i]:
                            lcaCandiates.pop()
                        else:
                            break
            helper(node.left, depth+1)
            helper(node.right, depth+1)
            path.pop()
        helper(root)
        return lcaCandiates[-1]

s = Solution()


def getTree(nodes:List[int]):
    N = len(nodes)
    root = TreeNode([nodes[0]])
    q = deque([root])
    index = 1
    while q:
        node = q.popleft()
        if index< N:
            if nodes[index] is not None:
                node.left = TreeNode(nodes[index])
                q.append(node.left)
            index += 1
        if index < N: 
            if nodes[index] is not None:
                node.right = TreeNode(nodes[index])
                q.append(node.right)
            index += 1
    return root


print(s.lcaDeepestLeaves(getTree([3,5,1,6,2,0,8,None,None,7,4])))