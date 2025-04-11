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
print("Direct children of root:")
for child in root.children:
    print(child.data)