from tree import Tree, pre_order
if __name__=="__main__":
    t = Tree(10)
    t.insert(8)
    t.insert(5)
    t.insert(9)
    t.insert(15)
    visited = pre_order(t)
    print(visited)
