from collections import deque

class Queue:
    def __int__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)