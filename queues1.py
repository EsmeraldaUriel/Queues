from collections import deque


class Queue:
    def __init__(self):
        self._elements = deque()