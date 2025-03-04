# Definition for a binary tree node.
from collections import deque
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time complexity: init O(1), find O(log(n))
# space complexity: init O(1), find O(log(n))

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        

    def find(self, target: int) -> bool:
        stack = []
        LEFT, RIGHT = 1, 0
        while target>0:
            stack.append(target%2)
            target = (target-1)//2 
        node = self.root
        while len(stack) >0:
            lr = stack.pop()
            if lr == LEFT:
                if node.left is None:
                    return False
                node = node.left
            else:
                if node.right is None:
                    return False
                node = node.right
        return True
            

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