from collections import deque


class MyStack(object):

    def __init__(self):
        self.queue_in = deque([])
        self.queue_out = deque([])

    def push(self, x):
        self.queue_in.append(x)
        
    def pop(self):
        # push all elements to queue_out
        if not self.queue_out:
            while self.queue_in:
                self.queue_out.append(self.queue_in.popleft())

        # push all elements back to queue_in except the last one
        while len(self.queue_in) < len(self.queue_out) - 1:
            self.queue_in.append(self.queue_out.popleft())

        return self.queue_out.popleft()
        
    def top(self):
        # push all elements to queue_out
        if not self.queue_out:
            while self.queue_in:
                self.queue_out.append(self.queue_in.popleft())

        # push all elements back to queue_in except the last one
        while len(self.queue_in) < len(self.queue_out) - 1:
            self.queue_in.append(self.queue_out.popleft())

        top = self.queue_out[0]
        self.queue_in.append(self.queue_out.popleft())

        return top
        

    def empty(self):
        return not self.queue_in and not self.queue_out