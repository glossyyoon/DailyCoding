from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        a = self.queue.pop()
        self.queue.append(a)
        return a

    def empty(self) -> bool:
        return not self.queue
