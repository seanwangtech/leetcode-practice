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
        pass

s = Solution()

root = s.constructFromPrePost([1,2,4,5,3,6,7],[4,5,2,6,7,3,1])
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