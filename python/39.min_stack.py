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


class Item(object):
    def __init__(self, value, counter=1):
        self.value = value
        self.counter = counter

    def __repr__(self):
        return "{}.{}".format(self.value, self.counter)


class Min(object):
    def __init__(self):
        self.mini_stack = list()

    def push(self, x):
        if len(self.mini_stack):
            top = self.mini_stack[-1]
            if x < top.value:
                self.mini_stack.append(Item(x))
            elif x == top.value:
                top.counter += 1
        else:
            self.mini_stack.append(Item(x))

    def pop(self, x):
        top = self.mini_stack[-1]
        if x == top.value:
            top.counter -= 1
            if top.counter == 0:
                self.mini_stack.pop()

    def top(self):
        return self.mini_stack[-1].value


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mini_stack = Min()

    def push(self, x):
        self.stack.append(x)
        self.mini_stack.push(x)

    def pop(self):
        x = self.stack.pop()
        self.mini_stack.pop(x)

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.mini_stack.top()


if __name__ == "__main__":
    stack = MinStack()
    for i in [2, 2, 3, 2, 3, 1, 1, 1, 5]:
        stack.push(i)
    while stack.stack:
        print(stack.top(), stack.get_min(), stack.mini_stack.mini_stack[-1])
        stack.pop()
