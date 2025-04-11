class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print(" " * level * 4 + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

    def max_depth(self):
        if not self.children:
            return 1
        depths = []
        for child in self.children:
            depths.append(child.max_depth())
        return 1 + max(depths)

root = TreeNode("Root")
child1 = TreeNode("Child1")
child2 = TreeNode("Child2")
child3 = TreeNode("Child3")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(TreeNode("GrandChild1.1"))
child1.add_child(TreeNode("GrandChild1.2"))
child1.add_child(TreeNode("GrandChild1.3"))
child2.add_child(TreeNode("GrandChild2.1"))
child2.add_child(TreeNode("GrandChild2.2"))
child3.add_child(TreeNode("GrandChild3"))

root.display()
length = root.max_depth()
print(f"Maximum depth of the tree: {length}")