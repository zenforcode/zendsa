## Algorithm Design
1. Model the problem.
2. Find an algorithm to solve the problem.
3. Is the algorithm fast enough? Does it fits in memory?
4. If not, figure out why?
5. Find a way to address the problem
6. Iterate until satisfied.
It is kind of scientific method to solve it.

## Dynamic connectivity (Union-Find)
Problem: Given a set of N objects you have to:
1. *Union*: Connect two objects.
2. *Find/connected query* : is there a path connecting two objects?

```mermaid
graph TD
    subgraph Initial Sets
        A0((0)) 
        A1((1)) 
        A2((2)) 
        A3((3)) 
        A4((4)) 
        A5((5)) 
    end

    click A0 "javascript:void(0)" "Node 0"
    click A1 "javascript:void(0)" "Node 1"
    click A2 "javascript:void(0)" "Node 2"
    click A3 "javascript:void(0)" "Node 3"
    click A4 "javascript:void(0)" "Node 4"
    click A5 "javascript:void(0)" "Node 5"

    %% After union(0,1), union(1,2)
    subgraph After Unions [ ]
        A0 --- A1
        A1 --- A2

        %% union(3, 4)
        A3 --- A4
    end

    %% find(0, 2) = true
    %% find(0, 4) = false

```