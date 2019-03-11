# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
# Time:  O(2^n)
# Space: O(n)


class Solution:
    def __init__(self):
        self.lookup = {
            1: 1,
            2: 2,
        }

    def fibonacci2(self, n):
        result = self.lookup.get(n)
        if result is not None:
            return result
        result = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        self.lookup[n] = result
        return result

    def fibonacci(self, n):
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current,
        return current

    def climb_stairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.fibonacci2(n - 1) + self.fibonacci2(n - 2)


if __name__ == "__main__":
    print(Solution().climb_stairs(26))

