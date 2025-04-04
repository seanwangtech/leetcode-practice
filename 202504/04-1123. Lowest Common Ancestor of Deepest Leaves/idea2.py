from email.errors import NonPrintableDefect
from tkinter.tix import Tree
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
        def dfs(node:TreeNode) -> Tuple[int, TreeNode]:
            if node is None:
                return (-1, None)
            ldepth, llca = dfs(node.left)
            rdepth, rlca = dfs(node.right)
            if ldepth> rdepth:
                return ldepth+1, llca
            elif ldepth == rdepth:
                return ldepth+1, node
            else:
                return rdepth+1, rlca

        return dfs(root)[1]

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