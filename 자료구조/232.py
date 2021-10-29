# 지윤
from collections import deque


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        a = self.queue.popleft()
        self.queue.appendleft(a)
        return a

    def empty(self) -> bool:
        return not self.queue
