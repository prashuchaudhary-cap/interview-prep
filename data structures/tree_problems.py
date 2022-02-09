Reply1
    - Reply1
        - Reply3
            - Reply7
            - Reply8
        - Reply4
    - Reply5
    - Reply6


AddReply(parentReplyId, reply) -- O(n)
GetAllReplies(replyId)
GetAllRepliesTillDepth(replyId, depth)
GetCountOfAllReplies(replyId)

max_depth = 10



from collections import deque

# A binary tree node has key, pointer to left
# child and a pointer to right child
class Node:
    def __init__(self, key):

        self.key = key
        self.left = None
        self.right = None

# Function to print corner node at each level
def printCorner(root: Node):

    # If the root is null then simply return
    if root == None:
        return

    # Do level order traversal
    # using a single queue
    q = deque()
    q.append(root)

    while q:
        # n denotes the size of the current
        # level in the queue
        n = len(q)
        for i in range(n):
            node = q.popleft()

            # If it is leftmost corner value or
            # rightmost corner value then print it
            if i == 0 or i == n - 1:
                print(node.key, end = " ")

            # push the left and right children
            # of the temp node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)



from collections import namedtuple

fields = ('val', 'left', 'right')
Node = namedtuple('Node', fields, defaults=(None,) * len(fields))

from typing import Any, NamedTuple

class Node(NamedTuple):
    val: Any
    left: 'Node' = None
    right: 'Node' = None


def insert(node, key):
    """ If the tree is empty,
    return a  node """
    if (node == None):
        return Node(key)

    """ Otherwise, recur down the tree """
    if (key < node.key):
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# A node structure
class Node:

    # A utility function to create a  node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to print level order traversal of given binary tree
def levelOrderTraversal(root):

    # create an empty queue and enqueue root node
    queue = deque()
    # insert the value to the right end of deque
    queue.append(root)

    # loop till queue is empty
    while queue:
        # process each node in queue and enqueue their
        # non-empty left and right child to queue

        curr = queue.popleft()
        # pop from the left end of deque

        print(curr.key, end=' ')

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)



def zigZagOrderTraversal(root):
    if root == None:
        return

    q = deque()
    q.append(root)

    ltr = False

    while q:
        n = len(q)
        for i in range(n):

            if ltr:
                node = q.popleft()
            else:
                node = q.pop()

            print(node.data, end=" ")

            if ltr:
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            else:
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)

        ltr = not ltr

"""
                  1
              /      \
            2           3
          /   \        /  \
         4     5      6     7
        / \   / \    / \   / \
       8   9 10  11 12 13 14 15
"""


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)



def findLCA(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root

    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca



# function to find distance of any node
# from root
def findLevel(root, data, d, level):

    # Base case when tree is empty
    if root is None:
        return

    # Node is found then append level
    # value to list and return
    if root.data == data:
        d.append(level)
        return

    findLevel(root.left, data, d, level + 1)
    findLevel(root.right, data, d, level + 1)

# function to find distance between two
# nodes in a binary tree
def findDistance(root, n1, n2):

    lca = findLCA(root, n1, n2)

    # to store distance of n1 from lca
    d1 = []

    # to store distance of n2 from lca
    d2 = []

    # if lca exist
    if lca:

        # distance of n1 from lca
        findLevel(lca, n1, d1, 0)

        # distance of n2 from lca
        findLevel(lca, n2, d2, 0)
        return d1[0] + d2[0]
    else:
        return -1


def verticalSumUtil(root, distance, mp):
    if root == None:
        return

    if distance in mp:
        mp[distance].append(root.data)
    else:
        mp[distance] = [root.data]

    verticalSum(root.left, distance-1, mp)
    verticalSum(root.right, distance+1, mp)


def verticalSum(root):
    mp = dict()
    verticalSum(root, 0, mp)

    for i in sorted(mp):
        print(sum(mp[i]), end=" ")



def diagonalSumUtil(root, distance, mp):
    if root == None:
        return

    if distance in mp:
        mp[distance] += root.data
    else:
        mp[distance] = root.data

    diagonalSumUtil(root.left, distance+1, mp)
    diagonalSumUtil(root.right, distance, mp)


def diagonalSum(root):
    mp = dict()
    diagonalSumUtil(root, 0, mp)

    sums = []
    for i in sorted(mp):
        sums.append(mp[i])


""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""

def height(node):
    if node is None:
        return 0
    else :
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        #Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
printLevelOrder(root)



# Python program to print right view of Binary Tree

# A binary tree node
class Node:
    # A constructor to create a  Binary tree Node
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

# Recursive function to print right view of Binary Tree
# used max_level as reference list only max_level[0]
# is helpful to us

def rightViewUtil(root, level, max_level):
    # Base Case
    if root is None:
        return

    # If this is the last node of its level
    if (max_level[0] < level):
        print(root.data, end=" "),
        max_level[0] = level

    # Recur for right subtree first, then left subtree
    rightViewUtil(root.right, level+1, max_level)
    rightViewUtil(root.left, level+1, max_level)

def rightView(root):
    rightViewUtil(root, 1, [0])


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

rightView(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)






# Python3 program to convert a binary
# tree to its mirror

# Utility function to create a
# tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

""" Change a tree so that the roles of the
    left and right pointers are swapped at
    every node.

So the tree...
         4
        / \
       2   5
      /     \
     1       3

is changed to...
     4
    / \
   5   2
  /     \
 3       1
"""

def mirror(node):

    if not node:
        return

    """ do the subtrees """
    mirror(node.left)
    mirror(node.right)

    """ swap the pointers in this node """
    temp = node.left
    node.left = node.right
    node.right = temp


""" Helper function to print Inorder traversal."""
def inOrder(node) :

    if (node == None):
        return

    inOrder(node.left)
    print(node.data, end = " ")
    inOrder(node.right)


##############################################
        Top view of Binary Tree
##############################################

from collections import OrderedDict

# A binary tree node
class Node:

    # A constructor to create a
    # Binary tree Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 2**32

        1
      /   \
    2       3
      \
        4
          \
            5
             \
               6

def printTopViewUtil(root, height, hd, mapp):

    # Base Case
    if (root == None):
        return

    # If the node for particular horizontal
    # distance is not present in the map, add it.

    # For top view, we consider the first element
    # at horizontal distance in level order traversal
    # If height of new node is lower, then we replace it.
    if hd not in mapp:
        mapp[hd] = [root.data, height]
    elif  m[hd][1] > height:
        mapp[hd] = [root.data, height]

    # Recur for left and right subtree
    printTopViewUtil(root.left, height + 1, hd - 1, mapp)
    printTopViewUtil(root.right, height + 1, hd + 1, mapp)


def printTopView(root):

    # to store horizontal distance,
    # height and node's data
    mapp = OrderedDict()
    printTopViewUtil(root, 0, 0, mapp)

    # Print the node's value stored
    # by printTopViewUtil()
    for i in sorted(list(m)):
        print(m[i][0], end = " ")

# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

print("Top View : ", end = "")
printTopView(root)


binary_paths = []
def getAllPaths(root, path):
    if root == None:
        return

    path = "{path}{data}".format(path=path, data=root.val)

    if root.left == None and root.right == None:
        binary_paths.append(path)
        return

    getAllPaths(root.left, path)
    getAllPaths(root.right, path)


def sumAllPath(root):
    getAllPaths(root, '')

    tree_sum = 0
    for binary_path in binary_paths:
        tree_sum += int(binary_path, 2)

    print(tree_sum)



