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

    def depth(self, target, length=0):
        if self.data == target:
            return length
        for child in self.children:
            count = child.depth(target, length + 1)
            if count != -1:
                return count
        return -1 

root = TreeNode("Root")
child1 = TreeNode("Child1")
child2 = TreeNode("Child2")
child3 = TreeNode("Child3")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(TreeNode("GrandChild1"))
child2.add_child(TreeNode("GrandChild2"))
child3.add_child(TreeNode("GrandChild3"))

root.display()
depth = root.depth("GrandChild2")
print(f"Depth of GrandChild2: {depth}")