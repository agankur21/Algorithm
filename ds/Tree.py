
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.right = None
        self.left= None
        self.parent=None
        self.height = None

    def set_right_child(self,node):
         self.right=node

    def set_left_child(self,node):
         self.left=node

    def set_parent(self,node):
        self.parent=node

    def set_value(self,value):
        self.value = value

    def set_height(self,height):
        self.height=height
        if self.right is not None:
            self.right.set_height(height+1)
        if self.left is not None:
            self.left.set_height(height+1)


class Tree:
    def __init__(self,value=None):
        self.root = TreeNode(value)
        self.root.set_height(0)