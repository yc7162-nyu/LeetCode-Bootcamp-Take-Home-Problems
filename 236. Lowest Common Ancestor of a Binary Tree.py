# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        found = False

        def helper(node, p, q):
            nonlocal found

            # Base case current node is null
            if node == None:
                return None

            
            # go down lst
            lst = helper(node.left, p, q)

            # Possible that the common ancestor is in the lst
            # if found = true, then this is the case, no need to check rst
            if found == True:
                return lst

            rst = helper(node.right, p, q)

            if found == True:
                return rst

            # Case 5
            if lst != None and rst != None:
                found = True
                return node

            if not rst and not lst:
                # Case 1
                if node != p and node != q:
                    return None
                # Case 2
                elif node == p or node == q:
                    return node

            if lst != None or rst != None:
                # Case 3
                if node != p and node != q:
                    return node
                # Case 4
                elif node == p or node == q:
                    found = True
                    return node      
        
        return helper(root, p, q)


    ''' 
        At each particular node, there are a number of cases:

        Case 1:
            No descendents are p or q
            curr (root) of this subtree is not p or q

            return None
        
        Case 2:
            No descendents are p or q
            root of this st is p or q

            return curr

        Case 3:
            Descendent is p or q (only 1; marked by found = False)
            curr not p or q

            return curr
        
        Case 4:
            Descendent is p or q (only 1; marked by found = False)
            curr p or q

            mark found = True
            return curr
        
        Case 5:
            lc is p or q
            rc is p or q

            mark found = True
            return curr
    '''