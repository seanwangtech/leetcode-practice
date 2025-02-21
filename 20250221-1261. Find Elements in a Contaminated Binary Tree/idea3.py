# Definition for a binary tree node.
from collections import deque
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time complexity: init O(n), find O(1)
# space complexity: init O(n), find O(1)

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hashSet = set()
        self.root = root
        self.hashSet.add(0)
        def dfs(node):
            if(node.left is not None):
                node.left.val = node.val*2 + 1
                self.hashSet.add(node.left.val)
                dfs(node.left)
            if(node.right is not None):
                node.right.val = node.val*2 + 2
                self.hashSet.add(node.right.val)
                dfs(node.right)
        root.val = 0
        dfs(root)
        

    def find(self, target: int) -> bool:
        return target in self.hashSet

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