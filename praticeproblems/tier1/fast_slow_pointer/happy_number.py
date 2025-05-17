def isHappy(n: int) -> bool:
    slow_runner = n
    fast_runner = sumOfSquares(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = sumOfSquares(slow_runner)
        fast_runner = sumOfSquares(sumOfSquares(fast_runner))
    return fast_runner == 1

def sumOfSquares(self, number: int) -> int:
    total_sum = 0
    while number > 0:
        number, digit = divmod(number, 10)
        total_sum += digit ** 2
    return total_sum
`
