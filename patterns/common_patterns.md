## Two pointers
Start the pointers at the edges of the input. Move them towards each other until they meet.

1. Start one pointer at the first index 0 and the other pointer at the last index input.length - 1.
2. Use a while loop until the pointers are equal to each other.
3. At each iteration of the loop, move the pointers towards each other. This means either increment the pointer that started at the first index, decrement the pointer that started at the last index, or both. Deciding which pointers to move will depend on the problem we are trying to solve.
```python
   def solution(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        #Do some logic here depending on the problem
        #Do some more logic here to decide on one of the following:
        #    1. left++
        #    2. right--
        #    3. Both left++ and right--
```

###  Fast and Slow pointer
The key idea is that the pointers start at the same location and then start moving at different speeds. The slow pointer moves one step at a time, while the fast pointer moves by two steps (different speed). Due to the different speeds of the pointers, this pattern is also commonly known as the Hare and Tortoise algorithm, where the Hare is the fast pointer while Tortoise is the slow pointer. If a cycle exists, the two pointers will eventually meet during traversal.
```python
def someCondition(fastPointer, slowPointer) -> bool:
    """
        enforce the condition
    """
    ...
def handleCondition(dataStructure):
    """
        handle condition
    """
    ...
def fastAndSlow(dataStructure):
  # initialize pointers (or indices)
  fastPointer = dataStructure.start   # or 0 if the data structure is an array
  slowPointer = dataStructure.start   # or 0 if the data structure is an array
  
  while fastPointer is not None AND fastPointer.next is not None: 
    # For arrays: WHILE fastPointer < dataStructure.length AND (fastPointer + 1) < dataStructure.length:
    slowPointer = slowPointer.next            
    # For arrays: slowPointer = slowPointer + 1
    fastPointer = fastPointer.next.next       
    # For arrays: fastPointer = fastPointer + 2
    if fastPointer is not None AND someCondition(fastPointer, slowPointer):
      # For arrays: use someCondition(dataStructure[fastPointer], dataStructure[slowPointer]) if needed
      handleCondition(fastPointer, slowPointer)
      break

  # process the result
  processResult(slowPointer)
  # For arrays: processResult(slowPointer) might process dataStructure[slowPointer]
```

## Sliding windows
There is a very common group of problems involving subarrays that can be solved efficiently with sliding window. Let's talk about how to identify these problems.

There is a very common group of problems involving subarrays that can be solved efficiently with sliding window. Let's talk about how to identify these problems.

First, the problem will either explicitly or implicitly define criteria that make a subarray "valid". There are 2 components regarding what makes a subarray valid:

1. A constraint metric. This is some attribute of a subarray. It could be the sum, the number of unique elements, the frequency of a specific element, or any other attribute.
2. A numeric restriction on the constraint metric. This is what the constraint metric should be for a subarray to be considered valid.


Second, the problem will ask you to find valid subarrays in some way.

1. The most common task you will see is finding the best valid subarray. The problem will define what makes a subarray better than another. For example, a problem might ask you to find the longest valid subarray.

2. Another common task is finding the number of valid subarrays. We will take a look at this later in the article


Examlples:
- Find the longest subarray with a sum less than or equal to k
- Find the longest substring that has at most one "0"
- Find the number of subarrays that have a product less than k

### Key Idea.

The idea behind a sliding window is to consider only valid subarrays. Recall that a subarray can be defined by a left bound (the index of the first element) and a right bound (the index of the last element). In sliding window, we maintain two variables left and right, which at any given time represent the current subarray under consideration.

Initially, we have left = right = 0, which means that the first subarray we look at is just the first element of the array on its own. We want to expand the size of our "window", and we do that by incrementing right. When we increment right, this is like "adding" a new element to our window.

But what if after adding a new element, the subarray becomes invalid? We need to "remove" some elements from our window until it becomes valid again. To "remove" elements, we can increment left, which shrinks our window.


```bash
function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer
```

- Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k.

# Prefix sum
Prefix sum is a technique that can be used on arrays (of numbers). The idea is to create an array prefix where prefix[i] is the sum of all elements up to the index i (inclusive). For example, given nums = [5, 2, 1, 6, 3, 8], we would have prefix = [5, 7, 8, 14, 17, 25].

```
prefix = [nums[0]]
for (int i = 1; i < nums.length; i++)
    prefix.append(nums[i] + prefix[prefix.length - 1])
```

A prefix sum is a great tool whenever a problem involves sums of a subarray. 
It only costs  O(n)  to build but allows all future subarray queries to be 
O(1), so it can usually improve an algorithm's time complexity by a factor of 
O(n), where  n is the length of the array. Let's look at some examples.

Building a prefix sum is a form of pre-processing. Pre-processing is a useful strategy in a variety of problems where we store pre-computed data in a data structure before running the main logic of our algorithm. While it takes some time to pre-process, it's an investment that will save us a huge amount of time during the main parts of the algorithm.

## Example 

*Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.*

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
```python
def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans
```
## Hashing
HashMap is an unordered data structure that stores key-value pairs. A hash map can add and remove elements in O(1)
O(1), as well as update values associated with a key and check if a key exists, also in 
O
(
1
)
O(1). You can iterate over both the keys and values of a hash map, but the iteration won't necessarily follow any order. In some languages javascript and python preserve
the order of insertion.

## Set
A set is another data structure that is very similar to a hash table. It uses the same mechanism for hashing keys into integers. The difference between a set and hash table is that sets do not map their keys to anything. Sets are more convenient to use when you only care about checking if elements exist.


### Pattern: Counting.
Counting is a very common pattern with hash maps. By "counting", we are referring to tracking the frequency of things. This means our hash map will be mapping keys to integers. Anytime you need to count anything, think about using a hash map to do it.

Example
```
Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
```
Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".

## Linked List. 
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Let prev_node be the node at position i - 1
def delete_node(prev_node):
    prev_node.next = prev_node.next.next
```

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Let node be the node at position i
def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

# Let node be the node at position i
def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
```

### Fast and slow pointers

Fast and slow pointers is an implementation of the two pointers technique that we learned in the arrays and strings chapter. The idea is to have two pointers that don't move side by side. This could mean they move at different "speeds" during iteration, begin iteration from different locations, or any other abstract difference.

When the pointers move at different speeds, usually the "fast" pointer moves two nodes per iteration, whereas the "slow" pointer moves one node per iteration (although this is not always the case).

```python
function fn(head):
    slow = head
    fast = head

    while fast and fast.next:
        Do something here
        slow = slow.next
        fast = fast.next.next
```

Example:
```
def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
    
    for _ in range(length // 2):
        head = head.next
    
    return head.val
```

### Reversing a linked list.

While reversing a linked list is a common interview problem in itself, it is also a technique that can be a step in solving different problems. Elegantly performing the reversal requires a good understanding of how to move pointers around, which we will aim to achieve in this article.

```
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next # first, make sure we don't lose the next node
        curr.next = prev      # reverse the direction of the pointer
        prev = curr           # set the current node to prev for the next node
        curr = next_node      # move on
        
    return prev
```

## Stack 
Stacks is LIFO, which stands for last in, first out. The last (most recent) element placed inside is the first element to come out.

String questions involving stacks are popular. Normally, string questions that can utilize a stack will involve iterating over the string and putting characters into the stack, and comparing the top of the stack with the current character at each iteration.


## Quueue

While a stack followed a LIFO pattern, a queue follows FIFO (first in first out). In a stack, elements are added and removed from the same side. In a queue, elements are added and removed from opposite sides. Like with a stack, there are multiple ways to implement a queue, but the important thing that defines it is the abstract interface of adding and removing from opposite sides.
```
import collections
queue = collections.deque()

# If you want to initialize it with some initial values:
queue = collections.deque([1, 2, 3])

# Enqueueing/adding elements:
queue.append(4)
queue.append(5)

# Dequeuing/removing elements:
queue.popleft() # 1
queue.popleft() # 2

# Check element at front of queue (next element to be removed)
queue[0] # 3

# Get size
len(queue) # 3
```

## Monotonic Stack

## Tree

```
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
```
In binary tree problems, you will be given a reference to the root of a binary tree as the input. You can access the root's left subtree with root.left and the root's right subtree with root.right. Like with linked lists, each node will also carry a value val as data. In a linked list, the tail (last node) has its next pointer as null. In a binary tree, if a node does not have a left child, then node.left will be null, and vice-versa with the right child. Remember that if both children are null, then the node is a leaf.


Level Order Traversal
Pre-order traveraal
In-order traversal DFS
Post Order Traversla DFS
Binary Tree DFS using
Binary Tree BFS.


```
from collections import deque

def print_all_nodes(root):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        # do some logic here for the current level

        for _ in range(nodes_in_current_level):
            node = queue.popleft()
            
            # do some logic here on the current node
            print(node.val)

            # put the next level onto the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

When to use BFS vs DFS?

We mentioned earlier that in many problems, it doesn't matter if you choose preorder, inorder, or postorder DFS, the important thing is that you just visit all nodes. If you have a problem like this, then it doesn't matter if you use BFS either, because every "visit" to a node will store sufficient information irrespective of visit order.

Because of this, in terms of binary tree algorithm problems, it is very rare to find a problem that using DFS is "better" than using BFS. However, implementing DFS is usually quicker because it requires less code, and is easier to implement if using recursion, so for problems where BFS/DFS doesn't matter, most people end up using DFS.

On the flip side, there are quite a few problems where using BFS makes way more sense algorithmically than using DFS. Usually, this applies to any problem where we want to handle the nodes according to their level. We'll see this in the upcoming example and practice problems.

In an interview, you may be asked some trivia regarding BFS vs DFS, such as their drawbacks. The main disadvantage of DFS is that you could end up wasting a lot of time looking for a value. Let's say that you had a huge tree, and you were looking for a value that is stored in the root's right child. If you do DFS prioritizing left before right, then you will search the entire left subtree, which could be hundreds of thousands if not millions of operations. Meanwhile, the node is literally one operation away from the root. The main disadvantage of BFS is that if the node you're searching for is near the bottom, then you will waste a lot of time searching through all the levels to reach the bottom.


Example:
Given the root of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see ordered from top to bottom.



BST

With a binary search tree, operations like searching, adding, and removing can be done in 
O
(
log
⁡
n
)
O(logn) time on average, where 
n
n is the numb


Example 1: 938. Range Sum of BST

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

```
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            if node.left and low < node.val:
                stack.append(node.left)
            if node.right and node.val < high:
                stack.append(node.right)
            
        return ans

```
# Graphs
A graph is any collection of nodes and connections between those nodes.

Edges of a node can either be directed or undirected. Directed edges mean that you can only traverse in one direction. If you're at node A and there is a directed edge to node B, you can move from A -> B, but once you're at B you can't move B -> A. In graphical representations, directed edges will be arrows between nodes. Undirected edges mean that you can traverse in both directions. So using the same example, you can move from A -> B and B -> A. In graphical representations, undirected edges will just be straight lines between nodes.

### Connected component.
A connected component of a graph is a group of nodes that are connected by edges.

The number of edges that can be used to reach the node is the node's indegree. The number of edges that can be used to leave the node is the node's outdegree. Nodes that are connected by an edge are called neighbors


```
from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        # graph[y].append(x)
        # uncomment the above line if the graph is undirected
    
    return graph
```
Second input format: adjacency list
Second input format: adjacency matrix



Example 1: 547. Number of Provinces

There are n cities. A province is a group of directly or indirectly connected cities and no other cities outside of the group. You are given an n x n matrix isConnected where isConnected[i][j] = isConnected[j][i] = 1 if the 
i
t
h
i 
th
  city and the 
j
t
h
j 
th
  city are directly connected, and isConnected[i][j] = 0 otherwise. Return the total number of provinces.


  from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                # the next 2 lines are needed to prevent cycles
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        # build the graph
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        seen = set()
        ans = 0
        
        for i in range(n):
            if i not in seen:
                # add all nodes of a connected component to the set
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans


### Implicit Graph
Cases where the input is nto a graph but is a graph proble,


#heap
There are multiple ways to implement a heap, although the most popular way is called a binary heap using an array. In the trees and graphs chapter, we saw that binary trees are typically implemented with a Node object.

A binary heap implements a binary tree, but with only an array. The idea is that each element in the array is a node in the tree. The smallest element in the tree is the root, and the following property is maintained at every node: if A is the parent of B, then A.val <= B.val. Notice that this property directly implies that the root is the smallest element.

# In Python, we will use the heapq module
# Note: heapq only implements min heaps
from heapq import *

# Declaration: heapq does not give you a heap data structure.
# You just use a normal list, and heapq provides you with
# methods that can be used on this list to perform heap operations
heap = []

# Add to heap
heappush(heap, 1)
heappush(heap, 2)
heappush(heap, 3)

# Check minimum element
heap[0] # 1

# Pop minimum element
heappop(heap) # 1

# Get size
len(heap) # 2

# Bonus: convert a list to a heap in linear time
nums = [43, 2, 13, 634, 120]
heapify(nums)


You are given an array of integers stones where stones[i] is the weight of the 
i
t
h
i 
th
  stone. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. If x == y, then both stones are destroyed. If x != y, then x is destroyed and y loses x weight. Return the weight of the last remaining stone, or 0 if there are no stones left.

  
  # Grreedy algorithm
  A greedy algorithm is any algorithm that makes the locally optimal decision at every step.


  LeetCode would like to work on some projects to increase its capital before IPO. You are given n projects where the 
i
t
h
i 
th
  project has a profit of profits[i] and a minimum capital of capital[i] is needed to start it. Initially, you have w capital. When you finish a project, the profit wil
l be added to your total capital. Return the max capital possible if you are allowed to do up to k projects.
# Binary Search
# backtracing
Backtracking is a way to efficiently run through all possibilities in a problem. It typically uses an optimization that involves abandoning a "path" once it is determined that the path cannot lead to a solution. The idea is similar to binary search trees - if you're looking for a value x, and the root node has a value greater than x, then you know you can ignore the entire right subtree. Because the number of nodes in each subtree is exponential relative to the depth, backtracking can save huge amounts of computation.
Abandoning a path is also sometimes called "pruning".

To summarize the difference between exhaustive search and backtracking:

In an exhaustive search, we generate all possibilities and then check them for solutions. In backtracking, we prune paths that cannot lead to a solution, generating far fewer possibilities.


Backtracking is almost always implemented with recursion - it really doesn't make sense to do it iteratively. In most backtracking problems, you will be building something, either directly (like modifying an array) or indirectly (using variables to represent some state). Here is some pseudocode for a general backtracking format:

// let curr represent the thing you are building
// it could be an array or a combination of variables

function backtrack(curr) {
    if (base case) {
        Increment or add to answer
        return
    }

    for (iterate over input) {
        Modify curr
        backtrack(curr)
        Undo whatever modification was done to curr
    }
}
### Pattern backtracking: generation
One common type of problem that can be solved with backtracking are problems that ask you to generate all of something.

Given an array nums of distinct integers, return all the possible permutations in any order.

For example, given nums = [1, 2, 3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].


#More constrained backtracking
Report Issue
Generation problems are relatively straightforward and usually follow the same format - let's take a look at some other backtracking problems.

Example 1: 39. Combination Sum

Given an array of distinct positive integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path, start, curr):
            if curr == target:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if curr + num <= target:
                    path.append(num)
                    backtrack(path, i, curr + num)
                    path.pop()     
        
        ans = []
        backtrack([], 0, 0)
        return ans

Example 3: 79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 3: 79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def backtrack(row, col, i, seen):
            if i == len(word):
                return True

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    if board[next_row][next_col] == word[i]:
                        seen.add((next_row, next_col))
                        if backtrack(next_row, next_col, i + 1, seen):
                            return True
                        seen.remove((next_row, next_col))
            
            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True
        
        return False

# Dynamic programming
Dynamic programming (DP) is a problem-solving technique. Usually, problems where you use DP can only be solved with DP (in a reasonable time complexity). For many people, DP is the most feared topic. To be honest, there is a large stigma around DP. This is likely a combination of:

If you don't know DP, then it is almost impossible to solve a DP problem, even if it's an easy one
DP isn't as common in interviews - some companies even ban it, which means people have less of an incentive to learn it

In short, dynamic programming is just optimized recursion. Let's say you had some recursive function that returned the answer to the original problem treating whatever you call the function with as the input. We saw this idea extensively in the tree section. For example, we would frequently define a function dfs that took a node and returned the answer to the original problem as if the input was the subtree rooted at node.

The idea behind dynamic programming is the exact same. We define some recursive function, usually called dp, that returns the answer to the original problem as if the arguments you passed to it were the input.

The arguments that a recursive function takes represents a state. When we looked at tree problems, we never visited a node more than once in our DFS, which means that a state was never repeated. The difference with DP is that states can be repeated, usually an exponential number of times. To avoid repeating computation, we use something called memoization. When we find the answer (the return value) for a given state, we cache that value (usually in a hash map). Then in the future, if we ever see the same state again, we can just refer to the cached value without needing to re-calculate it.

The arguments that a recursive function takes represents a state. When we looked at tree problems, we never visited a node more than once in our DFS, which means that a state was never repeated. The difference with DP is that states can be repeated, usually an exponential number of times. To avoid repeating computation, we use something called memoization. When we find the answer (the return value) for a given state, we cache that value (usually in a hash map). Then in the future, if we ever see the same state again, we can just refer to the cached value without needing to re-calculate it.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

memo = {}

This improves our time complexity to 
O
(
n
)
O(n) - which is, of course, extremely fast compared to 
O
(
2
n
)
O(2 
n
 ). The first approach is just basic recursion - by memoizing results to avoid duplicate computation, it becomes dynamic programming.



 Another way to approach a dynamic programming problem is with a "bottom-up" algorithm. In bottom-up, we start at the bottom (base cases) and work our way up to larger problems. This is done iteratively and also known as tabulation. Here is the bottom-up version of Fibonacci:
 def fibonacci(n):
    arr = [0] * (n + 1)
    # base case - the second Fibonacci number is 1
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[n]


Problems that should be solved with DP usually have two main characteristics:

The problem will be asking for an optimal value (max or min) of something or the number of ways to do something.
What is the minimum cost of doing ...
What is the maximum profit of ...
How many ways are there to ...
What is the longest possible ...
At each step, you need to make a "decision", and decisions affect future decisions.
A decision could be picking between two elements
Decisions affecting future decisions could be something like "if you take an element x, then you can't take an element y in the future"



State
We briefly talked about state in earlier chapters. State refers to a set of variables that can fully describe a scenario. When we looked at tree problems, every recursive call to dfs took node, and maybe some other variables as arguments. These arguments represent the state. We'll see in the next article that the first step to creating DP algorithms is deciding on what state variables are necessary.

When we talked about trees, we said that each function call to dfs would return the answer to the original problem as if the state passed to the call was the input. With DP, it's the same. A call to dp(state) should return the answer to the original problem as if state was the input.

The following are common state variables that you should think about:

An index along an input string, array, or number. This is the most common state variable and will be a state variable in almost all problems, and is frequently the only state variable. With Fibonacci, the "index" refers to the current Fibonacci number. If you are dealing with an array or string, then this variable will represent the array/string up to and including this index. For example, if you had nums = [0, 1, 2, 3, 4] and you had a state variable i = 2, then it would be like if nums = [0, 1, 2] was the input.
A second index along an input string or array. Sometimes, you need another index variable to represent the right bound of the array. Again, if you had nums = [0, 1, 2, 3, 4] and two state variables along the input, let's say i = 1 and j = 3, then it would be like nums = [1, 2, 3] - we are only considering the input between and including i and j.
Explicit numerical constraints given in the problem. This will usually be given in the input as k. For example, "you are allowed to remove k obstacles". This state variable would represent how many more obstacles we are allowed to remove.
A boolean to describe a status. For example, "true if currently holding a package, false if not".
The number of state variables used is the dimensionality of an algorithm. For example, if an algorithm uses only one variable like i, then it is one dimensional. If a problem has m



Complexity analysis for DP algorithms is very easy. Like with trees/graphs, we calculate each state only once. Therefore, if there are 
N
N possible states, and the work done at each state is 
F
F, then your time complexity will be 
O
(
N
⋅
F
)
O(N⋅F). Notice that this is the exact same argument we used in the tree and graph problems.

The space complexity will be 
O
(
N
)
O(N) - if we are doing top-down, our hash map will store all the states at the end. If we are doing bottom-up, the array we use for tabulation will be the same size as the number of states.



Frameworkd

For this article, we're going to use Min Cost Climbing Stairs as an example. We will start with a top-down solution.

You are given an integer array cost where cost[i] is the cost of the 
i
t
h
i 
th
  step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor (outside the array, not the last index of cost).


To create any DP algorithm, there are 3 main components.

1. A function or data structure that will compute/contain the answer to the problem for any given state

Since we're starting with top-down, we will be talking about a function here. This involves two parts. First, we need to decide what the function is returning. Second, we need to decide on what arguments the function should take (state variables).

The problem is asking for the minimum cost to climb the stairs. So, let's define a function dp(state) that returns the minimum cost to climb the stairs for a given state.

What state variables do we need? The only relevant state variable would be an index along the input, let's call it i.




What state variables do we need? The only relevant state variable would be an index along the input, let's call it i.

A good way to think about state variables is to imagine if the problem was a real-life scenario. What information do you need to 100% describe a scenario? We certainly need to know what step we're on - that's where i comes in. What about the color of your socks? Standing on the 5th step with green socks is technically a different state than standing on the 5th step with red socks, but it doesn't change the cost of the steps, or anything relevant.


Therefore, let's have a function dp(i) that returns the minimum cost to climb the stairs up to the 
i
t
h
i 
th
  step - i.e. if the input was the subarray from index 0 up to and including i.




  2. A recurrence relation to transition between states

A recurrence relation is an equation used to calculate states. With Fibonacci, the recurrence relation was 
F
n
=
F
n
−
1
+
F
n
−
2
F 
n
​
 =F 
n−1
​
 +F 
n−2
​
 .

In this problem, let's say we wanted to figure out the minimum cost of climbing to the 
10
0
t
h
100 
th
  step. The problem states that at each step, we are allowed to take one or two steps. That means, to get to the 
10
0
t
h
100 
th
  step, we must have arrived from the 
9
9
t
h
99 
th
  or 
9
8
t
h
98 
th
  step. Therefore, the minimum cost of climbing to the 
10
0
t
h
100 
th
  step is either the minimum cost of getting to the 
9
9
t
h
99 
th
  step + the cost of the 
9
9
t
h
99 
th
  step, or the minimum cost of getting to the 
9
8
t
h
98 
th
  step + the cost of the 
9
8
t
h
98 
th
  step.

dp(100) = min(dp(99) + cost[99], dp(98) + cost[98])



dp(i) = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])


Which is the recurrence relation of this problem. Typically, finding the recurrence relation is the hardest part of constructing a DP algorithm. This one is relatively straightforward, but we'll see later that recurrence relations can be much more complicated.




3. Base cases

The recurrence relation is useless on its own. We still can't figure out dp(100) because we don't know dp(99) or dp(98). If we try to find them, we have the same problem - how can we know dp(98) if we don't know dp(97) or dp(96)? By itself, the recurrence relation will continue forever until dp(-infinity).

We need base cases so that our function eventually returns actual values. The problem states that we can start at steps 0 or 1. Therefore, the base cases are:

dp(0) = dp(1) = 0



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. A function that returns the answer
        def dp(i):
            if i <= 1:
                # 3. Base cases
                return 0
            
            if i in memo:
                return memo[i]
            
            # 2. Recurrence relation
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))