'''
Given reference to the root of a binary tree & an integer value x,
fina all nodes distance k from the node with value x

k = 2
x = 3
root =     1
          / \
         3   2
        / \   \
       4   6   7

output: [2]
k = 1
x = 3
output: [1, 4, 6]

1. find node with value x and store parent pointers for each node (using preorder)
2. initialize a queue with just target node and distance of 0
3. carry out the bfs and terminate (add to output list) when distance == k
4. for the bfs, neighbers for a node inlude left, right, and parent nodes
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root, x, k):
    target_node = [None]
    parent_map = {}
    output = []

    def preorder(node, parent=None):
        if not node:
            return
        
        if node.val == x:
            target_node[0] = node
        parent_map[node] = parent
        preorder(node.left, node)
        preorder(node.right, node)
    preorder(root)

    # If target node is not found
    if not target_node[0]:
        return []

    queue = deque([(target_node[0], 0)])
    seen = set()

    while queue:
        node, dist = queue.popleft()
        seen.add(node)

        if dist == k:
            output.append(node.val)
        if dist < k:  # Ensure we only add nodes if we haven't reached the required distance
            for nei in [node.left, node.right, parent_map[node]]:
                if nei and nei not in seen:
                    queue.append((nei, dist + 1))
                    seen.add(nei)  # Mark it as seen immediately to avoid re-processing

    return output

def test():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(7)

    result = distanceK(root, 3, 2)
    print(result)  # Output: [2]

    result = distanceK(root, 3, 1)
    print(result)  # Output: [1, 4, 6]

test()
