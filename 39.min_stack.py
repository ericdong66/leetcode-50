# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Time:  O(n)
# Space: O(1)


class MinStack(object):

    def __init__(self):
        self.stack, self.minStack = [], []

    def push(self, x):
        self.stack.append(x)
        if len(self.minStack):
            if x < self.minStack[-1][0]:
                self.minStack.append([x, 1])
            elif x == self.minStack[-1][0]:
                self.minStack[-1][1] += 1
        else:
            self.minStack.append([x, 1])

    def pop(self):
        x = self.stack.pop()
        if x == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
            if self.minStack[-1][1] == 0:
                self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.minStack[-1][0]


if __name__ == "__main__":
    stack = MinStack()
    for i in [1, 2, 3, 3, 1]:
        stack.push(i)
    while stack.stack:
        print(stack.top(), stack.get_min())
        stack.pop()
