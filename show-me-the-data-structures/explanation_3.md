## Reasoning Behind Decisions:

We're building an Huffman encoding tree and as per encoding and decoding algorithm we need a min heap. 
We've different approaches for each subproblem to take in accounts.
### Building the Huffman tree
- We put O(N) frequency in the min heap, so O(N log N), where N is the number of chars.
- Do successive merge to build the Huffman tree.
## Encoding
- We performs a preorder traversal (Depth-First Search, DFS) of the Huffman tree to generate the codes,
  using recursion, O(log(N)).
- We chars to the list to avoid consecutive expensive string concatation and we do join at the end. O(N) space.
## Decoding
- Visit the tree O(logN), add to a list 


## Time Efficiency:
- Building the heap: O(N log N) (as we insert N nodes).
- Extracting two nodes and inserting the merged node: O(N log N) (for N-1 merges).
- O(N log N), which is optimal for this problem.

## Space Efficiency:
- N nodes for the tree O(N)
- A  list of N elements
- N nodes for the heap.
- O(N) is the final complexity.

