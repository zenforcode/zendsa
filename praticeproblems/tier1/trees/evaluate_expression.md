## Evaluate expression

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

```
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
```

1. The leftmost max node evaluates to max(4, 6, sum(5, 7)) = max(4, 6, 12) = 12
2. The rightmost sum node has one child prod(6, 8) = 48
3. The root min node evaluates to min(12, 48) = 12