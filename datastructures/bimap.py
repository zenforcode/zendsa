class bimap:
    def __init__(self):
        self._forward = {}
        self._backward = {}

    def insert(self, key, value):
        if key in self._forward or value in self._backward:
            raise ValueError("Duplicate key or value")
        self._forward[key] = value
        self._backward[value] = key

    def __setitem__(self, key, value):
        self._forward[key] = value
        self._backward[value] = key

    def __getitem__(self, key):
        return self._forward[key]

    def __delitem__(self, key):
        value = self._forward[key]
        del self._backward[value]
        del self._forward[key]

    def __iter__(self):
        return iter(self._forward)

    def items(self):
        return self._forward.items()

    def inv_items(self):
        return self._backward.items()

    def __contains__(self, key):
        return key in self._forward
