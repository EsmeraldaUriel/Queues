from collections import deque


class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

