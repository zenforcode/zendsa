#include <memory>
#include <vector>
template <typename T, std::shared_ptr<V>> struct dictionary_item {
    dictionary_item(const T& key const std::shared_ptr<V>& value): key(key), value(value) {};
    T key;
    std::shared_ptr<V> value;
}
template<typename T, std::shared_ptr<V>> class dictionary {
    public:
    std::optional<std::shared_ptr<V>> search_key(const T& key) const
    {
         for (auto item&: keys) {
            if (item.key == key) {
                return std::optional<std::shared_ptr<V>(item.value);
            }
         }
         return std::nullopt;
    }
    void insert_key(const T& key, const V& value)
    {
        auto item = dictionary_item<T,V>(key, value);
        keys.push_back(std::move(item));
    }
    bool delete_key(const std:shared_ptr<V>& item) {
        dictionary_item<T,V> to_delete;
        std::remove_if(std::begin(key_arrays), std::end(key_arrays), [](auto& element){ element == item});
        return false;
    }
    private:
        std::vector<dictionary_item<T,V>> key_arrays;
}
