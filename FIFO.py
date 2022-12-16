from queues2 import Queue

fifo = Queue("Person 1", "Person 2", "Person 3")
print("In line: ", len(fifo), "Person/s")

for element in fifo:
    print(element)

print("In line: ", len(fifo), "Person/s")