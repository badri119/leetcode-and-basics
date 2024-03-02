class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)


# if input n is either 0 or 1, return n
# if input is > 1, fibonacci will be sum of (n-1) + (n-2)
