# Trees in Data Structures :
# 1. What is a Tree?
# A Tree is a non-linear data structure.
# It consists of nodes connected by edges.
# It represents a hierarchical relationship between elements.
# Unlike arrays and linked lists, data is not stored sequentially.

# Example:

#         A
#       /   \
#      B     C
#     / \   / \
#    D   E F   G


# 2. Terminologies of Tree
# 1. Node
# The basic element of a tree.
# Stores data.

# Example:

# A, B, C, D are nodes.
# 2. Root Node
# The topmost node of the tree.
# Every tree has only one root.

# Example:

#       A

# Here,

# A is the root.
# 3. Parent Node
# A node that has one or more children.

# Example:

#      A
#     / \
#    B   C

# A is the parent of B and C.

# 4. Child Node
# A node directly connected below a parent.

# Example:

# A
# |
# B

# B is the child of A.

# 5. Leaf Node
# A node that has no children.
# Also called an external node.

# Example:

#       A
#      / \
#     B   C
#    / \
#   D   E

# Leaf nodes:

# D, E, C
# 6. Internal Node
# Any node having at least one child.

# Example:

# A
# B

# are internal nodes.

# 7. Edge
# A connection between two nodes.

# Example:

# A ---- B

# There is one edge.

# 8. Siblings
# Nodes having the same parent.

# Example:

#       A
#      / \
#     B   C

# B and C are siblings.

# 9. Degree of a Node
# Number of children a node has.

# Example:

#       A
#     / | \
#    B  C  D

# Degree(A) = 3

# 10. Degree of Tree
# Maximum degree among all nodes.

# Example:

#       A
#     / | \
#    B  C  D

# Degree of tree = 3

# 11. Path
# Sequence of nodes connected by edges.

# Example:

# A → B → D

# Path length = 2 edges.

# 12. Level
# Distance from the root.

# Example:

#         A
#       /   \
#      B     C
#     /
#    D


# Node	Level
# A	0
# B,C	1
# D	2

# (Some books start the root at Level 1.)

# 13. Depth of a Node
# Number of edges from the root to that node.

# Example:

# Depth(A) = 0
# Depth(B) = 1
# Depth(D) = 2
# 14. Height of a Node
# Number of edges from that node to the deepest leaf.

# Example:

#       A
#      /
#     B
#    /
#   C

# Height(C) = 0

# Height(B) = 1

# Height(A) = 2

# 15. Height of Tree
# Height of the root node.
# Equal to the longest path from root to any leaf.

# Example:

#       A
#      / \
#     B   C
#    /
#   D

# Height = 2

# 16. Subtree
# A smaller tree formed from any node and its descendants.

# Example:

#       A
#      / \
#     B   C
#    / \
#   D   E

# Subtree rooted at B:

#     B
#    / \
#   D   E


# 17. Ancestors
# All nodes on the path from the root to a given node.

# Example:

#       A
#      /
#     B
#    /
#   D

# Ancestors of D:

# A, B
# 18. Descendants
# All nodes below a given node.

# Example:

#       A
#      /
#     B
#    / \
#   D   E


# Descendants of B:

# D, E
# 3. Properties of Trees
# A tree with N nodes has N − 1 edges.
# There is exactly one path between any two nodes.
# Every node except the root has one parent.
# The root has no parent.
# Trees do not contain cycles.
# 4. Types of Trees
# 1. General Tree
# A node can have any number of children.
#       A
#    / / \ \
#   B C  D  E


# 2. Binary Tree
# Each node has at most 2 children (left and right).
#       A
#      / \
#     B   C



# 3. Binary Search Tree (BST)
# Left child < Parent < Right child.
#       50
#      /  \
#    30    70
#   / \   / \
# 20 40 60 80



# 4. Full Binary Tree
# Every node has either 0 or 2 children.
#       A
#      / \
#     B   C


# 5. Complete Binary Tree
# All levels are full except possibly the last.
# The last level is filled from left to right.
#       A
#      / \
#     B   C
#    / \  /
#   D  E F



# 6. Perfect Binary Tree
# All internal nodes have exactly 2 children.
# All leaf nodes are at the same level.
#         A
#       /   \
#      B     C
#     / \   / \
#    D  E  F  G
# 7. Balanced Binary Tree
# Height difference between left and right subtrees is small (typically at most 1).

# Example:

# AVL Tree
# Red-Black Tree
# 8. Degenerate (Skewed) Tree
# Every node has only one child.
# A
#  \
#   B
#    \
#     C
#      \
#       D

# This behaves like a linked list.

# 5. Tree Traversals
# 1. Preorder (Root → Left → Right)
#         A
#        / \
#       B   C
#      / \
#     D   E

# Output:

# A B D E C
# 2. Inorder (Left → Root → Right)

# Output:

# D B E A C

# For a Binary Search Tree (BST), an inorder traversal visits the values in sorted order.

# 3. Postorder (Left → Right → Root)

# Output:

# D E B C A
# 4. Level Order (Breadth-First)

# Output:

# A B C D E
# 6. Applications of Trees
# File system directories
# Database indexing (B-Tree, B+ Tree)
# Expression trees (calculators, compilers)
# Decision trees (Machine Learning)
# XML/HTML DOM structure
# Organization charts
# DNS hierarchy
# Trie (autocomplete and dictionaries)
# 7. Time Complexity (Binary Search Tree)
# Operation	Average	Worst
# Search	O(log n)	O(n)
# Insert	O(log n)	O(n)
# Delete	O(log n)	O(n)

# If the BST is balanced, these operations remain O(log n).

# Interview Questions
# What is a tree?
# Why does a tree with N nodes have N − 1 edges?
# What is the difference between height and depth?
# What is the difference between a full, complete, and perfect binary tree?
# Why does an inorder traversal of a BST produce sorted output?
# What is the difference between DFS (Preorder, Inorder, Postorder) and BFS (Level Order)?
# What is a balanced tree, and why is it important?
# What is the difference between a Binary Tree and a Binary Search Tree (BST)?