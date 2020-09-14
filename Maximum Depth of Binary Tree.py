Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

***************************************************************************8

  def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        que = []
        que.append(root)
        count = 0
        if root is None:
            return count
        while que:
            nodes = []
            for x in range(len(que)):
                node = que.pop(0)
                nodes.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                    
            count += 1
        return count
        
