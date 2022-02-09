class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def topView(root, distance, level, mp):
    if root == None:
        return

    if distance not in mp:
        mp[distance] = [level, root.data]
    elif level < mp[distance][0]:
        mp[distance] = [level, root.data]

    topView(root.left, distance-1, level+1, mp)
    topView(root.right, distance+1, level+1, mp)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

mp = dict()
topView(root, 0, 0, mp)


from collections import deque

def zigZagOrderTraversal(root):
    if root == None:
        return

    q = deque()
    q.append(root)

    order = 'ltr'

    while q:
        n = len(q)
        for i in range(n):
            if order == 'ltr':
                node = q.popleft()
            else:
                node = q.pop()

            print(node.data)

            if order == 'ltr':
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            else:
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)


        order = order[::-1]





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



def isSumTree(root):
    if root == None:
        return True

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()

        has_child = False

        child_sum = 0
        if node.left:
            has_child = True
            queue.append(node.left)
            child_sum += node.left.data
        if node.right:
            has_child = True
            queue.append(node.right)
            child_sum += node.right.data

        if node.data != child_sum and has_child:
            return False

    return True


root = Node(62)
root.left = Node(16)
root.right = Node(15)
root.left.right = Node(8)
root.left.right.right = Node(8)
root.right.left = Node(4)
root.right.right = Node(7)
root.right.left.left = Node(4)

          62
    16          15
       8      4    7
         8  4



def sumTreeUtil(root):
    if root == None:
        return 0, True

    hasChildren = root.left or root.right

    if not hasChildren:
        return root.data, True

    lSum, isSumEqual = sumTreeUtil(root.left)
    rSum, isSumEqual = sumTreeUtil(root.right)

    if (root.data != lSum + rSum):
        return root.data + lSum + rSum, False

    return root.data + lSum + rSum, True

