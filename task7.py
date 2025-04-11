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

root = TreeNode("Semester 4")
child1 = TreeNode("DSA")
child2 = TreeNode("MnI")
child3 = TreeNode("OS")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(TreeNode("Lab"))
child1.add_child(TreeNode("Theory"))
child2.add_child(TreeNode("Lab"))
child2.add_child(TreeNode("Theory"))
child3.add_child(TreeNode("Lab"))
child3.add_child(TreeNode("Theory"))

print("Folder Structure is given below:")
root.display()