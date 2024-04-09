'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''

def __init__(self):
    self.stack = []
    self.min_stack = []

def push(self, val):
    self.stack.append(val)

    if not self.min.stack or val <= self.min_stack[-1]:
        self.min_stack.append(val)

def pop(self):
    if self.stack.pop() == self.min_stack[-1]:
        self.min_stack.pop()

def top(self):
    if self.stack:
        return self.stack[-1]

def get_min(self):
    if self.min_stack:
        return self.min_stack[-1]

