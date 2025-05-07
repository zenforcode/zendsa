#include <memory>
template <typename T> class tree {
    T item;
    std:shared_ptr<tree<T>> parent;
    std::shared_ptr<tree<T>> left;
     
};