# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # BFS
        # Append right child then left child
        # At each level, the first in BFS queue is the 
        # one we see

        if not root:
            return []

        res = []

        q = deque()
        q.append(root)

        while q:
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft()

                # If first of this level, then append to res
                if (i == 0):
                    res.append(node.val)
                
                # Add right child
                if node.right:
                    q.append(node.right)

                # Add left child
                if node.left:
                    q.append(node.left)
        
        return res

        # Time Complexity: O(n)
        # Space Complexity: O(D) where D is width of tree