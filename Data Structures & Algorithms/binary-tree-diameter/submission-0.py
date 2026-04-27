class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            # update diameter (path through this node)
            self.diameter = max(self.diameter, left + right)

            # return height of this node
            return 1 + max(left, right)

        depth(root)
        return self.diameter