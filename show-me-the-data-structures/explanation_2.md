## Reasoning Behind Decisions:
  We use an explicity stack (with a deque) instead of recursion for traversing directory starting
  from the current directory provided as input. We prefer use a stack in order to avoid any 
  depth problems that might be happen due eccessive depth of the directory tree. In this process:
   - os.listdir(path) is used to retrieve files and directories in the given path.
   - The stack.pop() mechanism ensures that directories are expanded depth-first.
   In case we're dealing with files we check the suffix and it matches we put it on a list.
   As final result we sort the list.
## Time Efficiency:
    O(N) in the worst case, where N is the total number of files and directories in the tree.
    Sorting at the end adds O(M log M), where M is the number of matching files.
    So O(N) + O(M log M), where M <=N, we can assume O(N log N)
## Space Efficiency:
    O(D) stack space, where D is the depth of the directory tree.
    O(M) list storage, where M is the number of files found.