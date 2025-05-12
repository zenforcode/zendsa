""""""
Given the root of a tree representing an arithmetic expression, evaluate it.

We use this node definition with three fields: `kind`, `num`, and `children`.

- The `kind` field can be either `"num"` or one of `"sum"`, `"product"`, `"max"`, or `"min"`. It determines the node's type: it can be a number node or an operation node.

A number node has `kind = "num"` and stores an integer value in its `num` field. It has no children.

An operation node has `kind` equal to one of `"sum"`, `"product"`, `"max"`, or `"min"`. It has one or more children nodes in its `children` field.

The value of a number node is simply its `num` value. The value of an operation node is:

- For `"sum"`: The sum of all its children's values
- For `"product"`: The product of all its children's values (the product of a single value is itself)
- For `"max"`: The maximum among its children's values
- For `"min"`: The minimum among its children's values

Return the value of evaluating the entire expression tree.

""""
Example:

Input:
     min
    /   \
 max     +
 /|\      \
4 6 +      *
   / \    / \
  5   7  6   8

Output: 12

1. The leftmost max node evaluates to max(4, 6, sum(5, 7)) = max(4, 6, 12) = 12
2. The rightmost sum node has one child prod(6, 8) = 48
3. The root min node evaluates to min(12, 48) = 12
```

class Node:
    def __init__(self, kind = None, num = None, childern = None):
        self.kind = kind
        self.num = num
        self.children = children
        
def compute(root: Node, collected: list):
  if not root:
    return
  if root.children:
    for child in root.children:
        compute(child, collected)
  else:
    match root.kind:
      case "num":
        collected.append(root.num)
      case "sum":
        s = sum(collected)
        collected = [s]
      case "product":
        p = 1
        for i in collected:
          p*=i
        collected = [p]
      case "max":
        mx = max(collected)
        collected = [m]
      case "min":
        mn = min(collected)
        collected = [mn]



"""
    min
    /   \
 max     +
 /|\      \
4 6 +      *
   / \    / \
  5   7  6   8

"""
root = Node(kind='min', children=[Node(kind='max', children=[])])
compute()