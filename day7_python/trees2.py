# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class Tree:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         newNode = Node(data)

#         if self.root is None:
#             self.root = newNode
#             return
#         queue = []
#         queue.append(self.root)

#         while queue:
#             temp = queue.pop(0)

#             if temp.left is None:
#                 temp.left = newNode
#                 return
#             else:
#                 queue.append(temp.left)

#             if temp.right is None:
#                 temp.right = newNode
#                 return
#             else:
#                 queue.append(temp.right)

#     def inorder(self, root):
#         if root:
#             self.inorder(root.left)
#             print(root.data, end=" ")
#             self.inorder(root.right)


# # Driver Code
# t = Tree()

# t.insert(10)
# t.insert(20)
# t.insert(30)
# t.insert(40)
# t.insert(50)
# t.insert(60)
# t.insert(70)

# print("Inorder Traversal:")
# t.inorder(t.root)


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

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


# Driver Code
t = Tree()

t.root = t.insert(t.root, 10)
t.root = t.insert(t.root, 20)
t.root = t.insert(t.root, 30)
t.root = t.insert(t.root, 40)
t.root = t.insert(t.root, 50)

print("Inorder Traversal:")
t.inorder(t.root)