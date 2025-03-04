# Definition for a binary tree node.
from collections import deque
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time complexity: init O(n), find O(n)
# space complexity: init O(1), find O(1)

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def dfs(node):
            if(node.left is not None):
                node.left.val = node.val*2 + 1
                dfs(node.left)
            if(node.right is not None):
                node.right.val = node.val*2 + 2
                dfs(node.right)
        root.val = 0
        dfs(root)
        self.root = root
        

    def find(self, target: int) -> bool:
        def dfs(node) -> bool:
            if (node is None):
                return False
            if node.val == target:
                return True
            if dfs(node.left):
                return True
            if dfs(node.right):
                return True
            return False
        return dfs(self.root)

def constuctFromArray(arr:List[int]):
    # [-1,None,-1,-1,None,-1]
    q = deque()
    root = TreeNode(arr[0])
    q.append(root)
    index = 1
    while(len(q)>0):
        node = q.popleft()
        if index <len(arr):
            if(arr[index] is not None):
                node.left = TreeNode(arr[index])
                q.append(node.left)
            index += 1
        if index <len(arr):
            if(arr[index] is not None):
                node.right = TreeNode(arr[index])
                q.append(node.right)
            index += 1
    return root
root = constuctFromArray([-1,None,-1,-1,None,-1])

# Your FindElements object will be instantiated and called as such:
obj = FindElements(root)
param_1 = obj.find(1)
print([obj.find(x) for x in [2,3,4,5]])