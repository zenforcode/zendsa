def reverseWords(arr):
    def mirrorReverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(arr)
    mirrorReverse(arr, 0, n - 1)

    start = None
    for i in range(n + 1):  # Go one past the end
        if i == n or arr[i] == ' ':
            if start is not None:
                mirrorReverse(arr, start, i - 1)
                start = None
        else:
            if start is None:
                start = i

    return arr

