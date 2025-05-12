type Nullable<T> = T | null;

class Node<T> {
    value: T;
    left: Nullable<Node<T>>;
    right: Nullable<Node<T>>;

    constructor(value: T) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

export class BinaryTree<T> {
    private _root: Node<T>;

    constructor(value: T) {
        this._root = new Node(value);
    }

    getRoot(): Node<T> {
        return this._root;
    }

    insert(value: T): void {
        this._insertNode(this._root, value);
    }

    delete(value: T): Nullable<Node<T>> {
        if (!this._root) {
            return null;
        }
        this._root = this._deleteNode(this._root, value);
        return this._root;
    }

    private _deleteNode(x: Nullable<Node<T>>, value: T): Nullable<Node<T>> {
        if (x === null) return null;

        if (x.value < value) {
            x.right = this._deleteNode(x.right, value);
        } else if (x.value > value) {
            x.left = this._deleteNode(x.left, value);
        } else {
            if (x.right === null) return x.left;
            if (x.left === null) return x.right;

            // Find the minimum node in the right subtree
            let t = x.right;
            while (t.left !== null) {
                t = t.left;
            }

            // Replace current node's value with that of t
            x.value = t.value;
            // Delete the duplicate from the right subtree
            x.right = this._deleteNode(x.right, t.value);
        }

        return x;
    }

    private _insertNode(root: Nullable<Node<T>>, value: T): Node<T> {
        if (!root) return new Node(value);

        const queue: Node<T>[] = [root];

        while (queue.length > 0) {
            const curr = queue.shift()!;
            if (curr.left === null) {
                curr.left = new Node(value);
                return root;
            } else {
                queue.push(curr.left);
            }

            if (curr.right === null) {
                curr.right = new Node(value);
                return root;
            } else {
                queue.push(curr.right);
            }
        }

        return root;
    }
}
