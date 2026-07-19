class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if root.left is None:
            root.left = Node(data)
        elif root.right is None:
            root.right = Node(data)
        else:
            self.insert(root.left, data)
        return root

    def dfs(self, root):
        if root is None:
            return

        stack = []
        stack.append(root)
        while len(stack) > 0:
            current = stack.pop()
            print(current.data, end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
# Driver Code
t = Tree()

t.root = t.insert(t.root, 10)
t.root = t.insert(t.root, 20)
t.root = t.insert(t.root, 50)
t.root = t.insert(t.root, 30)
t.root = t.insert(t.root, 40)
t.root = t.insert(t.root, 60)

print("DFS Traversal:")
t.dfs(t.root)