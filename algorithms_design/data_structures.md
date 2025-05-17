# Data structures summary
Data structered can be neatly classified:
 - contiguously allocated: contiguosuly alloccated are composed by single slabs of memory: array, matrixes, heaps, hash tables
 - linked: are composed of distinct chunks of memory bound together by pointers: lists, trees, graphs, adjectent list, hash maps.
## Array
Arrays have the following strenght:
    1. *Constant access time given the index*: because the index of one element maps directly to a memort address, we can access 
        arbitrary items with O(1).
    2. *Space efficiency*: array consist of pure data so no space is wasted to keeping accounting information such as trees or linked lists. Array are of fixed size.
    3. *Memory locality* and *cache friendly*: Physical continuity between successive data accesses help to exploit the processor cache, if the array is not bigger of the cache size, typically is alwas in cache.

Arrays has the following weaknesses:
  1. They are no resizable.

Modern Programming Languages use both arrays and dyamic arrays.
## Python
Python has not concept of fixed size array. Everything is a list, a dynamic array
```Python
current_list = 10 * [1]
for x in current_list:
    print('Item: {x}')
```
## Java
Java has both fixed size arrays and dynamic ones, called ArrayList.
```Java
int [] firstNumbers = new int[100];
for (int k =0; k < 100; k++) {
    if ((k % 2) == 0) {
        firstNumbers[k] = k; // No new object is created.
    }
}
```
In Java and also in C# we apply boxing in case of dynamic arrays.
```Java
var firstNumbers = new ArrayList<Integer>();
for (int k =0; k < 100; k++) {
    if ((k % 2) == 0) {
        firstNumbers.add(k); // Boxing - we create 50 Integer objects
    }
}
```
## C++ 
C++ has both fixed size arrays in the stack, fixed size arrays in the heap, dynamic size arrays in the heap.
Here we've more features.
- static size array on the stack.
- std::array
- std::vector
```C++
int firstNumbers[100];
for (int k =0; k < 100; k++) {
    if ((k % 2) == 0) {
        firstNumbers[k] = k; // No new object is created.
    }
}
```
This is more idiomatic
```C++
std::array<int, 100> firstNumbers;
for (int k =0; k < 100; k++) {
    if ((k % 2) == 0) {
        firstNumbers[k] = k; // No new object is created.
    }
}
```
Dynamic array
```C++
std::vector<int> firstNumbers;
for (int k =0; k < 100; k++) {
    if ((k % 2) == 0) {
        firstNumbers.emplace_back(k); // No new object is created.
    }
}
```
The idea of dynamic array is double the memory behind them everytime they go out of memory and copying the lower half in the new one.
If you think number of doubling times is O(log(n)), so the total number of movement is 2n.
In the worst case possible we've O(n), but most of the time is also O(1). Skiena speaks about amortized guarantees (clarify).




