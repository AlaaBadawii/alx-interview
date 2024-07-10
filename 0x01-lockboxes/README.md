# Lockboxes

This repository contains the solution to the lockboxes problem.

## Problem Description

You are given `n` number of lockboxes, each containing a list of keys. Some of the keys can unlock other boxes. Your task is to determine if all the boxes can be opened by sequentially unlocking the boxes using the keys.

## Approach

To solve this problem, we can use a depth-first search (DFS) algorithm. We start by initializing a set to keep track of the boxes we have visited. Then, we recursively explore each box and its corresponding keys, marking them as visited. If we encounter a box that we have already visited, it means there is a cycle and not all boxes can be opened.

## Implementation

The solution is implemented in Python. The main function `can_unlock_all_boxes` takes a list of lockboxes as input and returns a boolean value indicating whether all the boxes can be opened or not.

```python
def can_unlock_all_boxes(lockboxes):
    visited = set()
    return dfs(0, lockboxes, visited)

def dfs(box, lockboxes, visited):
    if box in visited:
        return False
    
    visited.add(box)
    
    for key in lockboxes[box]:
        if key < len(lockboxes):
            if not dfs(key, lockboxes, visited):
                return False
    
    return True
```

## Complexity Analysis

The time complexity of this solution is O(n + m), where n is the number of boxes and m is the total number of keys. The space complexity is O(n), where n is the number of boxes.
