class MinStack(object):

    def __init__(self):
        self.stack = []
        # Store the minimum value at each state of the stack.
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if self.min_stack:
            min_val= min(self.min_stack[-1], value)
            self.min_stack.append(min_val)
        else:
            self.min_stack.append(value)
        
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.min_stack[-1]
        